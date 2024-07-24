import os

import boto3
import os
from dotenv import load_dotenv
load_dotenv()

localhost= os.getenv('localhost')
user = os.getenv('user')
password= os.getenv('password')

def load():
    s3 = boto3.resource(
        's3',
        endpoint_url = f'{localhost}:9000',
        aws_access_key_id=user,
        aws_secret_access_key=password,
    )

    # Print out bucket names
    for bucket in s3.buckets.all():
        print(bucket.name)

    # # Upload a new file
    # with open('1.jpeg', 'rb') as data:
    #     s3.Bucket('mem').put_object(Key='1.jpeg', Body=data)

    # #upload a new bucket
    # response = s3.create_bucket(
    #     Bucket='examplebucket',
    # )
    #
    # print(response)

def down():
    s3 = boto3.client('s3',
        endpoint_url = f'{localhost}:9000',
        aws_access_key_id=user,
        aws_secret_access_key=password,
    )
    # down = s3.download_file('mem', '5.jpeg', 'new2.jpeg')


    list = s3.list_objects(Bucket='mem')['Contents']
    for key in list:
        s3.download_file('mem', key['Key'], key['Key'])

if __name__ == "__main__":
    down()