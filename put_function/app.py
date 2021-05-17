import json
import boto3
dynamodb = boto3.resource('dynamodb')
table_name = 'cloud-resume'
table = dynamodb.Table(table_name)
ID = '0'



def lambda_handler(event, context):
    print('Fetching item id = {} from the dB\n'.format(ID))
 
    response = table.get_item(
        Key={
            'ID': ID
        }
        )
    if 'Item' in response:
        response = table.update_item(
             Key={
                'ID': ID
            },
            UpdateExpression="set total_count = total_count + :N",
            ExpressionAttributeValues={
                ':N': 1
            }
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print('Item updated with status code = {} OK'.format(response['ResponseMetadata']['HTTPStatusCode']))
        else:
            print('Some error occurred while updating the item from the dB')
    else:
        print('Item id = {} not found in the dB'.format(ID))

    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        }
    }