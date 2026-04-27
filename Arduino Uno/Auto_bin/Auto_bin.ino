#include <Servo.h>

const int pirPin = 2;       // PIR Sensor OUT pin
const int servoPin = 9;     // Servo Signal (Orange)
const int greenLedPin = 7;
const int redLedPin = 8; // Status LED

Servo butlerServo;

// --- ADJUST THESE FOR YOUR BIN ---
const int travelTime = 2500;   // Time to rotate 90 degrees
const int openWaitTime = 3500; // How long to stay open (5 seconds)
const int stopValue = 90;     
const int openSpeed = 180;    
const int closeSpeed = 0;     
// ---------------------------------

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(greenLedPin, OUTPUT);
  pinMode(redLedPin, OUTPUT);
  butlerServo.attach(servoPin);
  
  butlerServo.write(stopValue); // Start stopped
  digitalWrite(greenLedPin, LOW);
  digitalWrite(redLedPin, LOW);
  Serial.begin(9600);
}

void loop() {
  int motion = digitalRead(pirPin);

  if (motion == HIGH) {
    Serial.println("Hand detected! Opening...");
    
    // 1. OPEN simultaneously with LED
    digitalWrite(greenLedPin, HIGH);
    butlerServo.write(openSpeed);
    delay(travelTime);
    butlerServo.write(stopValue);
    
    // 2. WAIT while open
    delay(openWaitTime);
    
    // 3. CLOSE
    digitalWrite(greenLedPin, LOW);
    Serial.println("Closing...");
    digitalWrite(redLedPin, HIGH);
    butlerServo.write(closeSpeed);
    delay(travelTime);
    butlerServo.write(stopValue);
    
    // 4. RESET
    digitalWrite(redLedPin, LOW);
    
    // Small "Cool down" so it doesn't immediately re-trigger 
    // from the lid's own movement
    delay(2000); 
  }
}
