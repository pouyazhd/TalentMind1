"""laus deo
Project name: Loop academy telent mind project
Project description: 
Module: opendataset
Module description: to load and open dataset.
Developer: P.Zahedi. 
E-Mail: p.zahedi@live.com
"""

import logging
from sys import exit

try:
    from pandas import read_csv, DataFrame
except Exception as err:
    logging.error(err)
    raise "Error in import pandas. please check if module installed correctly"

try:
    import kaggle
except Exception as err:
    logging.error(err)
    raise "Error in import kaggle. please check if module installed correctly."


class load_data:
    """load dataset"""
    def __init__(self, filename:str) -> DataFrame:
        # extract file type

        # open dataset
        self.dataset= self.open_csv(filename=filename)
        
        
        return self.dataset

    def open_csv(self, filename:str)-> DataFrame:
        """oped csv file dataset usuing pandas

        Args:
            filename (str): address of the file to open

        Returns:
            DataFrame: data frame of loaded dataset
        """

        try:
            loaded_dataset = read_csv(filename)
            return loaded_dataset
        except Exception as err:
            logging.error(err)
            raise "Error in reading dataset. read logs for more info."
    
    def download_from_kaggle(self):
        pass