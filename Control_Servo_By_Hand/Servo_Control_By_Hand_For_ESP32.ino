#include <WiFi.h> // Import the Wi-Fi library
#include <ESPAsyncWebServer.h> // Import the Async Web Server library
#include <ESP32Servo.h> // Import the Servo library

const char* ssid = "SSID";  // Change to your Wi-Fi SSID
const char* password = "Password";  // Change to your Wi-Fi Password

Servo myServo;
const int servoPin = 13;  // GPIO pin for the servo

AsyncWebServer server(80); 

void setup() {
  Serial.begin(115200);
  myServo.attach(servoPin);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Wi-Fi Connected! IP: " + WiFi.localIP().toString());

  server.on("/update", HTTP_GET, [](AsyncWebServerRequest* request) {
    if (request->hasParam("angle")) {
      int angle = request->getParam("angle")->value().toInt();
      Serial.println("Rotating to: " + String(angle));
      myServo.write(angle);
    }
    request->send(200, "text/plain", "OK");
  });

  server.begin();
}

void loop() {
  // Nothing needed in the loop, handled by the web server
}
