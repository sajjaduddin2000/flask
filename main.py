import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Azure!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use PORT from Azure or default to 8000
    uvicorn.run(app, host="0.0.0.0", port=port)
