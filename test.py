myNumbers = [1,2,3,4,5,6,7,8,9,10]

def square(x):
    return x**2

evens = list(filter(lambda x: x%2 == 0, myNumbers))
print(evens)