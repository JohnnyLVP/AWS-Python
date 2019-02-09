import psycopg2
import sys
from utils.configmanager import *

def rs_connection():
    '''
        Connection to Redshift
    '''
    con = psycopg2.connect(host=AWS_RS_HOST,
                           port=AWS_RS_PORT,
                           dbname=AWS_RS_DATABASE,
                           user=AWS_RS_USER,
                           password=AWS_RS_PASS)

    cur = con.cursor()

    return cur,con


def unload_table(RS_SCHEMA_NAME,RS_TABLE_NAME):
    '''
        Choosing an especific table to be downloaded.

        Requirements: 
            - Access Key y Secret Key with S3 policies.
            - Bucket Destination, where data data is going to be saved.
    '''
    try:
        cur, con = rs_connection()

    except:
        print('Unable to connect!\n{}'.format(psycopg2.InternalError))
        sys.exit(1)

    qry = 'select * from {schema}.{table}'.format(schema=RS_SCHEMA_NAME,
                                                    table=RS_TABLE_NAME)

    s3_path = 's3://{bucket}/{folder}/{filename}_'.format(bucket=AWS_S3_BUCKET,
                                                            folder=AWS_S3_FOLDER,
                                                            filename=RS_TABLE_NAME)

    query = '''
            unload (%(select_query)s)
            to %(s3_path)s
            access_key_id %(s3_key_id)s
            secret_access_key %(s3_secret_key)s
            ALLOWOVERWRITE
            MAXFILESIZE 1 GB
            DELIMITER ','
            PARALLEL OFF;
            '''

    select_param = {'select_query': qry,
                    's3_path':s3_path,
                    's3_key_id':AWS_S3_ACCESS_KEY,
                    's3_secret_key':AWS_S3_SECRET_KEY}

    cur.execute(query, select_param)
    con.commit()


def f_tables(RS_SCHEMA):
    '''
        Selecting all tables in a schema using a created view.
    
        The view [v_space_used_per_tbl] is located: 
        [1]: https://github.com/awslabs/amazon-redshift-utils/blob/master/src/AdminViews/v_space_used_per_tbl.sql
    
    '''
    try:
        cur, con = rs_connection()
    
    except:
        print('Unable to connect!\n{}'.format(psycopg2.InternalError))
        sys.exit(1)
    
    qry =   '''
            SELECT DISTINCT tablename 
            FROM public.v_space_used_per_tbl 
            WHERE schemaname = %(schemaname)s;
            '''
    
    select_param = { 'schemaname': RS_SCHEMA}
    
    cur.execute(qry, select_param)
    
    x = cur.fetchall()
    
    return x

def  unload_tables_schema():
    '''
        Unload all tables in the schema using the 2 functions below
    '''

    tables = f_tables(RS_SCHEMA_NAME)

    for record in tables:

        unload_table(SCHEMANAME,record[0])

