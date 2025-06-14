import pytest
import boto3
from moto import mock_s3
from src import lambda_function

@mock_s3
def test_csv_transformation():
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="input-bucket")
    s3.create_bucket(Bucket="output-bucket")

    csv_data = "name,age\njohn,30\njane,25"
    s3.put_object(Bucket="input-bucket", Key="test.csv", Body=csv_data)

    event = {
        "Records": [{
            "s3": {
                "bucket": {"name": "input-bucket"},
                "object": {"key": "test.csv"}
            }
        }]
    }

    lambda_function.OUTPUT_BUCKET = "output-bucket"
    lambda_function.SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:123456789012:test"
    lambda_function.s3 = s3

    response = lambda_function.lambda_handler(event, None)
    assert response["status"] == "success"
