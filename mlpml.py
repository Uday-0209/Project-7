import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report , confusion_matrix, accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import pickle

data = pd.read_csv("D:\\motor drive data\\lavanya\\training data\\the_complete_data.csv")
print(data.label.value_counts())
labels = {'Unbalance':1,'Loose':2, 'Missalign':3, 'Good':0}
data['label_num'] = data.label.map(labels)
data = data[['metrix','label_num']]
print(data.label_num.value_counts())

X_train = data[['metrix']]

X_train = data['metrix'].apply(lambda x:np.array([float(i) for i in x.split(',')]))

X_train = np.vstack(X_train.values)

Y_train = data['label_num']

#MLP = MLPClassifier(hidden_layer_sizes=(40,20),max_iter=100, activation='relu',solver='adam', alpha=0.0001, batch_size = 10, learning_rate='constant', random_state=4)
#lg = LogisticRegression(multi_class='multinomial')
#rfc = RandomForestClassifier(n_estimators=10, max_depth=5)
dtc = DecisionTreeClassifier(max_depth=5)
#svc = SVC(kernel = 'linear')
#knc = KNeighborsClassifier(n_neighbors=4)
#gnb = GaussianNB()

#model = MLP.fit(X_train, Y_train)
#LGM = lg.fit(X_train, Y_train)
#RFC = rfc.fit(X_train, Y_train)
DTC = dtc.fit(X_train, Y_train)
#SVVC = svc.fit(X_train, Y_train)
#KNC = knc.fit(X_train, Y_train)
#GNB = gnb.fit(X_train, Y_train)
with open("D:\\motor drive data\\lavanya\\models\\motor_DTCmodel2.pkl", 'wb') as file:
     pickle.dump(DTC, file)

#y_pred = model.predict(X_train)
#y_pred1 = LGM.predict(X_train)
#y_pred2 = RFC.predict(X_train)
y_pred3 = DTC.predict(X_train)
#y_pred4 = SVVC.predict(X_train)
#y_pred5 = KNC.predict(X_train)
#y_pred6 = GNB.predict(X_train)

# print(accuracy_score(Y_train, y_pred))
#print(confusion_matrix(Y_train, y_pred))

#print('MLP:',classification_report(Y_train, y_pred))
#print('LGM:',classification_report(Y_train, y_pred1))
#print('RFC',classification_report(Y_train, y_pred2))
print('DTC:',classification_report(Y_train, y_pred3))
#print('SVVC:',classification_report(Y_train, y_pred4))
#print('KNC:',classification_report(Y_train, y_pred5))
#print('GNB:',classification_report(Y_train, y_pred6))