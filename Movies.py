import boto3
import pandas as pd

from io import StringIO

client = boto3.client('s3')

csv_obj = client.get_object(Bucket='movies123', Key='movies.csv')

#print(csv_obj['Body'])

csv_obj_body = csv_obj['Body']

csv_string = csv_obj_body.read().decode('utf-8')

df = pd.read_csv(StringIO(csv_string))

df_comedy  = df[df.Genre=='Drama']

# Write the filtered data into S3

csv_buf = StringIO()
df_comedy.to_csv(csv_buf, header=True, index=False)
csv_buf.seek(0)
client.put_object(Bucket='movies123', Body=csv_buf.getvalue(), Key='movies-drama123.csv')