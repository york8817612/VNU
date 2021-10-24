# 實作5-1

## 說明
Lab 5-1 請使用兩個伺服馬達同步從 0 度逐步掃描到 180 度之後再逐步掃描回0度, 每步的間隔時間為50ms (0.05秒)

### 電路圖
![image](https://user-images.githubusercontent.com/10968626/138579602-64742ed4-dbbf-4a90-941b-fc6a09a00f48.png)
![image](https://user-images.githubusercontent.com/10968626/138579608-91994064-2985-4645-b516-8be8686ef7ef.png)


### 程式
```C
// C++ code
#include <Servo.h>

int pos = 0;

Servo servo_9;
Servo servo_10;

void setup()
{
  servo_9.attach(9, 500, 2500);
  servo_10.attach(10, 500, 2500);

}

void loop()
{
  for (pos = 0; pos <= 180; pos += 1) {
    servo_9.write(pos);
    servo_10.write(pos);
    delay(50);
  }
  for (pos = 180; pos >= 0; pos -= 1) {
    servo_9.write(pos);
    servo_10.write(pos);
    delay(50);
  }
}
```
