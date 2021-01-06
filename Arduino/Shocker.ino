
const int shockPin = 13; // the pin that the LED is attached to
const int tonePin = 8;
const int expPin = 2;
int incomingByte;      // a variable to read incoming serial data into
String r;
long t;

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  Serial.setTimeout(15);
  // initialize the LED pin as an output:
  pinMode(shockPin, OUTPUT);
  pinMode(tonePin, OUTPUT);
  pinMode(expPin, OUTPUT);
  digitalWrite(expPin,LOW);
//  Bipbip for init useless (GG)
//  tone(8,400,200);
//  delay(200);
//  tone(8,400,200);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();

    // Send pulse depending on what information was sent by the Python program
    if (incomingByte == 'S'){
      t = 0;
      while(t == 0){
        r = Serial.readString();
        t = r.toInt();
      }

      digitalWrite(shockPin, HIGH);
      delay(t);
      digitalWrite(shockPin,LOW);
      Serial.println("Done");
    }

    if (incomingByte == 'T'){

      t = 0;
      while(t == 0){
        r = Serial.readString();
        t = r.toInt();
      }
      tone(8,1000,t);
      Serial.println("Done");
    }

    if (incomingByte == 'A'){
      t = 0;
      while(t == 0){
        r = Serial.readString();
        t = r.toInt();
      }
      
      tone(8,400,t);
      digitalWrite(shockPin, HIGH);
      delay(t);
      digitalWrite(shockPin,LOW);
      Serial.println("Done");
    }
    if (incomingByte == 'W'){
      t = 0;
      while(t == 0){
        r = Serial.readString();
        t = r.toInt();
      }
      delay(t);
      Serial.println("Done");
    }

    if (incomingByte == 'D'){
      digitalWrite(expPin,HIGH);
      Serial.println("Done");
    }

    if (incomingByte == 'F'){
      digitalWrite(expPin,LOW);
      Serial.println("Done");
    }
  }
}
