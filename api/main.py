from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import pandas as pd
import numpy as np

app = FastAPI(
    title="Data Pipeline API",
    description="API for data pipeline operations",
    version="1.0.0"
)

class DataRequest(BaseModel):
    data_source: str
    parameters: Optional[dict] = None

class DataResponse(BaseModel):
    status: str
    message: str
    data_preview: Optional[dict] = None

@app.get("/")
async def root():
    return {"message": "Data Pipeline API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/process", response_model=DataResponse)
async def process_data(request: DataRequest):
    """Process data from a source."""
    try:
        # Example: Load and process data
        if request.data_source == "test":
            # Create sample data
            data = pd.DataFrame({
                'id': range(10),
                'value': np.random.randn(10)
            })
            
            # Process data (example transformation)
            data['processed'] = data['value'] * 2
            
            return DataResponse(
                status="success",
                message=f"Processed data from {request.data_source}",
                data_preview=data.head().to_dict()
            )
        else:
            raise HTTPException(status_code=400, detail="Unknown data source")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
