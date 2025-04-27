import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load and preprocess dataset
data = pd.read_csv('fruit_spoilage_large.csv')

# Encode Yes/No to 1/0
data['Spoilage'] = LabelEncoder().fit_transform(data['Spoilage'])

X = data[['Temperature', 'Humidity', 'CO2', 'Days']]
y = data['Spoilage']

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

def predict(temp, humidity, co2, days):
    return model.predict([[temp, humidity, co2, days]])[0]
