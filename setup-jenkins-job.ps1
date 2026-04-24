# Wait for Jenkins to be ready
Write-Host "Waiting for Jenkins to be ready..."
Start-Sleep -Seconds 30

# Create Jenkins job using Jenkins CLI
$content = Get-Content Jenkinsfile -Raw
$jobContent = $content -replace "`n", "&#10;"
$jobContent = $jobContent -replace "`r", "&#13;"

# Create the Jenkins job
$jobContent | & "java" -jar jenkins-cli.jar -s http://localhost:8080/ create-job elk-post-pipeline

Write-Host "Jenkins job created successfully!"
Write-Host "Access Jenkins at: http://localhost:8080"