import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

verizon_data = 'Telco_Churn_Data.csv'

df = pd.read_csv(verizon_data)

df.head(10)