int A=0,B=0;
int SUM,CARRY;


void setup() {
    pinMode(2, OUTPUT);  
    pinMode(3, OUTPUT);
   
}


void loop() {
  
 SUM=(!A&&B) || (!B&&A);
CARRY=(A&&B);

  digitalWrite(2, SUM); 
  digitalWrite(3, CARRY); 
  }
