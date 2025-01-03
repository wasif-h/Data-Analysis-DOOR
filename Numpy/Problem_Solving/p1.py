import numpy as np

arr = np.array([], dtype=np.int32)
num = int(input("How Many Days Temp : "))
for i in range(num):
    value = int(input("Days {} Temp -> ".format(i)))
    arr = np.append(arr, value)
avg = arr.mean()
count = 0
print("Average -> ", avg)
for item in arr:
    if (item > avg):
        count += 1

print(f"{count} Days's are above average")
