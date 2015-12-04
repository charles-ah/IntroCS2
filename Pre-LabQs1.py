def f(x):

  x = x + 1

a = 3

f(a)

print a "return 3"

def g(L):

  L.append(3)

B = [ 0 ]

g(B)

print B "return [0, 3]"

def h(L):

   L = L + [ 2]

   L.append(3)

h(B)

print(B) "return [0, 3]"
