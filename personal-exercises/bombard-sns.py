import boto3
import traceback
import sys
import time

start = time.time()
sns = boto3.client('sns')
success = 0

for i in range(1000):
    try:
        response = sns.publish(
            TopicArn='arn:aws:sns:us-east-2:711589413744:tasq-celery-sqs-test-dev-CeleryWorkerTopic-N7BVPQ7NICMH', 
            Message='Hello World {} !'.format(i))
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            print(response)
        else:
            success += 1
    except Exception as e:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)
        del exc_info
end = time.time()
print('Successfully pushed {} messages in {} seconds'.format(success, (end - start)))
