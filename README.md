# Labwork 4 Unit tests
## General
Файл `main` содержит классы `Point` и `Face` описывающих точку и грань в пространстве, соответственно. Методы классов позволяют находить необходимые геометрические величины и поворачивать объекты. Файл `test` содержит **unit** тесты позволяющие проверить корректность методов данных классов.

## Classes
### Point
`rotate`  поворачивает точку вокруг заданной оси на заданное число радиан по часововй стрелке:
```python
p = Point(1, 1, 1)
p.rotate_x(math.pi) # 1 1 -1
```

`length` находит расстояние от точки до начала координат:
```python
p.length() # 1.73205080
```

`angle_cos` находит косинус угла между двумя точками с вершиной в начале координат:
```python
p2 = Point(1, -1, 1)
p.angle_cos(p2) # 0.707106781
```
### Face
`rotate` поворачивает грань вокруг заданной оси на заданное число радиан:
```python
v1 = Point(1, 2, 3)
v2 = Point(-2, 3, 4)
v3 = Point(5, -1, 5)
face = Face([v1, v2, v3])
face.rotate_x(1)
# 1 -1.4438083426874098 3.3038488872202123
# 5 -4.747657229907622 1.8600405445328023
# 5.0 1.195668134641914 11.116221377419665
```

`normal` находит нормаль данной грани:
```python
n = face.normal() # 5 10 5
```

`is_visible` проверяет видна ли грань из заданной точки:
```python
vp = Point(0, 0, 0)
p.is_visible(vp) # True
```

## Tests
`TestPointFunc` и `TestFaceFunc` тестируют методы соответствующих классов сравнивая результаты их работы с заведомо верными ответами. Так как вычисления производятся с нецелочисленным типом, сравнения происходит с точностью до определенного числа знаков.
