import boto3
import csv
import os
import traceback
from io import StringIO

s3 = boto3.client('s3')
sns = boto3.client('sns')

OUTPUT_BUCKET = os.environ.get("OUTPUT_BUCKET")
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")

def lambda_handler(event, context):
    try:
        # Get object info
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        response = s3.get_object(Bucket=bucket, Key=key)
        csv_content = response['Body'].read().decode('utf-8')

        # Transform CSV
        output = StringIO()
        writer = csv.writer(output)
        reader = csv.reader(StringIO(csv_content))

        for row in reader:
            transformed = [item.upper() for item in row]
            writer.writerow(transformed)

        # Save to output bucket
        output.seek(0)
        s3.put_object(Bucket=OUTPUT_BUCKET, Key=f"processed/{key}", Body=output.getvalue())
        return {"status": "success"}

    except Exception as e:
        error_message = f"CSV Processing Failed: {str(e)}\n{traceback.format_exc()}"
        sns.publish(TopicArn=SNS_TOPIC_ARN, Message=error_message, Subject="CSV Processing Failed")
        raise e
