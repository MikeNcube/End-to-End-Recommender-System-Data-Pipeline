# My Agentic Tool - Cloud Data Engineering Pipeline

A comprehensive data engineering pipeline for document and data automation.

## Project Structure

\\\
my-agentic-tool/
├── src/                    # Source code
│   ├── main.py            # Main pipeline script
│   └── pipeline_dag.py    # Airflow DAG definition
├── tests/                 # Test files
├── data/                  # Data files
├── config/                # Configuration files
├── docs/                  # Documentation
├── scripts/               # Utility scripts
├── airflow/               # Airflow configuration
├── requirements.txt       # Python dependencies
├── great_expectations.yml # Data quality checks
├── main.tf               # Terraform infrastructure
├── .env                  # Environment variables (create from .env.example)
├── test_main.py          # Local test script (no AWS required)
└── README.md             # This file
\\\

## Setup

1. **Clone or navigate to the project:**
   \\\ash
   cd my-agentic-tool
   \\\

2. **Set up Python environment (recommended):**
   \\\ash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   
   pip install -r requirements.txt
   \\\

3. **Configure environment:**
   \\\ash
   # Copy the example environment file
   cp .env.example .env
   # Edit .env with your configuration
   \\\

4. **Test the setup:**
   \\\ash
   python test_main.py
   \\\

## Features

- **Data Pipeline Automation**: Automated ETL/ELT workflows
- **Data Quality**: Great Expectations for validation
- **Workflow Orchestration**: Apache Airflow DAGs
- **Cloud Integration**: AWS services (Kinesis, S3, etc.)
- **Infrastructure as Code**: Terraform configuration
- **Local Testing**: Mock services for development without AWS

## Usage

### Local Development (No AWS Required)
\\\ash
python test_main.py
\\\

### Production Mode (Requires AWS Credentials)
\\\ash
python src/main.py
\\\

### Running Airflow DAGs
\\\ash
# If Airflow is set up
airflow dags list
airflow tasks list my_pipeline_dag
\\\

## Configuration

### AWS Credentials
Create a \.env\ file with:
\\\ash
# For development without AWS:
USE_MOCK_SERVICES=true

# For production with AWS (uncomment and fill):
# AWS_ACCESS_KEY_ID=your_access_key
# AWS_SECRET_ACCESS_KEY=your_secret_key
# AWS_DEFAULT_REGION=us-east-1
\\\

### Environment Variables
- \USE_MOCK_SERVICES\: Set to 'true' to use mock services
- \LOG_LEVEL\: Logging level (DEBUG, INFO, WARNING, ERROR)
- \DATA_SOURCE_PATH\: Path to local data files

## Development

### Adding New Features
1. Add Python code to \src/\ directory
2. Update tests in \	ests/\ directory
3. Update requirements.txt if new dependencies are needed
4. Update documentation in \docs/\ and README.md

### Testing
\\\ash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_pipeline.py

# Run with coverage
pytest --cov=src tests/
\\\

## Troubleshooting

### Common Issues

1. **AWS Credentials Error**:
   - Ensure AWS credentials are configured in \.env\ file
   - Or set \USE_MOCK_SERVICES=true\ for local development

2. **Import Errors**:
   - Activate virtual environment: \env\Scripts\activate\
   - Install dependencies: \pip install -r requirements.txt\

3. **Airflow Issues**:
   - Check Airflow is installed: \irflow version\
   - Initialize Airflow database: \irflow db init\

## License

MIT License

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Review the documentation in \docs/\ directory
3. Create an issue in the project repository
