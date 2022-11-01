#include <LiquidCrystal.h>
int x;
//int rows=2;
//int columns=6;
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
int cart[6][2]={{1,120},
            {2,220},
            {3,130},
            {4,300},
            {5,350},
            {6,200}};
int price=0;

void setup() {

  Serial.begin(115200);
  // put your setup code here, to run once:
//data transmission code
}

void loop() {
  while(Serial.available()==0){}
  x=Serial.readString().toInt();
  shopping(x,cart[6][2]);
  // put your main code here, to run repeatedly:
//code to accept the id

}
void shopping(int id,  int a[6][2]){
  
  for(int b=1;b<=6;b++)
  {
    for (int c=1;c<=2;c++){
      if (a[c][0]==id){
        price+=a[c][1];
        Serial.print(price);
        displaylcd(price);}
        }}
}
void displaylcd(int p){
  lcd.begin(16, 2);
  lcd.print("price is Rs"+p);
  }
