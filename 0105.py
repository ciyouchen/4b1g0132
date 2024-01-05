class Dog:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    def bark(self):
        print(f"{self._name} is barking!")

# 創建三個Dog
a1 = Dog('小黑', '5', '50')
a2 = Dog('小白', '3', '40')
a3 = Dog('小黃', '7', '60')

# 輸出每個狗狗的資訊
print("狗a1姓名 =", a1._name)
print("狗a1年齡 =", a1._age)
print("狗a1身高 =", a1._height)

print("狗a2姓名 =", a2._name)
print("狗a2年齡 =", a2._age)
print("狗a2身高 =", a2._height)

print("狗a3姓名 =", a3._name)
print("狗a3年齡 =", a3._age)
print("狗a3身高 =", a3._height)

# 使用bark方法
a1.bark()
a2.bark()
a3.bark()
