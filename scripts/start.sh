#!/bin/bash
# Startup script for the data pipeline project

echo "=== Data Pipeline Project Startup ==="

# Activate virtual environment
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate  # Linux/Mac
    # venv\Scripts\activate  # Windows
else
    echo "Virtual environment not found. Please create one with: python -m venv venv"
    exit 1
fi

# Check dependencies
echo "Checking dependencies..."
pip install -r requirements.txt

# Set environment variables
export AIRFLOW_HOME=$(pwd)/airflow

# Initialize Airflow if needed
if [ ! -d "airflow" ]; then
    echo "Initializing Airflow..."
    airflow db init
fi

# Start services based on argument
case "$1" in
    "airflow")
        echo "Starting Airflow..."
        # Start Airflow webserver in background
        airflow webserver --port 8080 &
        # Start Airflow scheduler
        airflow scheduler
        ;;
    "api")
        echo "Starting FastAPI..."
        cd api
        uvicorn main:app --reload --host 0.0.0.0 --port 8000
        ;;
    "test")
        echo "Running tests..."
        pytest tests/ -v
        ;;
    *)
        echo "Usage: $0 {airflow|api|test}"
        echo "  airflow - Start Airflow webserver and scheduler"
        echo "  api     - Start FastAPI server"
        echo "  test    - Run tests"
        exit 1
        ;;
esac
