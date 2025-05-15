int ledPins[] = {2, 3, 4, 5, 6};  // Thumb, Index, Middle, Ring, Pinky

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);  // Ensure LEDs are off initially
  }
}

void loop() {
  if (Serial.available() >= 5) {
    byte fingerStates[5];
    Serial.readBytes(fingerStates, 5);  // Read all 5 bytes at once

    for (int i = 0; i < 5; i++) {
      digitalWrite(ledPins[i], fingerStates[i] == 1 ? HIGH : LOW);
    }

    // Debug output (optional)
    // Serial.print("Received: ");
    // for (int i = 0; i < 5; i++) Serial.print(fingerStates[i]);
    // Serial.println();
  }
}
