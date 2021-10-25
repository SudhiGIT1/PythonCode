# Accessing AWS Bucket from Python
import boto3
import pandas

# get boto3 client
client = boto3.client(
    's3'
)

# Fetch the list of existing buckets
clientResponse = client.list_buckets()

#print(clientResponse)

#print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')

#print object name from the bucket
csv_obj = client.get_object(Bucket='test-10232021-first', Key='movies.csv')

