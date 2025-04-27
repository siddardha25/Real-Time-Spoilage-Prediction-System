from django.shortcuts import render
from django.http import JsonResponse
import requests
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import json

# Train the ML model once when the server starts
data = {
    'temperature': [25, 28, 30, 32, 35, 27],
    'humidity': [60, 65, 72, 75, 80, 68],
    'gas': [300, 350, 600, 650, 700, 320],
    'label': [0, 0, 1, 1, 1, 0]  # 0 = Fresh, 1 = Spoiled
}

df = pd.DataFrame(data)
X = df[['temperature', 'humidity', 'gas']]
y = df['label']

model = RandomForestClassifier()
model.fit(X, y)

# ThingSpeak config
THINGSPEAK_CHANNEL_ID = '2933441'
THINGSPEAK_READ_API_KEY = 'UIQT1TXRZV6Y21ST'

def index(request):
    return render(request, 'index.html')

def latest(request):
    url = f"https://api.thingspeak.com/channels/{THINGSPEAK_CHANNEL_ID}/feeds.json?api_key={THINGSPEAK_READ_API_KEY}&results=1"
    try:
        response = requests.get(url)
        data = response.json()

        if not data['feeds']:
            return JsonResponse({"error": "No data found"}, status=404)

        feed = data['feeds'][0]
        temp = float(feed['field1'])
        hum = float(feed['field2'])
        gas = float(feed['field3'])

        return JsonResponse({
            "temperature": temp,
            "humidity": hum,
            "gas": gas
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:
            input_data = json.loads(request.body)
            features = [[input_data['temp'], input_data['hum'], input_data['co2']]]
            prediction = model.predict(features)[0]
            result = "Spoiled" if prediction == 1 else "Fresh"
            return JsonResponse({"output": result})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid HTTP method"}, status=405)
