# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#from google.colab import drive
#uploaded = files.upload()

# Import dataset
data = pd.read_csv('coding-grandmaster/m16/lesson1/Titanic Dataset.csv')
data.head(5)

# Check the datatype
data.dtypes

# Check Null Values
data.isnull().sum()