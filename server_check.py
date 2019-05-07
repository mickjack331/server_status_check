import logging
import boto3
from boto3.session import Session

print('Loading function... ')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# set your access key here, don't use my key!!
AWS_ACCESS_KEY = 'AKIAJTS52TFCQHJFOI3A'
# set your secret access key here, don't use my key!!
AWS_ACCESS_SECRET = '9Z/jzL0J+haty7f2hwrkK0BDmw06wq/EcnNgscEk'

# option
AWS_REGION = 'ap-northeast-1'
EC2_TARGET_NAME_TAG = 'CheckInstanceStatus'

def handler(event, context):
