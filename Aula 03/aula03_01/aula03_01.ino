// Trigger envia um ping atraves da porta 8
int trigPin = 8;
// Echo recebe a resposta atraves do pino 7
int echoPin = 7;
// Observa o tempo que leva pra sinal ir e voltar
long duration;
// sera usado para converter o tempo para cm
long distance_cm; 

void setup() {
  // configurar os pinos com i/o
  Serial.begin (9600); 
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT);
  
}

void loop() {
  //envia o sinal em loop
  digitalWrite(trigPin, LOW); 
  digitalWrite(trigPin, HIGH);
  digitalWrite(trigPin, LOW);
  // capta a duração em microssegundos do sinal high captado pelo echo
  duration = pulseIn(echoPin, HIGH);

  // som viaja a 34300 cms a cada 100000μs
  // o que significa 29 cm por 1μs
  // precisamos dividir a duracao da ida e volta por 29 
  //e depois ao meio pois a onda vai e volta
  distance_cm = duration / 29 / 2; 
 
  Serial.print(distance_cm);
  Serial.print(" cm");
  Serial.println();
  delay(2000);
  

}
