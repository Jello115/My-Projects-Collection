int pirPin = 2;    // Input pin from PIR sensor
int ledPin = 13;   // Pin for the LED
int val = 0;       // Variable for reading the pin status

void setup() {
  pinMode(ledPin, OUTPUT);      // Declare LED as output
  pinMode(pirPin, INPUT);       // Declare sensor as input
  Serial.begin(9600);
}

void loop() {
  val = digitalRead(pirPin);    // Read input value
  
  if (val == HIGH) {            // Check if the input is HIGH
    digitalWrite(ledPin, HIGH); // Turn LED ON
    Serial.println("Motion detected!");
  } else {
    digitalWrite(ledPin, LOW);  // Turn LED OFF
    Serial.println("No motion.");
  }
  delay(100); 
}