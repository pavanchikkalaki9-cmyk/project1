import matplotlib.pyplot as plt

def selectionSort(array):
    n = len(array)
    for i in range(n):
        min = i
        for j in range(n):
            if array[j] > array[min]:
                array[j]
                array[j], array[min] = array[min], array[j]
    return array

array = []
n = int(input('How many elements you want in your array : '))
for i in range(n):
    e = int(input('Enter element :'))
    array.append(e)

print(f'Before swapping : {array}')
array = selectionSort(array)
print(f'After swapping : {array}')

x = list(range(1, 10000))
plt.plot(x, [x*y for y in x])
plt.title('Time complexity of selection sort is O(n\u00b2)')
plt.xlabel('Input')
plt.ylabel('Time')
plt.show()

