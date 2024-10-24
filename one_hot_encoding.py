import numpy as np
import pandas as pd
data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Green', 'Red', 'Blue', 'Blue', 'Green', 'Red', 'Red', 'Blue',
                  'Blue', 'Red', 'Blue', 'Green', 'Blue', 'Blue', 'Red', 'Blue', 'Green', 'Blue']}
df = pd.DataFrame(data)
df_encoded = pd.get_dummies(df, columns=['Color'])
df_encoded = df_encoded.astype(int)
print(df_encoded)
