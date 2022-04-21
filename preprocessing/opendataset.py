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
    exit(1)


class load_data:
    """load dataset"""
    def __init__(self, filename:str) -> DataFrame:
        # extract file type

        # open dataset
        self.dataset= self.open_csv(filename=filename)
        pass

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