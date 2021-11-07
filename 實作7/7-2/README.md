# 實作7: AI-based ES? AI? ML? DL? 要如何入門 (How To Learn)?
## 描述
Lab 7-2 暖身: 一起來十分鐘學會Python

## 步驟
建立我們的第二個Colab Notebook (Filename: 十分鐘學會Python.ipynb)

## 成果
* task 1: string variable
```python
name = "MingLi"
print(name)
```
![image](https://user-images.githubusercontent.com/10968626/140632219-bc4e1224-891d-49ce-9aa1-7977bef6f4d9.png)

* task 2: number variable
```python
number = 29
print(number)
print(number*3)
print(number/2)
print(number + number)
print(number - number)
```
![image](https://user-images.githubusercontent.com/10968626/140632237-0756e579-f27d-402f-bb2c-9a918b384717.png)


* task 3: function
```python
def printName(firstName, lastName):
  print(lastName + ' ' + firstName)

printName('Li', 'Ming')
```
![image](https://user-images.githubusercontent.com/10968626/140632263-1953e733-1867-42ba-af45-db40af023108.png)


* task 4: if else
```python
def printName(firstName, lastName, isCool):
  if isCool:
    print(lastName + ' ' + firstName + ' very cool!')
  else:
    print(lastName + ' ' + firstName + ' not cool!')

printName('Li', 'Ming', True)
printName('Li', 'Ming', False)
```
![image](https://user-images.githubusercontent.com/10968626/140632244-99b6e1d7-ea02-4c75-bbc4-ee99c27fdc0a.png)


* task 5: for loop
```python
# task 5: for loop
def printName(firstName, lastName, isCool, num):
  for i in range(1, num):
    if isCool:
      print(i, lastName + ' ' + firstName + ' very cool!')
    else:
      print(i, lastName + ' ' + firstName + ' not cool!')

# Start
printName('Li', 'Ming', True, 5)
```
![image](https://user-images.githubusercontent.com/10968626/140632296-f0ee07bc-cee7-45ee-a4c2-8f7e7216c9aa.png)
