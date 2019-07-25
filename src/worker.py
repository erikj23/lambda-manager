
import boto3
import json

def lambda_handler(event, context):
    
    # create channel for communication
    sns_client = boto3.client("sns")
    
    
   # invoke worker if needed to persist
    lambda_client = boto3.client("lambda")
    
    # main event loop
    while True:
        
        # if remaining execution time is greater than 1 second do work
        if context.get_remaining_time_in_millis() > 1000:
            pass

        # else prepare to persist
        else:
            sns_client.delete_topic(TopicArn=response.get("TopicArn"))
            return {
                "statusCode": 202,
                "body": {
                    "state": "persisted"
                }
            }
    
    return {
        "statusCode": 200,
        "body": {
            "state": "absent"
        }
    }
