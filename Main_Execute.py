from Redshift.Redshift-Unload import * 
from S3.S3-Unload import *

if __name__ == "__main__":
    unload_tables_schema()
    s3_to_local()
    transform_files()
