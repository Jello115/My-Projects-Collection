#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h> // The stable standard library
#include <SinricPro.h>
#include <SinricProSwitch.h>

// Credentials
#define WIFI_SSID         "Nasri"
#define WIFI_PASS         "2508nasri1012"
#define APP_KEY           "0a187fc5-c1ac-465b-947d-13777de7ebcf"
#define APP_SECRET        "5d7f3634-2751-4861-b3af-543357c0c0df-e4be7447-0b9d-4e5b-92c4-f536f57f320b"
#define SWITCH_ID         "69c4f97c17b32c0941dcd2e3"

#define RELAY_PIN         2  
#define BUTTON_PIN        0  

bool myPowerState = false; 
unsigned long lastBtnPress = 0;

WebServer server(80); // Standard Stable Server

const char index_html[] PROGMEM = R"rawliteral(
<!DOCTYPE HTML><html>
<head>
  <title>Pump Control</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { font-family: sans-serif; background: linear-gradient(45deg, #0f2027, #2c5364); color: white; height: 100vh; margin: 0; display: flex; align-items: center; justify-content: center; text-align: center; }
    .container { background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); padding: 50px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.2); }
    .btn { background: #00c6ff; border: none; color: white; padding: 20px 40px; font-size: 20px; border-radius: 10px; cursor: pointer; }
  </style>
</head>
<body>
  <div class="container">
    <h1>SMART PUMP</h1>
    <a href="/toggle"><button class="btn">TOGGLE POWER</button></a>
    <p>Status: <b>%STATE%</b></p>
  </div>
</body>
</html>)rawliteral";

void updateGlobalState(bool state) {
  myPowerState = state;
  digitalWrite(RELAY_PIN, myPowerState ? HIGH : LOW);
  SinricProSwitch &mySwitch = SinricPro[SWITCH_ID];
  mySwitch.sendPowerStateEvent(myPowerState);
}

void handleButton() {
  if (digitalRead(BUTTON_PIN) == LOW && (millis() - lastBtnPress > 400)) { 
    updateGlobalState(!myPowerState);
    lastBtnPress = millis();
  }
}

void handleRoot() {
  String s = index_html;
  s.replace("%STATE%", myPowerState ? "ON" : "OFF");
  server.send(200, "text/html", s);
}

void handleToggle() {
  updateGlobalState(!myPowerState);
  server.sendHeader("Location", "/");
  server.send(303);
}

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  digitalWrite(RELAY_PIN, LOW);

  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }

  Serial.println("\nWiFi Connected!");
  Serial.print("IP: "); Serial.println(WiFi.localIP());

  // Setup Standard Server Routes
  server.on("/", handleRoot);
  server.on("/toggle", handleToggle);
  server.begin();

  SinricProSwitch &mySwitch = SinricPro[SWITCH_ID];
  mySwitch.onPowerState([](const String &deviceId, bool &state) {
    updateGlobalState(state);
    return true;
  });
  SinricPro.begin(APP_KEY, APP_SECRET);
}

void loop() {
  server.handleClient(); // Standard server needs this
  handleButton();
  SinricPro.handle();
}