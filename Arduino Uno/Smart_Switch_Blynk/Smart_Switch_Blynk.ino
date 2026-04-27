// 1. REPLACE THESE 3 LINES WITH THE ONES FROM YOUR SCREEN
#define BLYNK_TEMPLATE_ID "TMPL6WxnP6xXM"
#define BLYNK_TEMPLATE_NAME "Quickstart Template"
#define BLYNK_AUTH_TOKEN "4zjqsswjtq1ETCGbIRrTtn0Uv9_kaZmK"

// 2. The Libraries
#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>

// 3. Your Network Credentials
char ssid[] = "Nasri";
char pass[] = "2508nasri1012";

// Pin 2 is your LED/Pump pin
const int relayPin = 2;

// This function tells Blynk what to do when you toggle the V0 button in the app
BLYNK_WRITE(V1) { 
  int value = param.asInt(); // Get the state of the button (0 or 1)
  digitalWrite(relayPin, value); // Turn LED/Pump on or off
  Serial.print("Blynk Button V1 state: ");
  Serial.println(value);
  if(value == 1) {
    Blynk.logEvent("light_on", "The light is turned On!");
  }
  else if(value == 0) {
    Blynk.logEvent("light_off", "The light is turned OFF!");
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(relayPin, OUTPUT);
  
  // Start Blynk connection
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);
}

void loop() {
  Blynk.run(); // This keeps the connection alive
}