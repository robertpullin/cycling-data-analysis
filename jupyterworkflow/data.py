# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:44:10 2021

@author: RP
"""


from urllib.request import urlretrieve
import os
import pandas as pd

# Link to data that can be retrieved without a file path and/or clicks
# e.g. URL, database, etc.
URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

# This function downloads the data and puts it in the repo if it doesn't already exist
def get_fremont_data(filename='fremont-bridge.csv',url=URL,force_download=False):

    """Download and cache the fremont data set
    
    Parameters
    ----------
    filename : string (optional)
      location to save the data
    url : string (optional)
      web location of the data
    force_download : bool (optional)
      if true, force re-download of data

    Returns
    -------
    data : pandas.DataFrame
      The fremont bridge data
    """

    if force_download or not os.path.exists(filename):
        urlretrieve(URL,filename)
        
    # Read the data into a dataframe    
    data = pd.read_csv('fremont-bridge.csv',index_col='Date')
    
    date_format = '%m/%d/%Y %H:%M:%S %p'
    
    try:
        data.index = pd.to_datetime(data.index,format=date_format)
    except:
        data.index = pd.to_datetime(data.index)

    
    # The columns are bit long so we can make them shorter
    data.columns = ['Total','East Sidewalk','West Sidewalk']
    
    return data