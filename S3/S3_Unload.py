import boto3
import botocore

from Redshift.Redshift_Unload import *
from utils.configfile import *

def s3_to_local():

    '''
    Funtions to save RS downloaded Files into Local Computer.

    Redshift Files subfix always finish in '000' for that in the function
    For that, I declare REMOTE_KEY AND LOCAL_KEY  in that way.

    '''
    s3 = boto3.resource('s3')

    tables = f_tables(AWS_RS_SCHEMA)

    for table in tables:

        REMOTE_KEY = '{folder}/{filename}_000'.format(folder=AWS_S3_FOLDER,
                                                    filename=table[0])

        LOCAL_KEY = '{localfolder}{filename}_000'.format(local_folder=LOCAL_PATH_DOWNLOAD, 
                                                        filename=table[0])
        try:
            s3.Bucket(AWS_S3_BUCKET).download_file(REMOTE_KEY, LOCAL_KEY)
        
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise