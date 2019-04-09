import boto3
import json
import logging.config


CLIENT = boto3.client('stepfunctions')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
	logger.info('Processing event :{}'.format(json.dumps(event)))
	if isinstance(event, dict):
		logger.info('Processing Invoke operation')
		return _operation(event)
	elif isinstance(event, (list, tuple)):
		logger.debug('Processing BatchInvoke operation with a batch of {}'.format(len(event)))
		return list(map(_operation, event))
	else:
		raise ValueError('Event type {} is not supported'.format(type(event)))

def _operation(event):
    if event['operation'] == 'getExecution':
        return _describe_execution(event['arguments']['executionArn'])
    elif event['operation'] == 'stopExecution':
        CLIENT.stop_execution(
            executionArn=event['arguments']['executionArn'],
            error=event['arguments'].get('error', ''),
            cause=event['arguments'].get('cause', '')
        )
        return _describe_execution(event['arguments']['executionArn'])
    else:
        raise ValueError('operation {} not supported'.format(event['operation']))

def _describe_execution(executionArn):
    response = CLIENT.describe_execution(
        executionArn=executionArn
    )
    response['startDate'] = response['startDate'].isoformat()
    response['stopDate'] = response['stopDate'].isoformat()
    return response