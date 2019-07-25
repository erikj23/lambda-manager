
import boto3
import json

def lambda_handler(event, context):
    
    # create channel for communication
    sns_client = boto3.client("sns")
    
    # create topic to subscribe to
    name = "{}{}".format("channel_id_", context.aws_request_id)
    response = sns_client.create_topic(
        Name=name,
    )
    
    # subscripe to topic created
    topic_arn = response.get("TopicArn")
    response = sns_client.subscribe(
        TopicArn=response,
        Protocol='string',
        Endpoint='string',
        Attributes={
            'string': 'string'
        },
        ReturnSubscriptionArn=True|False
    )
    
   # invoke worker and give topic arn
    lambda_client = boto3.client("lambda")
    response = lambda_client.invoke(
        FunctionName='The-Eternal-Workload',
        Payload=json.dump({
            "TopicArn":response
        }),        
    )
    
    # main event loop
    while True:
        
        # if remaining execution time is greater than 1 second do work
        if context.get_remaining_time_in_millis() > 1000:
            pass

        # else prepare to persist
        else:
            sns_client.delete_topic(topic_arn)
            return {
                "statusCode": 202,
                "body": {
                    "state": "persisted"
                }
            }
            
    event_context = {
        "event": event, 
        "context": get_lambda_context(context)
    }
    
    print(event_context)

    return {
        "statusCode": 200,
        "body": {
            "state": "absent"
        }
    }

def get_lambda_context(context: dict) -> dict:
    
    # ! only part of the context
    return {
        "remaining_time_in_millis": context.get_remaining_time_in_millis(),
        "function_name": context.function_name,
        "invoked_function_arn": context.invoked_function_arn,
        "memory_limit_in_mb": context.memory_limit_in_mb,
        "aws_request_id": context.aws_request_id,
        "log_group_name": context.log_group_name,
        "log_stream_name": context.log_stream_name,
    }
    