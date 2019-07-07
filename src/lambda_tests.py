
import boto3
import json

def get_client() -> boto3.Session:
    return boto3.client("lambda")
    
    

def external_lambda_tests() -> None:
    basic_call()
    

def basic_call() -> None:
    lambda_client = get_client()

    response = lambda_client.list_functions(
        MaxItems=10
    )
    
    pretty_print(response)

def pretty_print(response: str) -> None:
    print(json.dumps(response, indent=4, sort_keys=True))

if __name__ == "__main__":
    external_lambda_tests()
