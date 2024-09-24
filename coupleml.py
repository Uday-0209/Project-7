import pandas as pd
import pickle as pkl
import numpy as np
import os
from sklearn.decomposition import PCA

def mlmodel2(file_path):
    # with open("D:\\Test rig vibration stft ml model\\model pkl\\mlpclasiimodel_testrig_couple.pkl", 'rb') as file:
    with open("D:\\Test rig vibration stft ml model\\model pkl\\g1+b1_stft_data_couple.pkl", 'rb') as file:
        model = pkl.load(file)
    pca = PCA(n_components=512)
    df = pd.read_csv(os.path.normpath(file_path))
    X_test = pd.DataFrame(columns=['metrix'])
    result_list = []
    df_transposed = df.T
    reduced_matrix = pca.fit_transform(df_transposed)
    metrix = reduced_matrix.T
    matrix_str = ','.join(map(str, metrix.flatten()))
    result_list.append({'metrix': matrix_str})
    X_test = pd.DataFrame(result_list)
    X_test = X_test['metrix'].apply(lambda x: np.array([float(i) for i in x.split(',')]))
    X_test = np.vstack(X_test)
    y_pred = model.predict(X_test)
    if y_pred[0] == [1]:
        print('Good')
        return 'couple in good condition'

    else:
        print('Bad Data')
        return 'couple in bad condition'

# file_path = input()
#
# mlmodel2(file_path)