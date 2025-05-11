#include <ESP8266WiFi.h>
#include "DHT.h"
#include "ThingSpeak.h"

#define DHTPIN D4          // GPIO2
#define DHTTYPE DHT11
#define MQ135_PIN A0       // Analog input pin for MQ135

const char* ssid = "Siddu";         // Replace with your WiFi SSID
const char* password = "0987654321"; // Replace with your WiFi password
const char* apiKey = "5YQNCUMQC3JHL1X0";    // ThingSpeak API Key
const long channelNumber = 2933441;

WiFiClient client;
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println("\nConnected to WiFi!");
  ThingSpeak.begin(client);
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  int airQualityRaw = analogRead(MQ135_PIN);

  Serial.print("Temp: "); Serial.print(temperature);
  Serial.print(" °C, Humidity: "); Serial.print(humidity);
  Serial.print(" %, Air Quality (raw): "); Serial.println(airQualityRaw);

  // Send to ThingSpeak
  ThingSpeak.setField(1, temperature);
  ThingSpeak.setField(2, humidity);
  ThingSpeak.setField(3, airQualityRaw);

  int x = ThingSpeak.writeFields(channelNumber, apiKey);

  if (x == 200) {
    Serial.println("Data pushed successfully to ThingSpeak.");
  } else {
    Serial.print("Failed to push data. Error code: ");
    Serial.println(x);
  }

  delay(15000); // ThingSpeak allows updates every 15 seconds
}

