
# 實作4-3

## 說明
Lab 4-3 LCD顯示"Hello" + 你的英文名字 (e.g., "Hello Horace")

### 電路圖
![電路圖](https://user-images.githubusercontent.com/10968626/138578710-9e41213d-c726-4ea8-a417-328ca6cc4221.png)

### 程式
```C
// include the library code:
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(13, 10, 6, 5, 4, 3);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("hello, dismal!");
}

void loop() {
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 1);
  // print the number of seconds since reset:
  lcd.print(millis() / 1000);
}
```

