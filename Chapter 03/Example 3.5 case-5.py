def test():
    a=10
    b=20
    c= a+b
    all = [a,b,c]
    return all

x= test()
print (x[1])	#Call "b"
print (x[2])	#Call "c"