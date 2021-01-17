void setup(){

  Serial.begin(9600);
  Serial.println("Olá Mundo!");   
                                }



void loop(){

  digitalWrite(13, HIGH);
  Serial.println("LED ligado");
  delay(1000);

  digitalWrite(13, LOW);
  Serial.println("LED desligado");
  delay(1000);}

            
