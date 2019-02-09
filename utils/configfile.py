import pathlib
import os
import configparser


# Settings variables
config = configparser.ConfigParser()
config.read('config.ini')

AWS_S3_BUCKET = config.get('S3-Credentials', 'AWS_BUCKET')
AWS_S3_ACCESS_KEY = config.get('S3-Credentials', 'AWS_ACCESS_KEY')
AWS_S3_SECRET_KEY = config.get('S3-Credentials', 'AWS_SECRET_KEY')
AWS_S3_FOLDER = config.get('S3-Credentials', 'AWS_FOLDER')


AWS_RS_HOST = config.get('Redshift-Credentials', 'RS_HOST')
AWS_RS_DATABASE = config.get('Redshift-Credentials', 'RS_DB')
AWS_RS_PORT = config.get('Redshift-Credentials', 'RS_PORT')
AWS_RS_USER = config.get('Redshift-Credentials', 'RS_USER')
AWS_RS_PASS = config.get('Redshift-Credentials', 'RS_PASS')
AWS_RS_SCHEMA = config.get('Redshift-Credentials', 'RS_SCHEMA')

LOCAL_DOWNLOAD_DIR = config.get('Local-Paths', 'DOWNLOAD_PATH')
LOCAL_FORMAT_DIR = config.get('Local-Paths', 'FORMAT_PATH')

FILE_DICT = config.get('Top-Variables', 'DICT_TOP_FILES')
CSV_FILE = config.get('Top-Variables', 'CSV_FILENAME')
