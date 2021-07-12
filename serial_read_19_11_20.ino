#define SoundPin 5

int SoundValue;
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {  SoundValue = digitalRead(SoundPin); // Getting noise threshold value and saving it in variable
  Serial.print("Noise = "); //Displaying Noise
  Serial.print(SoundValue);
  Serial.print("dB");
  Serial.println();
  delay(1000);
}

  
