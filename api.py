from fastapi import FastAPI, Request
import uvicorn

import boto3
import os
from dotenv import load_dotenv
load_dotenv()

localhost= os.getenv('localhost')
user = os.getenv('user')
password= os.getenv('password')


s3 = boto3.resource(
    's3',
    endpoint_url = f'{localhost}:9000',
    aws_access_key_id=user,
    aws_secret_access_key=password,
)

app = FastAPI()

@app.post("/")
async def upload(file : UploadFile | None = None):
    
    
    list = s3.list_objects(Bucket='mem')['Contents']
    for key in list:
        await s3.download_file('mem', key['Key'], key['Key'])


if __name__ == "__main__":
    uvicorn.run("api:app", port=8000, host="0.0.0.0", reload=True)