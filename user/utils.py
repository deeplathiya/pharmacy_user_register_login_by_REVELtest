import boto3
import os
from dotenv import load_dotenv

load_dotenv()

Access_key = os.environ.get("Access_key")
Secret_key = os.environ.get("Secret_key")
region = os.environ.get("region")
bucket = os.environ.get("bucket")
folder = os.environ.get("folder")


def upload_file_s3():
    session = boto3.session.Session(aws_access_key_id=Access_key,
                                    aws_secret_access_key=Secret_key,
                                    region_name=region)

    s3 = session.client("s3")
    result = s3.upload_file("./a.txt", bucket, folder + "/a.txt")
    print(result)
