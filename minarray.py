arr = [9999,445454,235,223,43,4325,5,235,52,35,5,5,45,24,543,4,245,245,42,5,425,425,45,9954333232]

largest = arr[0]
for z in arr:
    if z > largest:
        largest = z
print(largest)

arr = [12, 5, 8, 21, 3, 7]
smallest = sorted(arr)[0]
print("Smallest number:", smallest)

arr = [12, 5, 8, 21, 3, 7]  
print("Smallest number:", min(arr)) 