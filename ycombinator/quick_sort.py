

Y = lambda f: lambda *args: f(Y(f))(*args)

# quick sort
qs = Y( lambda f:
  lambda x: (
    f( [ i for i in x if i < x[0] ] )
    + [ i for i in x if i == x[0] ]
    + f( [ i for i in x if i > x[0] ] )
  ) if x else []
)


a = [9,3,8,2,6,1,9]

print(a)
print(qs(a))
