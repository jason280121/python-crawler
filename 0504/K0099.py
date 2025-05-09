import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data9 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(data9)


#建立日期
# dates = pd.date_range('20250504', periods=6)
# print(dates)