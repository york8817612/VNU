# Lab 10-2 OpenCV電腦視覺入門
## 描述
OpenCV電腦視覺入門

## 程式碼
### 實作
```python
# Your Code
#205 openCV簡易繪圖範例
import numpy as np
# 建立一張 256x256 的 RGB 圖片（0黑色）
img = np.zeros((256, 256, 3), np.uint8) #np.zeros建立0矩陣
# 將圖片用淺灰色 (200, 200, 200) 填滿
img.fill(200)
# 在圖片上畫一條紫紅色的對角線，寬度為 5 px (0,0在最左上角)
# cv2.line(影像, 開始座標, 結束座標, 顏色, 線條寬度)
cv2.line(img, (0, 0), (255, 255), (255, 0, 255), 5)
cv2.line(img, (255, 0), (0, 255), (255, 0, 255), 5)
# 畫文字
cv2.putText(img, ('Dismal'), (80, 50), cv2.FONT_HERSHEY_SIMPLEX,
    1, (0, 255, 255), 5, cv2.LINE_AA)
# 顯示圖片
cv2_imshow(img)
```
## 成果
![image](https://user-images.githubusercontent.com/10968626/144733017-3887a225-5824-422e-a70b-f36baffafb70.png)

![image](https://user-images.githubusercontent.com/10968626/144733031-fb986282-e6c3-4a2f-9754-b11d34c74a26.png)
![image](https://user-images.githubusercontent.com/10968626/144733033-aa68e1ae-2a2b-4c4d-b6b1-c91d1ac390e3.png)
![image](https://user-images.githubusercontent.com/10968626/144733036-dbe2a765-d0e6-4804-b67a-8ffe78234e49.png)
![image](https://user-images.githubusercontent.com/10968626/144733039-dfe88b3f-7342-4aa3-a824-7b2f266fc2f0.png)
![image](https://user-images.githubusercontent.com/10968626/144733045-d5dd9935-f94e-42db-a846-8c162377dc6f.png)


