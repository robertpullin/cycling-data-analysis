# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:16:04 2021

@author: RP
"""

from jupyterworkflow.data import get_fremont_data
import pandas as pd
import numpy as np

data = get_fremont_data()

def test_fremont_data():
    assert all(data.columns)
    assert isinstance(data.index,pd.DatetimeIndex)
    assert len(np.unique(data.index.time) == 24)