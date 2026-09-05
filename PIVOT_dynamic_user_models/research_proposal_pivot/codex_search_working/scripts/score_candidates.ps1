param(
    [Parameter(Mandatory = $true)]
    [string]$InputCsv,

    [Parameter(Mandatory = $true)]
    [string]$OutputCsv
)

$ErrorActionPreference = 'Stop'

$positiveWeights = [ordered]@{
    existing_behavioral_robustness       = 8
    reproducibility_evidence              = 7
    naturalness_deployment_relevance      = 3
    safety_relevance                      = 6
    scientific_surprise                   = 3
    competing_explanations_quality        = 5
    mechanistic_discriminability          = 8
    intervention_usefulness               = 6
    open_weight_availability              = 4
    local_12gb_feasibility                = 7
    code_availability                      = 2
    dataset_cached_output_availability    = 2
    time_to_first_result                  = 7
    total_project_effort_fit              = 7
    neel_mats_fit                         = 7
    novelty_gap_plausibility              = 5
    value_if_mechanism_simple             = 2
    value_if_hypothesis_falsified         = 2
    coherent_artifact_probability         = 5
}

$riskWeights = [ordered]@{
    prompt_model_shopping_risk = 2
    lexical_triviality_risk    = 2
}

$rows = Import-Csv -LiteralPath $InputCsv
if ($rows.Count -eq 0) {
    throw "Candidate CSV contains no rows: $InputCsv"
}

$required = @('project_id', 'title', 'family', 'source_lane') + @($positiveWeights.Keys) + @($riskWeights.Keys)
$available = @($rows[0].PSObject.Properties.Name)
$missing = @($required | Where-Object { $_ -notin $available })
if ($missing.Count -gt 0) {
    throw "Missing required columns: $($missing -join ', ')"
}

function Get-Score([object]$row, [string]$name) {
    $value = 0.0
    if (-not [double]::TryParse([string]$row.$name, [Globalization.NumberStyles]::Float, [Globalization.CultureInfo]::InvariantCulture, [ref]$value)) {
        throw "Non-numeric score for $name in project $($row.project_id): '$($row.$name)'"
    }
    if ($value -lt 0 -or $value -gt 10) {
        throw "Out-of-range score for $name in project $($row.project_id): $value"
    }
    return $value
}

$scored = foreach ($row in $rows) {
    $weighted = 0.0
    foreach ($entry in $positiveWeights.GetEnumerator()) {
        $weighted += (Get-Score $row $entry.Key) * $entry.Value
    }
    foreach ($entry in $riskWeights.GetEnumerator()) {
        $weighted += (10.0 - (Get-Score $row $entry.Key)) * $entry.Value
    }

    $behavior = Get-Score $row 'existing_behavioral_robustness'
    $repro = Get-Score $row 'reproducibility_evidence'
    $natural = Get-Score $row 'naturalness_deployment_relevance'
    $safety = Get-Score $row 'safety_relevance'
    $surprise = Get-Score $row 'scientific_surprise'
    $competing = Get-Score $row 'competing_explanations_quality'
    $mech = Get-Score $row 'mechanistic_discriminability'
    $intervention = Get-Score $row 'intervention_usefulness'
    $open = Get-Score $row 'open_weight_availability'
    $local = Get-Score $row 'local_12gb_feasibility'
    $code = Get-Score $row 'code_availability'
    $data = Get-Score $row 'dataset_cached_output_availability'
    $first = Get-Score $row 'time_to_first_result'
    $fit = Get-Score $row 'total_project_effort_fit'
    $novelty = Get-Score $row 'novelty_gap_plausibility'
    $artifact = Get-Score $row 'coherent_artifact_probability'
    $falsified = Get-Score $row 'value_if_hypothesis_falsified'

    $row | Add-Member -NotePropertyName score_balanced -NotePropertyValue ([math]::Round($weighted / 10.0, 3)) -Force
    $row | Add-Member -NotePropertyName score_safety_view -NotePropertyValue ([math]::Round((3*$safety + 1.5*$natural + $behavior + $intervention + $local + $artifact) / 8.5, 3)) -Force
    $row | Add-Member -NotePropertyName score_mechanism_probability -NotePropertyValue ([math]::Round((1.5*$behavior + 1.25*$repro + 1.75*$mech + 1.25*$local + $first + 0.75*$code + 0.75*$data + 1.5*$artifact) / 9.75, 3)) -Force
    $row | Add-Member -NotePropertyName score_novelty_upside -NotePropertyValue ([math]::Round((2*$novelty + $surprise + $competing + 1.5*$mech + $safety + 0.5*$behavior) / 8.0, 3)) -Force
    $row | Add-Member -NotePropertyName score_forensics_view -NotePropertyValue ([math]::Round(($behavior + $repro + 1.25*$natural + $surprise + 1.5*$competing + 1.5*$mech + $safety + $first + $artifact + $falsified) / 11.25, 3)) -Force
    $row
}

$scored |
    Sort-Object -Property @{Expression='score_balanced'; Descending=$true}, @{Expression='project_id'; Descending=$false} |
    Export-Csv -LiteralPath $OutputCsv -NoTypeInformation -Encoding utf8

Write-Output "Scored $($scored.Count) candidates -> $OutputCsv"
