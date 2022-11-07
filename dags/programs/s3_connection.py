import time
import boto3
import pandas as pd
import requests

import os

def transform():
 
    
    
    s3_bucket = os.getenv('S3_BUCKET')
    
    path_read = 's3a://'+s3_bucket+'/input/input.csv' 
    path_write = 's3a://'+s3_bucket+'/output/output.csv'
    print('path to read: ' +  path_read)
    print('path to write: ' +  path_write)

    url = os.getenv('AWS_CONTAINER_CREDENTIALS_RELATIVE_URI')
    print('reading credentials from: ' +url)

    r = requests.get('http://169.254.170.2'+url)
    creds = r.json()
    print (creds)


    #aws_key = os.getenv('AWS_ACCESS_KEY_ID')
    #aws_secret = os.getenv('AWS_SECRET_ACCESS_KEY')

    aws_key = creds["AccessKeyId"]
    aws_secret = creds["SecretAccessKey"]
    aws_token = creds["Token"]

    session = boto3.Session(
    aws_access_key_id=aws_key,
    aws_secret_access_key=aws_secret,
    aws_session_token = aws_token
    )


    s3 = session.resource("s3")
    bucket = s3.Bucket(s3_bucket)
    print('printing AWS S3 bucket')
    for my_bucket_object in bucket.objects.all():
        print(my_bucket_object) 

    
    print('reading..')
    df  = pd.read_csv(path_read, sep =',')
    print('There are ' + str(len(df)) + ' rows')
    df['D'] = df['C'] + df['B']
    df.to_csv(path_write)

    


