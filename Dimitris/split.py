import os.path as path
import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split

train_data_path = path.join(path.pardir, 'train.csv')
data = pd.read_csv(train_data_path)
new_test: DataFrame
new_train, new_test = train_test_split(data, test_size=0.2)
new_train.to_csv(path_or_buf=path.join(path.pardir, 'new_train.csv'))
new_test.to_csv(path_or_buf=path.join(path.pardir, 'new_test.csv'))
