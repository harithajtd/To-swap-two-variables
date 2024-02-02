#PYTHON PROGRAM TO SWAP TWO VARIABLES
#USing a temporary variable
x=5
y=10

#create a temperory variable ans swap the values
temp=x
x=y
y=temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


'''_____________________________________________________________'''


#Without using temporary variable
x=5
y=10
x,y=y,x
print('x=',x)
print('y=',y)


'''____________________________________________________________'''


#If the variables are both numbers, we can use arithmetic
#operations to do the same. It might not look intuitive at
#first sight. But if you think about it, it is pretty easy to
#figure it out. Here are a few examples

x=4
y=2

#Addition and Subtraction
x=x+y
y=x-y
x=x-y

print(x)
print(y)

#Multiplication and Division
x=4
y=2

x=x*y
y=x/y
x=x/y

print(x)
print(y)

#XOR swap
#This algorithm works for integers only
x=4
y=2

x=x^y
y=x^y
x=x^y

print(x)
print(y)
