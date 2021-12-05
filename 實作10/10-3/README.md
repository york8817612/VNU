# Lab 10-3 人臉辨識實際應用
## 描述
人臉辨識實際應用

## 程式碼
### 實作1
```python
# Your Code
image = face_recognition.load_image_file("24470007n9n69r1065s2.jpg") #92
faces = face_recognition.face_locations(image,model='cnn')
print("找到臉的數量=",len(faces))
for (top, right, bottom, left) in faces: #畫矩形框 可改框的顏色/線條粗細
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
plt.figure(figsize=(12,10))
cv2.putText(image, ('Dismal'), (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 5, cv2.LINE_AA)
plt.imshow(image)
```
### 實作2
```python
# Your Code
image = face_recognition.load_image_file("24470007n9n69r1065s2.jpg") #92
faces = face_recognition.face_locations(image)
print("找到臉的數量=",len(faces))
for (top, right, bottom, left) in faces: #畫矩形框 可改框的顏色/線條粗細
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
plt.figure(figsize=(12,10))
cv2.putText(image, ('Dismal'), (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 5, cv2.LINE_AA)
plt.imshow(image)
```
## 成果
![image](https://user-images.githubusercontent.com/10968626/144733466-ea148498-1901-4c61-a421-04fb23e7449f.png)
![image](https://user-images.githubusercontent.com/10968626/144733471-6ec25987-541f-4c69-8eea-1a7b206c33a7.png)
![image](https://user-images.githubusercontent.com/10968626/144733480-000ff987-0865-40ea-8ef0-ce43ca0fe4f2.png)
![image](https://user-images.githubusercontent.com/10968626/144733483-25d5f480-13b7-4731-986f-1f62001bf83e.png)
![image](https://user-images.githubusercontent.com/10968626/144733487-ba5abb82-a77b-4b9e-a99d-8bb18ccc254b.png)
![image](https://user-images.githubusercontent.com/10968626/144733490-5ca95705-fa94-4ee1-94b8-c77b7d704948.png)
![image](https://user-images.githubusercontent.com/10968626/144733495-71ee56a7-6bae-4d63-8f28-cb45de4a00c7.png)
![image](https://user-images.githubusercontent.com/10968626/144733499-40282033-1a87-40fc-84c2-54aee511543c.png)
![image](https://user-images.githubusercontent.com/10968626/144733506-56e44339-2cc3-4a8a-889a-ed2af4f2f5b6.png)
![image](https://user-images.githubusercontent.com/10968626/144733508-007a15fc-4f1d-43a5-8990-da290da8b672.png)
![image](https://user-images.githubusercontent.com/10968626/144733512-7d32f5ff-e5da-4ee7-ade3-a7c7b4a4c641.png)
![image](https://user-images.githubusercontent.com/10968626/144733516-b56899df-eaf7-4d2c-b12c-0d1089fb89ad.png)
