import numpy as np

print(np.zeros(10, dtype='int'))

print(np.ones((3,5), dtype=float))

print(np.full((3,5),1.23))

print(np.arange(0, 20, 2))

print(np.linspace(0, 1, 5))

print(np.random.normal(0, 1, (3,3)))

print(np.eye(3))

x1 = np.array([4, 3, 4, 4, 8, 4])
print(x1[1])

x2 = np.random.randint(10, size=(3,4))
print(x2)
print(x2[2,3])


x = np.arange(10)
print(x)
print(x[::-1])