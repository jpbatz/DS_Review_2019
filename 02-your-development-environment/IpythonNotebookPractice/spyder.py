# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

data = np.random.rand(100)
pd.Series(data).cumsum().plot()