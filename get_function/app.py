import simplejson as json
import boto3
dynamodb = boto3.resource('dynamodb')
table_name = 'cloud-resume'
table = dynamodb.Table(table_name)
ID = '0'

# import requests


def lambda_handler(event, context):
    print('Fetching item id = {} from the dB\n'.format(ID))
    
    response = table.get_item(
        Key={
            'ID': ID
        }
    )
        
    if 'Item' in response:
        return {
            "statusCode": 200,
            'headers': {
                        'Access-Control-Allow-Headers': '*',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'GET'
            },
            "body": json.dumps({
                        "counter": response['Item'].get('total_count'),
            }),
        }
    else:
            print('Item id = {} not found in the dB'.format(id))