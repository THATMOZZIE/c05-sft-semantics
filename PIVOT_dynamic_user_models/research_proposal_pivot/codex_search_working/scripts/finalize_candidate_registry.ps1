param(
    [Parameter(Mandatory = $true)]
    [string]$InputCsv,

    [Parameter(Mandatory = $true)]
    [string]$OutputCsv
)

$ErrorActionPreference = 'Stop'

# Final ranks are an orchestrator judgment after primary-source verification and
# three independent reviews. They intentionally do not equal the provisional
# weighted score order.
$finalRanks = @{
    'E01-CENSORSHIP'        = 1
    'TRANS-04'              = 2
    'C-05-SFT-SEMANTICS'    = 3
    'VL-01'                 = 4
    'C-04-ROLE-ANTICONTROL' = 5
    'C-02-RH-MON'           = 6
    'D1-PSBENCH'            = 7
    'C-01-SPP-RL'           = 8
    'E02-EVAL-AWARENESS'    = 9
    'TRANS-03'              = 10
}

$finalStatus = @{
    'E01-CENSORSHIP'        = 'WINNER'
    'TRANS-04'              = 'RUNNER_UP'
    'C-05-SFT-SEMANTICS'    = 'FINALIST_CONDITIONAL_ACTION_GATE'
    'VL-01'                 = 'TOP5_EXTERNAL_COMPUTE'
    'C-04-ROLE-ANTICONTROL' = 'TOP5_LOCAL_FALLBACK'
    'C-02-RH-MON'           = 'SHORTLIST_PRELIMINARY_SUBSTRATE'
    'D1-PSBENCH'            = 'SHORTLIST_BENCHMARK_VALIDITY'
    'C-01-SPP-RL'           = 'SHORTLIST_UNESTABLISHED_RL_BRANCH'
    'E02-EVAL-AWARENESS'    = 'SHORTLIST_NOVELTY_REJECT'
    'TRANS-03'              = 'SHORTLIST_OVERTAKEN_BY_NEARBY_WORK'
}

$rows = Import-Csv -LiteralPath $InputCsv
if ($rows.Count -eq 0) {
    throw "Candidate CSV contains no rows: $InputCsv"
}

$seen = @{}
foreach ($row in $rows) {
    if ($seen.ContainsKey($row.project_id)) {
        throw "Duplicate project_id: $($row.project_id)"
    }
    $seen[$row.project_id] = $true

    $rank = if ($finalRanks.ContainsKey($row.project_id)) {
        [string]$finalRanks[$row.project_id]
    } else {
        ''
    }
    $status = if ($finalStatus.ContainsKey($row.project_id)) {
        $finalStatus[$row.project_id]
    } else {
        'SCREENED_OUT_BEFORE_INDEPENDENT_REVIEW'
    }

    $row | Add-Member -NotePropertyName final_rank -NotePropertyValue $rank -Force
    $row | Add-Member -NotePropertyName final_disposition -NotePropertyValue $status -Force

    if ($row.project_id -eq 'E01-CENSORSHIP') {
        $row.time_to_first_result_hours = '1-2 for frozen 30-generation qualification; 1-3 additional for 90-generation confirmation'
        $row.first_intervention = 'Cross-question bidirectional answer-boundary residual-state transplant derived on dev items and tested on untouched facts with selectivity controls.'
        $row.kill_rule = 'Stop if the exact 8B behavior fails without prompt/model search, lacks higher-precision confirmation, or the held-out state transplant is not bidirectional and censorship-selective.'
    }
}

$rows |
    Sort-Object -Property @(
        @{Expression={ if ($_.final_rank) { [int]$_.final_rank } else { 999 } }; Descending=$false},
        @{Expression='score_balanced'; Descending=$true},
        @{Expression='project_id'; Descending=$false}
    ) |
    Export-Csv -LiteralPath $OutputCsv -NoTypeInformation -Encoding utf8

Write-Output "Finalized $($rows.Count) candidates -> $OutputCsv"
