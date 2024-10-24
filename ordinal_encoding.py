import numpy as np
import pandas as pd

data = {'Grade': ['A', 'C', 'B', 'F', 'A', 'D', 'B', 'F', 'C', 'F', 'A', 'F', 'C', 'D', 'B']}
df = pd.DataFrame(data)
grade_ranking = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'F': 5}
df['Grade_Encoded'] = df['Grade'].replace(grade_ranking)
print(df)
