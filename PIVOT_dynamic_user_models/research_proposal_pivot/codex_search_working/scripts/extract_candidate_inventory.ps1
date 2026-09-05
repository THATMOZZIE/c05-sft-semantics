param(
    [string]$WorkingDirectory = (Join-Path $PSScriptRoot '..'),
    [string]$OutputCsv = (Join-Path $PSScriptRoot '..\candidate_inventory.csv')
)

$ErrorActionPreference = 'Stop'

$laneFiles = Get-ChildItem -LiteralPath $WorkingDirectory -File |
    Where-Object { $_.Name -match '^0[1-6]_.+\.md$' } |
    Sort-Object Name

if ($laneFiles.Count -eq 0) {
    throw "No lane files found in $WorkingDirectory"
}

$rows = foreach ($file in $laneFiles) {
    $text = Get-Content -LiteralPath $file.FullName -Raw
    $records = [System.Collections.Generic.List[object]]::new()

    # Markdown field form, including optional evidence labels and backticks.
    $fieldMatches = [regex]::Matches(
        $text,
        '(?im)^\s*(?:-\s*)?\*\*candidate_id:\*\*\s*(?:(?:\*\*)?\[[^\]]+\](?:\*\*)?\s*)?`?([^`\r\n]+)`?\s*$'
    )
    foreach ($match in $fieldMatches) {
        $records.Add([pscustomobject]@{ Id = $match.Groups[1].Value.Trim(); Start = $match.Index; HeadingTitle = '' })
    }

    # Fenced plain-text schema form: candidate_id on one line, value on next.
    $plainMatches = [regex]::Matches($text, '(?im)^candidate_id\s*\r?\n\s*([^\r\n]+)\s*$')
    foreach ($match in $plainMatches) {
        $records.Add([pscustomobject]@{ Id = $match.Groups[1].Value.Trim(); Start = $match.Index; HeadingTitle = '' })
    }

    # WeirdChat uses compact candidate headings rather than repeated schema fields.
    $headingMatches = [regex]::Matches($text, '(?im)^###\s+(WC-[A-Z]\d{2})\s+[—-]\s+([^\r\n]+)$')
    foreach ($match in $headingMatches) {
        $records.Add([pscustomobject]@{ Id = $match.Groups[1].Value.Trim(); Start = $match.Index; HeadingTitle = $match.Groups[2].Value.Trim() })
    }

    $ordered = @($records | Sort-Object Start)
    for ($i = 0; $i -lt $ordered.Count; $i++) {
        $record = $ordered[$i]
        $end = if ($i + 1 -lt $ordered.Count) { $ordered[$i + 1].Start } else { $text.Length }
        $block = $text.Substring($record.Start, $end - $record.Start)
        $titleMatch = [regex]::Match(
            $block,
            '(?im)^\s*(?:-\s*)?\*\*title:\*\*\s*(?:(?:\*\*)?\[[^\]]+\](?:\*\*)?\s*)?`?([^`\r\n]+)`?\s*$|^title\s*\r?\n\s*([^\r\n]+)\s*$'
        )
        $title = if ($record.HeadingTitle) {
            $record.HeadingTitle
        } elseif (-not $titleMatch.Success) {
            ''
        } elseif ($titleMatch.Groups[1].Success) {
            $titleMatch.Groups[1].Value.Trim()
        } else {
            $titleMatch.Groups[2].Value.Trim()
        }

        [pscustomobject]@{
            candidate_id = $record.Id
            title = $title
            lane_file = $file.Name
            source_path = $file.FullName
        }
    }
}

$duplicateIds = $rows | Group-Object candidate_id | Where-Object Count -gt 1
if ($duplicateIds) {
    $summary = ($duplicateIds | ForEach-Object Name) -join ', '
    throw "Duplicate candidate IDs across lane files: $summary"
}

$rows | Export-Csv -LiteralPath $OutputCsv -NoTypeInformation -Encoding utf8
Write-Output "Extracted $($rows.Count) candidate records from $($laneFiles.Count) lane files -> $OutputCsv"
