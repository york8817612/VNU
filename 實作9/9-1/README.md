# Lab 9-1 AI應用起手式: 使用 TensorFlow Hub 進行圖像分類
## 描述
使用 TensorFlow Hub 進行圖像分類

## 程式碼
### 實作B
```python
# 809 實作B: 在圖像上運行模型
# 
%time 

probabilities = tf.nn.softmax(classifier(image)).numpy()

top_5 = tf.argsort(probabilities, axis=-1, direction="DESCENDING")[0][:5].numpy()
np_classes = np.array(classes)
includes_background_class = probabilities.shape[1] == 1001

for i, item in enumerate(top_5):
  class_index = item if not includes_background_class else item - 1
  line = f'({i+1}) {class_index:4} - {classes[class_index]}: {probabilities[0][top_5][i]}'
  translation1 = E_2_TW.translate(classes[class_index])
  print(line, ', ', translation1)

show_image(image, '')

```
### 實作C
```python
# 實作C: 從已提供的選項中,找一張自己喜歡的照片來試試看
image_name = "cat"

img_url = images_for_test_map[image_name]
image, original_image = load_image(img_url, image_size, dynamic_size, max_dynamic_size)
probabilities = tf.nn.softmax(classifier(image)).numpy()

top_5 = tf.argsort(probabilities, axis=-1, direction="DESCENDING")[0][:5].numpy()
np_classes = np.array(classes)
includes_background_class = probabilities.shape[1] == 1001

for i, item in enumerate(top_5):
  class_index = item if not includes_background_class else item - 1
  line = f'({i+1}) {class_index:4} - {classes[class_index]}: {probabilities[0][top_5][i]}'
  translation1 = E_2_TW.translate(classes[class_index])
  print(line, ', ', translation1)

show_image(image, '')
```
### 實作D
```python
# 實作D (Optional): 從網路上找一張自己喜歡的照片來試試看 (jpg/png)
image_name = "wolf"
images_for_test_map['wolf'] = "https://upload.wikimedia.org/wikipedia/commons/a/ab/European_grey_wolf_in_Prague_zoo.jpg"

img_url = images_for_test_map[image_name]
image, original_image = load_image(img_url, image_size, dynamic_size, max_dynamic_size)
probabilities = tf.nn.softmax(classifier(image)).numpy()

top_5 = tf.argsort(probabilities, axis=-1, direction="DESCENDING")[0][:5].numpy()
np_classes = np.array(classes)
includes_background_class = probabilities.shape[1] == 1001

for i, item in enumerate(top_5):
  class_index = item if not includes_background_class else item - 1
  line = f'({i+1}) {class_index:4} - {classes[class_index]}: {probabilities[0][top_5][i]}'
  translation1 = E_2_TW.translate(classes[class_index])
  print(line, ', ', translation1)

show_image(image, '')
```
## 成果
![image](https://user-images.githubusercontent.com/10968626/143728744-0dafffdc-9e12-4700-b30e-95d01d1c6f69.png)
![image](https://user-images.githubusercontent.com/10968626/143728754-8c77de86-f54f-4438-a044-312bc734c600.png)
![image](https://user-images.githubusercontent.com/10968626/143728768-8a4806c0-bb5f-48ee-af0f-3e9da997e43f.png)
![image](https://user-images.githubusercontent.com/10968626/143728778-e51d9de4-1bfb-493f-ab37-3fa3e372c8ee.png)
![image](https://user-images.githubusercontent.com/10968626/143728787-a95692d2-6039-4353-8469-666139e42528.png)
![image](https://user-images.githubusercontent.com/10968626/143728797-a4b26d56-9986-44db-ab3d-32a7a1cb5778.png)


