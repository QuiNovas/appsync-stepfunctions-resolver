==============================
appsync-stepfunctions-resolver
==============================

.. _APL2: http://www.apache.org/licenses/LICENSE-2.0.txt

An AWS AppSync resolver that interacts with and
returns data about AWS StepFunctions

AWS Permissions Required
------------------------
- states:DescribeExecution
- states:StopExecution

Handler Method
--------------
.. code::

  function.handler

Request Syntax
--------------
.. code::


  {
    "operation": "describeExecution",
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
  Can be one of ``describeExecution`` or ``stopExecution``.

**describeExecution**
  :executionArn: The Amazon Resource Name (ARN) of the execution to describe - REQUIRED

**stopExecution**
  :executionArn: The Amazon Resource Name (ARN) of the execution to stop - REQUIRED
  :error: The error code of the failure
  :cause: A more detailed explanation of the cause of the failure

Each of these requests can be batched via the `BatchInvoke` protocol
from Appsync.

Response syntax
---------------
For ``describeExecution`` and ``stopExecution``:

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

  type Execution {
    executionArn: String!
    stateMachineArn: String!
    name: String!
    status: String!
    startDate: AWSDateTime!
    stopDate: AWSDateTime!
    input: String!
    output: String
  }

  type Mutation {
    stopExecution(executionArn: String!, error: String, cause: String): Execution
  }

  type Query {
    describeExecution(executionArn: String!): Execution
  }

  schema {
    query: Query
    mutation: Mutation
  }

Lambda Package Location
-----------------------
https://s3.amazonaws.com/lambdalambdalambda-repo/quinovas/appsync-stepfunctions-resolver/appsync-stepfunctions-resolver-0.0.1.zip

License: `APL2`_