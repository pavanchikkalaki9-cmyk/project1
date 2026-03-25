import matiplotlid.py as plt
def bubblesort (array):
    n=len (array)
    for i in range(n-1):
        swapped=False
        for j in range (n-1-i):
            if array[i]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
            swapped=true
            if swapped==flase:
                break
            return array
array=[]
n=int (input("how many element??"))
for i in range (n):
    array.appand (int(input(f"enter%d element"%j)))
print(f"befor suapping:{array}")
array=bubblesort(array)
print(f"affer swapped:{array}")
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title ("bubblesort time complexity is 0(n\u00b2)")
plt.xlable ("input")
plt.ylable ("time")
pit.show()
