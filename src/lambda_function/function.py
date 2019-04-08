import boto3
import json
import logging.config


CLIENT = boto3.client('stepfunctions')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    return event
