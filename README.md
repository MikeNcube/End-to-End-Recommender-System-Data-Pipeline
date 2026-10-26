# Cloud Data Engineering Pipeline

A Python data engineering pipeline that supports both **local development** (no cloud credentials needed) and **production** execution against AWS services. It ships a FastAPI status/trigger endpoint, Apache Airflow DAGs for orchestration, Great Expectations for data quality, and Terraform for infrastructure provisioning.

## What the pipeline does

| Layer | Component | File(s) |
|-------|-----------|---------|
| Ingestion | Sends records to an AWS Kinesis stream | `src/main.py` |
| Batch ETL | Placeholder batch transform | `scripts/batch_etl.py` |
| Streaming ETL | Placeholder streaming transform | `scripts/streaming_etl.py` |
| Orchestration | Airflow DAGs: daily `data_pipeline` + `example_pipeline` | `dags/data_pipeline.py`, `src/pipeline_dag.py` |
| REST API | FastAPI app with `/health` and `/process` endpoints | `api/main.py` |
| Data quality | Great Expectations suite definition | `great_expectations.yml` |
| Infrastructure | Terraform config (e.g. Kinesis stream) | `main.tf` |
| Configuration | Central YAML config (paths, batch size, Airflow defaults) | `config/config.yaml` |

The `USE_MOCK_SERVICES=true` flag (default in `.env.example`) lets you run and test the pipeline locally without any AWS credentials.

## Project structure

```
.
├── api/                    # FastAPI application
│   └── main.py
├── config/
│   └── config.yaml         # Central configuration
├── dags/
│   └── data_pipeline.py    # Daily Airflow DAG
├── scripts/
│   ├── batch_etl.py        # Batch ETL entry point
│   └── streaming_etl.py    # Streaming ETL entry point
├── src/
│   ├── main.py             # Kinesis ingestion (production)
│   └── pipeline_dag.py     # Minimal example Airflow DAG
├── sql/
│   └── ratings_table_ddl.sql
├── airflow/
│   └── docker-compose.yaml # Run Airflow via Docker Compose
├── notebooks/
│   └── analysis.ipynb
├── great_expectations.yml
├── main.tf                 # Terraform infrastructure
├── requirements.txt        # Pinned Python dependencies
├── .env.example            # Template — copy to .env and edit
├── test_main.py            # Local smoke test (no AWS required)
└── test_setup.py           # Environment validation tests
```

## Prerequisites

- Python 3.11+
- (Optional) Docker + Docker Compose — for running Airflow locally
- (Optional) AWS CLI configured — for production mode
- (Optional) Terraform — for infrastructure provisioning

## Quick start

### 1. Clone and set up Python environment

```bash
git clone <repo-url>
cd <repo-directory>
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment variables

```bash
cp .env.example .env
# Open .env and review the defaults.
# For local testing the defaults work as-is (USE_MOCK_SERVICES=true).
# For production, set AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, etc.
```

### 3. Run the local smoke test (no AWS needed)

```bash
python test_main.py
```

Expected output: each ETL step printed with a success status.

### 4. Start the FastAPI service

```bash
uvicorn api.main:app --reload
# API docs available at http://localhost:8000/docs
```

Key endpoints:

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Root health check |
| GET | `/health` | Service health status |
| POST | `/process` | Trigger a data processing run |

### 5. Run Airflow via Docker Compose

```bash
docker compose -f airflow/docker-compose.yaml up
# Airflow UI: http://localhost:8080  (user: airflow / password: airflow)
```

The `data_pipeline` DAG runs daily and executes: `start_pipeline → process_data → end_pipeline`.

### 6. Run Airflow directly (without Docker)

```bash
export AIRFLOW_HOME=./airflow
airflow db migrate
airflow webserver &
airflow scheduler &
```

## Environment variables

See `.env.example` for all supported variables. Key ones:

| Variable | Default | Description |
|----------|---------|-------------|
| `USE_MOCK_SERVICES` | `true` | Skip AWS calls; use local stubs |
| `AWS_ACCESS_KEY_ID` | — | AWS access key (production only) |
| `AWS_SECRET_ACCESS_KEY` | — | AWS secret key (production only) |
| `AWS_DEFAULT_REGION` | `us-east-1` | Target AWS region |
| `KINESIS_STREAM_NAME` | `example-stream` | Stream for ingestion records |
| `S3_BUCKET_NAME` | — | S3 bucket for pipeline data |
| `LOG_LEVEL` | `INFO` | Python logging level |
| `BATCH_SIZE` | `1000` | Records per batch |
| `MAX_RETRIES` | `3` | Retry attempts on transient errors |

## Running tests

```bash
# Validate environment setup
python test_setup.py

# Smoke test (no AWS)
python test_main.py

# Full pytest suite
pytest
```

## Infrastructure (Terraform)

```bash
cd /path/to/repo
terraform init
terraform plan
terraform apply
```

`main.tf` provisions the AWS resources the pipeline depends on (e.g. the Kinesis stream named in `KINESIS_STREAM_NAME`).

## Data quality

Great Expectations configuration is stored in `great_expectations.yml`. Validation results are written to `great_expectations/uncommitted/validations/` (excluded from version control).

## Troubleshooting

**Import errors after cloning**
Activate the virtual environment and reinstall: `pip install -r requirements.txt`.

**Airflow scheduler not picking up DAGs**
Ensure `AIRFLOW_HOME` points to the `airflow/` directory and that `dags/` is on the `dags_folder` path in `airflow.cfg`.

**AWS credential errors in production mode**
Set `USE_MOCK_SERVICES=false` in `.env` and provide valid `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`, or configure credentials via `~/.aws/credentials` or an IAM role.

## License

MIT
