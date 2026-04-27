const int soilPin = A0;
const int buzzerPin = 8;
const int ledPin = 9;

// Adjust this based on your water test (344) and air test (1023)
const int dryThreshold = 850; 

void setup() {
  Serial.begin(9600);
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int moistureValue = analogRead(soilPin);
  
  Serial.print("Moisture: ");
  Serial.println(moistureValue);

  if (moistureValue > dryThreshold) {
    // SOIL IS DRY - Sound the alarm!
    digitalWrite(ledPin, HIGH);
    tone(buzzerPin, 1000); // Send a 1KHz sound signal
    delay(200);
    digitalWrite(ledPin, LOW);
    noTone(buzzerPin);
    delay(200);
  } else {
    // SOIL IS HAPPY
    digitalWrite(ledPin, LOW);
    noTone(buzzerPin);
  }

  delay(500);
}