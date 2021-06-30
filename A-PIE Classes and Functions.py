# -*- coding: utf-8 -*-
"""
 A-PIE

"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2

# Import our own Function and Class files and Reload
import stream_functions
importlib.reload(stream_functions)

import stream_classes
importlib.reload(stream_classes)


# Input Parameters
ric = 'DBK.DE'   # DBK.DE -  MXN=X
file_extension = 'csv'

x, x_str, t = stream_functions.load_time_series(ric, file_extension)
stream_functions.plot_timeseries_price(t, ric)

z = stream_classes.jarque_bera_test(x, x_str)
z.compute()
print(z)

stream_functions.plot_histogram(x, x_str, z.plot_str(), bins=500) 


