import json

def lambda_handler(event, context):
    first_name = event['first_name']
    last_name = event['last_name']
    message = f'hello from {first_name} {last_name}'
    return message, {
        'statusCode': 200,
        'first name': first_name,
        'last name' : last_name
    }
