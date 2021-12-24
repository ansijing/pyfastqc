list_t = []
list_1 = [1, 2, 1, 2]
list_2 = [3, 4, 3, 4]
list_3 = [5, 6, 5, 6]
list_t = [list_1, list_2, list_3]






list_t.append(list_1)
list_t.append(list_2)
list_t.append(list_3)
print(list_t)
print(list_1 + list_3)

result = []
for i in range(len(list_1)):
    result.append(list_1[i] + list_2[i])
print("sum: ",result) 