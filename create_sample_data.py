import pandas as pd
import numpy as np

columns = ['A', 'B', 'C', 'D']

for i in range(1000, 1100):

    filename = r'data/' + str(i) + '.ftr'

    df = pd.DataFrame(
        np.random.randint(0, 1000, size=(1000, 4) )
        , columns=columns
    ) 
    df.to_feather(filename)