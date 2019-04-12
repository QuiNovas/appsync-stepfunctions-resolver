==============================
appsync-stepfunctions-resolver
==============================

.. _APL2: http://www.apache.org/licenses/LICENSE-2.0.txt

An AWS AppSync resolver that interacts with and
returns data about AWS StepFunctions

AWS Permissions Required
------------------------
- sfn:DescribeExecution
- sfn:StopExecution

Handler Method
--------------
.. code::

  function.handler

Request Syntax
--------------
.. code::


  {
    "operation": "getExecution",
    "arguments": {
      "executionArn": "arn"
    }
  }

  {
    "operation": "stopExecution",
    "arguments": {
      "executionArn": "arn",
      "error": "string"
      "cause": "string"
    }
  }

**operation** - REQUIRED
  Can be one of ``getExecution`` or ``stopExecution``.

**getExecution**
  :executionArn: The Amazon Resource Name (ARN) of the execution to describe - REQUIRED

**stopExecution**
  :executionArn: The Amazon Resource Name (ARN) of the execution to stop - REQUIRED
  :error: The error code of the failure
  :cause: A more detailed explanation of the cause of the failure

Each of these requests can be batched via the `BatchInvoke` protocol
from Appsync.

Response syntax
---------------
For ``getExecution`` and ``stopExecution``:

.. code::

  {
    'executionArn': 'string',
    'stateMachineArn': 'string',
    'name': 'string',
    'status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'ABORTED',
    'startDate': datetime(2015, 1, 1),
    'stopDate': datetime(2015, 1, 1),
    'input': 'string',
    'output': 'string'
}

Example AWS Appsync schema:
---------------------------

.. code::

pass

Lambda Package Location
-----------------------
pass

License: `APL2`_