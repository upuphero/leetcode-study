C = [('e', 4, 2), ('a', 2, 1), ('c', 5, 4), ('b', 3, 3), ('d', 1, 5)]
print(sorted(C, key=lambda y: y[0]))
#输出[('a', 2, 1), ('b', 3, 3), ('c', 5, 4), ('d', 1, 5), ('e', 4, 2)]
print(sorted(C, key=lambda x: x[0]))
#[('a', 2, 1), ('b', 3, 3), ('c', 5, 4), ('d', 1, 5), ('e', 4, 2)]
print(sorted(C, key=lambda x: x[2]))
[('a', 2, 1), ('e', 4, 2), ('b', 3, 3), ('c', 5, 4), ('d', 1, 5)]