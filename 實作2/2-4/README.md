# 實作2-1

## 說明
實作2-2, RGB LED燈全彩模組, 分別讓LED輪流表現正紅、正綠、正藍，三個顏色，時間間隔1秒鐘。並且觀查LED顏色和波形或是電壓有什麼關連性? 可將個人說明在更新GitHub時一起加入. (互動2), (2021-09-05)

### 電路圖
![電路圖](s.PNG)
### 程式
```C
// C++ code
//
int Red = 11;
int Green = 10;
int Blue = 9;
void setup()
{
  pinMode(Red, OUTPUT);
  pinMode(Green, OUTPUT);
  pinMode(Blue, OUTPUT);
}

void loop()
{
  analogWrite(Red, 255);
  analogWrite(Green, 0);
  analogWrite(Blue, 0);
  delay(1000);
  analogWrite(Red, 0);
  analogWrite(Green, 255);
  analogWrite(Blue, 0);
  delay(1000);
  analogWrite(Red, 0);
  analogWrite(Green, 0);
  analogWrite(Blue, 255);
  delay(1000);
}
```
