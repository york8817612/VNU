# 實作5-2

## 說明
Lab 5-2 LCD顯示溫度感應器的溫度;若溫度<38 綠LED亮; 若大於38度, 紅色LED亮

### 電路圖
![image](https://user-images.githubusercontent.com/10968626/138580192-b1b531b5-dfd3-4330-8579-7e3dcd96890a.png)
![image](https://user-images.githubusercontent.com/10968626/138580197-e6ac81c6-2d97-4dd8-bc55-f9268df04351.png)


### 程式
```C
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int RLED = 8;
int GLED = 7;
void setup() {
  lcd.begin(16, 2);
  digitalWrite(RLED, OUTPUT);
  digitalWrite(GLED, OUTPUT);
  pinMode(A1, INPUT);
}

void loop() {
  float reading = analogRead(A1);  // read analog level level (2^10)
  float voltage = (reading/1024) * 5;
  float tempC = (voltage - 0.5) * 100;
  lcd.setCursor(0,0);  
  lcd.print("TMP Sensor Demo");
  lcd.setCursor(0,1);
  lcd.print("Tmp:");
  lcd.print(tempC);
  lcd.print(" C");
  if (tempC < 38) {
    digitalWrite(RLED, LOW);
  	digitalWrite(GLED, HIGH);
  } else {
  	digitalWrite(RLED, HIGH);
  	digitalWrite(GLED, LOW);
  }
  delay(500);
  lcd.clear();
}
```
