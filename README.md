# CSV Data Transformation Pipeline on AWS

This project implements a **serverless pipeline** using AWS services to process CSV files uploaded to an S3 bucket. The pipeline performs data transformations on the CSV and stores the transformed result in another S3 bucket. Failures are notified via email using Amazon SNS.

---

## 🚀 Project Architecture

**Services Used:**

- **AWS S3**  
  - `InputBucket`: Accepts raw CSV uploads.  
  - `OutputBucket`: Stores transformed CSV files.

- **AWS Lambda**  
  - Processes CSV files, performs transformation, and writes output.  
  - Sends failure notifications to an admin via SNS.

- **Amazon SNS**  
  - Topic to send failure alerts via email.

---

## ⚙️ Features

- Fully serverless and event-driven
- Infrastructure as Code using AWS SAM
- Handles transformation logic and error reporting
- Modular and testable Python code
- Environment variables for configuration

---

## 🏗️ Infrastructure Details

| Resource             | Purpose                                                  |
|----------------------|----------------------------------------------------------|
| `InputBucket`        | S3 bucket to receive original CSV files                  |
| `OutputBucket`       | S3 bucket to store transformed CSV files                 |
| `CSVProcessorFunction`| AWS Lambda function that processes and transforms data |
| `NotifyTopic`        | SNS topic to send email notifications                    |
| `AdminSubscription`  | Email subscription to receive failure alerts             |

---

## 🔄 How It Works

1. **Upload**: A user uploads a `.csv` file to `InputBucket`.
2. **Trigger**: The upload triggers the `CSVProcessorFunction` Lambda.
3. **Transform**: Lambda reads the file, transforms it (e.g., filters columns, changes case).
4. **Store**: Writes the transformed CSV to `OutputBucket`.
5. **Notify**: If transformation fails, Lambda publishes an alert to `NotifyTopic` (email).

---

## 🧪 Prerequisites

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- Python 3.13 installed
- AWS credentials configured (`aws configure`)

---

## 🚀 Deployment Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/anubhav-ojha/csv-data-transformation.git
   cd csv-data-transforamtion

2. **Update Email in Template**  
   Open the `template.yaml` file and replace the placeholder email with your actual admin email address:

   ```yaml
   Endpoint: your-admin-email@example.com   

