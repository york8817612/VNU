# 實作6-1

## 說明
Lab 6-1 用16X2 LCD 顯示器來顯示4X4鍵盤輸入的數字 (0, 1, 2, .., 9), 若輸入的字數≥16則換到下一列, 若兩皆滿, 則清除劃面重新由Row=0, Col=0開始

### 電路圖
![image](https://user-images.githubusercontent.com/10968626/139566733-b7ba9e65-069c-48ab-a405-e95d8d369e1a.png)
![image](https://user-images.githubusercontent.com/10968626/139566735-71610117-e4cd-4e41-bef1-f991184fbb09.png)
![image](https://user-images.githubusercontent.com/10968626/139566744-e4192f4b-768b-49d0-9eed-615dc6c9eb41.png)


### 程式
```C
#include <Keypad.h>
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const byte ROWS = 4; // 4列數(橫的)
const byte COLS = 4; // 4行數(直的)
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[ROWS] = {A0, A1, A2, 10}; //定義列的腳位
byte colPins[COLS] = {9, 8, 7, 6}; //定義行的腳位

int LCDCol = 0;
int LCDRow = 0;

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.setCursor(LCDCol, LCDRow);
}

void loop() {
  char key = keypad.getKey(); //讀取 Keypad 的輸入
  if (key){
    Serial.println(key);
    if (LCDCol >= 16) {
      LCDCol = 0;
      ++LCDRow;
      if (LCDRow > 1) {
        LCDRow = 0;
        lcd.clear();
      }
    }
    lcd.setCursor(LCDCol, LCDRow);
    ++LCDCol;
    lcd.print(key);
  }
}
```
