import pandas as pd
import numpy as np
import os

def sampling(filename):

    data = pd.read_csv(os.path.normpath(filename))
    data = data.iloc[:, 1:5]
    downsampled_data = []
    for column in data.columns:
        column_data = data[column].values
        downsampled_column = []
        chunk_size = 5

        # Iterate through the column data in chunks of size `chunk_size`
        for i in range(0, len(column_data), chunk_size):
            # Get the current chunk
            chunk = column_data[i:i + chunk_size]

            # Compute the mean of the current chunk
            mean_value = np.mean(chunk)

            # Append the mean value to the downsampled column list
            downsampled_column.append(mean_value)

        # Add the downsampled column to the list of downsampled data
        downsampled_data.append(downsampled_column)
        downsampled_array = np.array(downsampled_data)
        print(downsampled_array.shape)


    return downsampled_data


# sampling('D:\\feeddrive bad couple data\\Steady data\\csv\\E-3000(1).csv')
