# arr = [1,564,213,23,54]
# for i in range(len(arr)):
#     for z in range(len(arr)-1):
#         if arr[z] < arr[z+1]:
#             arr[z],arr[z+1] = arr[z+1],arr[z]
# print(arr)
#сортировка пузырьком




# import random
# import time
# def arrRandmizer(size):
#     arr = []
#     for i in range(size):
#         arr.append(random.randint(1,1000000))
#     return arr
#
# def bubleSort(arr):
#     for i in range(len(arr)):
#         for z in range(len(arr) - 1):
#             if arr[z] < arr[z + 1]:
#                 arr[z], arr[z + 1] = arr[z + 1], arr[z]
# arr = arrRandmizer(10000)

# startTime = time.time()
# bubleSort(arr)
# endTime = time.time()
# print(endTime-startTime)







import random
import time
def arrRandmizer(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(1,1000000))
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
# arr = [12, 11, 13, 5, 6]
# insertion_sort(arr)
# print ("Sorted array is:")
# for i in range(len(arr)):
#     print (arr[i])

arr = arrRandmizer(10000)

startTime = time.time()
insertion_sort(arr)
endTime = time.time()
print(endTime-startTime)







import random
import time
def arrRandmizer(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(1,1000000))
    return arr
def shecker_sort(arr)
    for i in range
left = 0
right = len(arr) - 1

while left <= right:
    for i in range(left, right, 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    right -= 1

    for i in range(right, left, -1):
        if arr[i - 1] > arr[i]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    left += 1

print(arr)