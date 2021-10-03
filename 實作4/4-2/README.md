# 實作4-2

## 說明
Lab 4-2 如下圖的Demo, 用七段顯示器, 顯示 . →1→ ... → 9 → 0 → 全滅, 狀態改變的間隔時間為0.5秒

### 電路圖
![電路圖](https://user-images.githubusercontent.com/10968626/135739980-f84501c9-79a7-4301-a4ff-20ec9613d963.png)
### 程式
```C
// C++ code
//
void setup()
{
  for(int x = 1; x < 10; x++) {
      pinMode(x,OUTPUT);
  }
}

void SSD(int a, int b, int c, int d, int e, int f, int g, int h, int time = 500)
{
  digitalWrite(9, a);
  digitalWrite(2, b);
  digitalWrite(3, c);
  digitalWrite(4, d);
  digitalWrite(5, e);
  digitalWrite(6, f);
  digitalWrite(7, g);
  digitalWrite(8, h);
  delay(time);
}

void Display(int num) 
{
  switch (num) {
  	case 0:
    	SSD(0, 0, 0, 0, 0, 0, 0, 0, 0);
    	SSD(1, 1, 1, 1, 1, 1, 0, 0);
    	break;
    case 1:
    	SSD(0, 0, 0, 0, 0, 0, 0, 0, 0);
    	SSD(0, 1, 1, 0, 0, 0, 0, 0);
    	break;
    case 2:
    	SSD(0, 0, 0, 0, 0, 0, 0, 0, 0);
    	SSD(1, 1, 0, 1, 1, 0, 1, 0);
    	break;
    case 3:
    	SSD(0, 0, 0, 0, 0, 0, 0, 0, 0);
    	SSD(1, 1, 1, 1, 0, 0, 1, 0);
    	break;
    case 4:
    	SSD(0, 0, 0, 0, 0, 0, 0, 0, 0);
    	SSD(0, 1, 1, 0, 0, 1, 1, 0);
    	break;
    case 5:
    	SSD(0, 0, 0, 0, 0, 0, 0, 0, 0);
    	SSD(1, 0, 1, 1, 0, 1, 1, 0);
    	break;
    case 6:
    	SSD(0, 0, 0, 0, 0, 0, 0, 0, 0);
    	SSD(1, 0, 1, 1, 1, 1, 1, 0);
    	break;
    case 7:
    	SSD(0, 0, 0, 0, 0, 0, 0, 0, 0);
    	SSD(1, 1, 1, 0, 0, 1, 0, 0);
    	break;
    case 8:
    	SSD(0, 0, 0, 0, 0, 0, 0, 0, 0);
    	SSD(1, 1, 1, 1, 1, 1, 1, 0);
    	break;
    case 9:
    	SSD(0, 0, 0, 0, 0, 0, 0, 0, 0);
    	SSD(1, 1, 1, 1, 0, 1, 1, 0);
    	break;
    case 99: // dp
    	SSD(0, 0, 0, 0, 0, 0, 0, 0, 0);
    	SSD(0, 0, 0, 0, 0, 0, 0, 1);
    	break;
    default: // off
    	SSD(0, 0, 0, 0, 0, 0, 0, 0, 0);
    	SSD(0, 0, 0, 0, 0, 0, 0, 0);
    	break;
  }
}

void loop()
{
  	Display(100);
  	Display(99);
  	Display(1);
  	Display(2);
  	Display(3);
  	Display(4);
  	Display(5);
  	Display(6);
  	Display(7);
  	Display(8);
  	Display(9);
  	Display(0);
}
```
