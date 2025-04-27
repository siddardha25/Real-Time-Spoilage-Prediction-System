🚀 Project Title
Real-Time Spoilage Prediction of Perishable Goods

A smart IoT system combining sensor-based monitoring and computer vision to predict spoilage in real-time. This solution helps automate the detection of food spoilage, offering timely alerts and minimizing wastage.

💡 Problem & Solution
Problem:
Manual monitoring of perishable goods is error-prone and inconsistent.

Solution:
Our system uses live sensor data and webcam images analyzed by a machine learning model to automate spoilage detection. Real-time alerts enable faster action to prevent loss and ensure safety.

🛠️ Technical Approach
Technologies/Tools/Frameworks
NodeMCU ESP8266 - Data transmission	

DHT11 Sensor - Temperature & Humidity monitoring

MQ135 Sensor - CO₂ concentration detection

Laptop Webcam + OpenCV - Image capture

Flask - Backend server

scikit-learn - Machine Learning for spoilage prediction

Architecture Overview
Sensors collect environmental data via ESP8266.

Webcam captures fruit images.

Flask server receives and processes inputs.

ML model predicts spoilage status.

Web app displays live dashboard and sends alerts.


🔥 Feasibility & Viability
Time Feasibility:
Prototype development is achievable within a hackathon timeframe.

Challenges:
Sensor calibration and real-time ML inference optimization.

Scalability:
Easily extendable to cold chains, warehouses, and retail stores.

Resources Used:
Low-cost hardware and open-source software.

🌎 Impact & Benefits
Beneficiaries: Farmers, warehouse managers, food retailers

Innovation: Sensor fusion with vision-based AI

Impact: Reduces spoilage, ensures food safety, minimizes economic losses

Outcomes:

Real-time monitoring dashboard

Automated spoilage alerts

Lowered food wastage

🎯 Alignment with SDG Goals
Goal 12: Responsible Consumption and Production

Promotes sustainable supply chains

Enables efficient food storage monitoring


