# PowerShell startup script for Data Pipeline

Write-Host "=== Data Pipeline Project Startup ===" -ForegroundColor Cyan

# Check virtual environment
if (Test-Path "venv") {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    .\venv\Scripts\Activate.ps1
} else {
    Write-Host "Virtual environment not found." -ForegroundColor Red
    Write-Host "Create one with: python -m venv venv" -ForegroundColor Yellow
    exit 1
}

# Set Airflow home
$env:AIRFLOW_HOME = "$PWD\airflow"

# Parse command
param(
    [Parameter(Mandatory=$false)]
    [ValidateSet("airflow", "api", "test")]
    [string]$Command = "airflow"
)

switch ($Command) {
    "airflow" {
        Write-Host "Starting Airflow..." -ForegroundColor Green
        # Start Airflow webserver
        Start-Process -NoNewWindow -FilePath "airflow" -ArgumentList "webserver --port 8080"
        # Start scheduler
        airflow scheduler
    }
    "api" {
        Write-Host "Starting FastAPI..." -ForegroundColor Green
        cd api
        uvicorn main:app --reload --host 0.0.0.0 --port 8000
    }
    "test" {
        Write-Host "Running tests..." -ForegroundColor Green
        pytest tests/ -v
    }
}
