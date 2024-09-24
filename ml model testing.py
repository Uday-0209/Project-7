import pickle as pkl
import pandas as pd
import os
import numpy as np
from sklearn.decomposition import PCA

pca = PCA(n_components=512)
directory = "D:\\motor drive data\\lavanya\\stft data"
files = os.listdir("D:\\motor drive data\\lavanya\\stft data")
prediction = []
with open("D:\\Test rig vibration stft ml model\\model pkl\\mlpml_model_testrig_downsample.pkl", 'rb') as file:
    model = pkl.load(file)
for file in files:
    print(file)
    file_path = os.path.join(directory,file)
    title = os.listdir(file_path)
    for doc in title:
        #print(doc)
        result_list = []
        file_path1 = os.path.join(file_path,doc)
        print(file_path1)
        data = pd.read_csv(file_path1)
        data_transposed = data.T
        data_reduce_metrix = pca.fit_transform(data_transposed)
        metrix = data_reduce_metrix.T
        metrix_str = ','.join(map(str, metrix.flatten()))
        result_list.append({'metrix': metrix_str})
        X_test = pd.DataFrame(result_list)
        X_test = X_test['metrix'].apply(lambda x: np.array([float(i) for i in x.split(',')]))
        X_test = np.vstack(X_test)
        y_pred = model.predict(X_test)

        if y_pred[0] == [1]:
            print('Good')
            prediction.append({'file path':file_path1,'result':'Good'})
            #return 'Good Data'

        else:
            print('Bad Data')
            prediction.append({'file path':file_path1, 'result':'Bad'})
            #return 'Bad Data'

    predi = pd.DataFrame(prediction)
    predi.to_csv('D:\\Test rig vibration stft ml model\\output5.csv')
