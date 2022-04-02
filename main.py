"""laus deo
Project name: Loop academy telent mind project
Project description: 
Module: main
Module description: main module.
Developer: P.Zahedi. 
E-Mail: p.zahedi@live.com
"""

import logging
logging.basicConfig(filemode="a",format="")

import yaml 
from sys import exit

# load config file
def load_configs(config_file:str) -> dict:
    """load configs contain params, paths and etc from config file.

    Args:
        config_file (str): config file path

    Returns:
        dict: configs dict
    """
    try:
        with open(file=config_file, mode="r", encoding="utf-8") as config_ptr:
            conf = yaml.safe_load(config_ptr)
            logging.info("configs read successfully")
            return conf

    except Exception as err:
        logging.error(err)
        logging.info("programm stopped.")
        exit(0)

if __name__ == "__main__":
    CONFIGS = load_configs("conf.yaml")