import pandas as pd
from utils.configmanager import *

def transform_files():

	'''
		Giving Belcorp Project TOP's files the format that they need
	'''

    for key in FILE_DICT:
        
        LOCAL_KEY = '{path}{filename}'.format(path=LOCAL_PATH_DOWNLOAD,
        										filename=key)
        
        df = pd.read_csv(LOCAL_KEY, sep=',', 
        							encoding='utf-8',
        							names=FILE_DICT[key]['values'], 
        							dtype=str)

        if key != CSV_FILE:
            
            df.to_excel('{path}{excelfile}'.format(path=LOCAL_PATH_FORMAT, 
            										excelfile=FILE_DICT[key]['file_name']),
            								index = False)
        
        else:
            df.to_csv('{path}{csvfilename}'.format(path=LOCAL_PATH_FORMAT, 
            										csvfilename=FILE_DICT[key]['file_name']), 
            								index= False)

