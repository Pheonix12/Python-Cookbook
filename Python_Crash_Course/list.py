from rich import print

motorcycles = ['honda', 'ducati', 'suzuki']

print("The bikes i have are " + motorcycles[0])



motorcycles.append('royal enfiled')
print(motorcycles)

# list.pop() ---  removes last item in list. can't be restored
print("1. The bike i have is " + motorcycles.pop())
print(motorcycles)


# list.remove() --- removes by the value, if you don't know the position on the list
# only removes the 1st occarance, for duplicate values need to use a loop condition. 
motorcycles.remove("honda")
print("2. remove", motorcycles)

motorcycles = ['honda', 'ducati', 'suzuki']
x = 'honda'
motorcycles.remove(x)
print("3. remove by assigned varriable", motorcycles)
