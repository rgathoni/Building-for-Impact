import pickle
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

#load processed data and labels from pickle file
data_dict = pickle.load(open('./data.pickle', 'rb'))

#extract data and labels
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

#split data into training and testing sets (80% training, 20% testing)
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

print(x_train.shape) #verify training data

#initialize Random Forest Classifier model
model = RandomForestClassifier()

#train model -- using training data
model.fit(x_train, y_train)

#predictions on test data
y_predict = model.predict(x_test)

#compute model accuracy
score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

# Save trained model to a pickle file
# with open('model.p', 'wb') as f:
#     pickle.dump({'model': model}, f)
f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
