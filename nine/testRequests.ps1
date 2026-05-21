$port = $env:PORT
if (-not $port) { $port = '3002' }
$base = "http://localhost:$port"

Write-Output "Using server base: $base"

function Send-Json($method, $path, $body) {
  try {
    if ($body) {
      $resp = Invoke-RestMethod -Method $method -Uri ($base + $path) -ContentType 'application/json' -Body ($body | ConvertTo-Json -Depth 5) -ErrorAction Stop
    } else {
      $resp = Invoke-RestMethod -Method $method -Uri ($base + $path) -ErrorAction Stop
    }
    return ($resp | ConvertTo-Json -Depth 10)
  } catch {
    $webResp = $_.Exception.Response
    if ($webResp -ne $null) {
      $sr = New-Object System.IO.StreamReader($webResp.GetResponseStream())
      return $sr.ReadToEnd()
    } else {
      return $_.Exception.Message
    }
  }
}

Write-Output "`nINVALID:"
Write-Output (Send-Json 'Post' '/api/users' @{ email = 'bad' })

Write-Output "`nCREATE:"
Write-Output (Send-Json 'Post' '/api/users' @{ name = 'Jane Doe'; email = 'jane@example.com' })

Write-Output "`nCREATE Duplicate (expected 409):"
Write-Output (Send-Json 'Post' '/api/users' @{ name = 'Jane Doe'; email = 'jane@example.com' })

Write-Output "`nMISSING (expected 404):"
Write-Output (Send-Json 'Get' '/api/users/999' $null)
