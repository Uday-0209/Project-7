'''automate the pca and saving as single file'''
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import os
# result_df = pd.DataFrame(columns=['metrix'])
# directory = "D:\\motor drive data\\lavanya\\stft data\\correct data\\missalignment"
# pca = PCA(n_components=512)
# files  = os.listdir("D:\\motor drive data\\lavanya\\stft data\\correct data\\missalignment")
# result_list = []
# for file in files:
#     file_path = os.path.join(directory, file)
#     df = pd.read_csv(file_path)
#     df_transposed = df.T
#     reduced_matrix = pca.fit_transform(df_transposed)
#     metrix = reduced_matrix.T
#     print('file_name:',file,'shape:',metrix.shape)
#     matrix_str = ','.join(map(str, metrix.flatten()))
#     result_list.append({'metrix':matrix_str,'label':'Missalign'})
#
# result_df = pd.DataFrame(result_list)
# result_df.to_csv('D:\\motor drive data\\lavanya\\training data\\missalignment_data.csv', index=False)
# print(result_df.head())
#--------------------------------------------------------------------------------------------------------------------
# '''adding and labeling good and bad'''
df1 = pd.read_csv("D:\\motor drive data\\lavanya\\training data\\good_data.csv")
df2 = pd.read_csv("D:\\motor drive data\\lavanya\\training data\\lossness_data.csv")
df3 = pd.read_csv("D:\\motor drive data\\lavanya\\training data\\missalignment_data.csv")
df4 = pd.read_csv("D:\\motor drive data\\lavanya\\training data\\Unbalance_data.csv")

df3 = pd.concat([df1,df2, df3, df4])
# tp = {'LOOSNESS':1,'MISS ALIGNMENT':2,'reference':0, 'UNBALANCE':3}
# df3['label_num'] = df3.label.map(tp)
df4 = df3[['metrix','label']]

df4.to_csv('D:\\motor drive data\\lavanya\\training data\\the_complete_data.csv')
print(df4.head(10))
print(df4.shape)
#--------------------------------------------------------------------------------------------------------------------
'''pca to individual file'''
# #file_path = os.path.join(directory, file)
# pca = PCA(n_components=512)
# df = pd.read_csv("D:\\Test rig vibration stft ml model\\stft files\\Bad data couple stft\\2000_750.csv")
# result_df = pd.DataFrame(columns=['metrix'])
# result_list=[]
# print(df.shape)
# df_transposed = df.T
# reduced_matrix = pca.fit_transform(df_transposed)
# metrix = reduced_matrix.T
# print(type(metrix))
# #print(metrix)
# print(metrix.shape)
# # metrix_flatten = metrix.flatten()
# # print(metrix_flatten.shape)
# # print()
# matrix_str = ','.join(map(str, metrix.flatten()))
# result_list.append({'metrix':matrix_str})
# print(type(result_list))
# print(len(result_list))
# result_df = pd.DataFrame(result_list)
# result_df.to_csv('D:\\Test rig vibration stft ml model\\testing files\\2000_bad_couple.csv', index=False)
# print(result_df.shape)
# print(result_df.head())