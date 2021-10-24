# 實作4-2

## 說明
Lab 4-4 整合超音波感測器 + LCD: 參考之前的實作, 完成以下任務:

1. **將超音波感測器傳回的距離, 在LCD上面顯示,** 
2. **同時也和之前的實作一樣, 在序列輸出.** 
3. **另外, 當物體的距離小於150cm時, 則亮紅色LED, 否則亮綠色LED**

### 電路圖
![image](https://user-images.githubusercontent.com/10968626/138579151-0807aac2-e59f-4c55-8f6b-9390681911f1.png)
![image](https://user-images.githubusercontent.com/10968626/138579162-f879200b-a110-40de-90c3-8c281a467974.png)

### 程式
```C
// include the library code:
#include <LiquidCrystal.h>

#define echo 7
#define trig 7
  
float  duration; 
float  dd;
int RLED = 9;
int GLED = 8;

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(13, 10, 6, 5, 4, 3);

void setup() {
  digitalWrite(RLED, OUTPUT);
  digitalWrite(GLED, OUTPUT);
  lcd.begin(16, 2);
}

void loop() {
  time_Measurement();
  dd = duration * 0.01723;   
  lcd.setCursor(0, 0);
  lcd.print("Distance, cm: ");
  lcd.setCursor(0, 1);
  lcd.print(dd);
  if (dd < 150) {
    digitalWrite(RLED, HIGH);
    digitalWrite(GLED, LOW);
  } else {
    digitalWrite(RLED, LOW);
    digitalWrite(GLED, HIGH);
  }
}

void time_Measurement()
  { //function to measure the time taken by the pulse to return back
    pinMode(trig, OUTPUT);
    digitalWrite(trig, LOW);
    delayMicroseconds(2);  
    digitalWrite(trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig, LOW);
    pinMode(echo, INPUT);  
    duration = pulseIn(echo, HIGH);
  }
```
