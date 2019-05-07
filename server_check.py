import logging
import boto3
from boto3.session import Session

print('Loading function... ')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
