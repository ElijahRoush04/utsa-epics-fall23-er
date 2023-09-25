/*
	Alternate Blink
		1.	Turn on LED1, turn off LED2 for 
			1 second (at the same time)
		2.	Turn off LED1, turn on LED2 for 
			1 second (at the same time)
		3.	Repeat
*/

  int pinA=13;
  int pinB=12;

  void setup() {
    pinMode(pinA,OUTPUT);
    pinMode(pinB,OUTPUT);
  
  }

  void loop() {
    //turn on pinA and turn off pinB
    digitalWrite(pinA,HIGH);
    digitalWrite(pinB,LOW);
  
    //wait 1 sec
    delay(500);

    //turn off pinA and turn on pinB
    digitalWrite(pinA,LOW);
    digitalWrite(pinB,HIGH);

    //wait 1 sec
    delay(500);
  }
