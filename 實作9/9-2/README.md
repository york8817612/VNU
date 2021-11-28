# Lab 9-2 Python的5個回顧練習
## 描述
Python的5個回顧練習

## Question 1
![image](https://user-images.githubusercontent.com/10968626/143728886-6518a68a-d941-4129-8c8e-b649e0ff5756.png)

### 程式碼
```pyton
# 1. 印出一個9X9的直角三角形
for i in range(1, 10):
    print("*" * i)
```
### 結果
![image](https://user-images.githubusercontent.com/10968626/143729058-c90ea98f-79b4-4dcb-ba2c-bee22b4d746f.png)

## Question 2
![image](https://user-images.githubusercontent.com/10968626/143728921-28076bca-5890-4d25-b00a-668bc3f72892.png)

### 程式碼
```pyton
# 2. 製作10~30之間奇數清單
for i in range(10, 30):
  if (i%2):
    print(i)
```
### 結果
![image](https://user-images.githubusercontent.com/10968626/143729110-eef52542-0ef0-4144-bdff-2c42c94daef7.png)

## Question 3
![image](https://user-images.githubusercontent.com/10968626/143728929-1932be7b-0c86-4796-828e-2e21dd9b5910.png)

### 程式碼
```pyton
# 3. 製作20~3之間偶數清單
for i in range(20, 3, -2):
    print(i)
```
### 結果
![image](https://user-images.githubusercontent.com/10968626/143729202-c2708b80-61b5-4e80-be82-397974b78720.png)

## Question 4
![image](https://user-images.githubusercontent.com/10968626/143728937-cc39b1f4-615c-4233-8fa6-eb9dca7dea42.png)

### 程式碼
```pyton
# 4. 印出3X3乘法表
for i in range(1,4):
  for j in range(1,4):
    print("%s X %s = %s" % (i, j, i*j))
```
### 結果
![image](https://user-images.githubusercontent.com/10968626/143729298-e9251386-cbeb-43e3-a538-fe1757930495.png)
![image](https://user-images.githubusercontent.com/10968626/143729340-8e4fe0e9-1292-4bb9-9fac-3932a495c1cc.png)

## Question 5
![image](https://user-images.githubusercontent.com/10968626/143728946-45bb49e7-ea9e-4a5c-aefb-6d2a43485ff3.png)

### 程式碼
```pyton
# 5. 請使用funtion, 設計可以求出1~n之間被2整除的正整數清單
num = int(input())
arr = []
for i in range(1, num+1):
  if i % 2 != 1:
    arr.append(i)
print(arr)
```
### 結果
![image](https://user-images.githubusercontent.com/10968626/143729454-e08082db-43ec-44f9-83dc-3a69fcbc46e0.png)
