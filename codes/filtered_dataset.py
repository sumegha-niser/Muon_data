import pandas as pd
import numpy as np

#filename='23-04-03-14-43.data'

import pandas as pd
def filter_muon(filename):
    df = pd.read_csv(filename, delimiter=' ')

# Extract the first column of the DataFrame
    time_column = df.iloc[:, 0]

# Filter out muon decays less than 20000 ns
    filtered_time_column = time_column[time_column <= 20000]

# Save the filtered time values to a new file
    filtered_time_column.to_csv('filtered_{}'.format(filename), index=False, header=None)
    return 'filtered_{}'.format(filename)
    

#filter_muon(filename)