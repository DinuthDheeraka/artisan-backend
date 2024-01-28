import boto3
from botocore.exceptions import NoCredentialsError
from fastapi import HTTPException

from app.util.environment import get_environment

s3 = boto3.client('s3', aws_access_key_id=get_environment("AWS_ACCESS_KEY"),
                  aws_secret_access_key=get_environment("AWS_SECRET_KEY"))

s3_uri = get_environment("S3_URI")


def upload_to_s3(file_name, file):
    try:
        s3.put_object(Body=file.read(), Bucket=get_environment("S3_BUCKET"), Key=file_name)
        return f"{s3_uri}{file_name}"
    except NoCredentialsError:
        raise HTTPException(status_code=500, detail="AWS credentials not available")
