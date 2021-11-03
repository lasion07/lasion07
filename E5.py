def MyMathShower(*args):
    def sum(*args):
        s = 0.0
        
        for num in args:
            s += num
        
        return s

    def product(*args):
        p = 1.0

        for i in args:
            p *= i
        
        return p

    def diff(*args):
        dif = float(args[0])

        for i in range(1,len(args)):
            dif -= i

        return dif

    print('Tong:',sum(*args))
    print('Tich:',product(*args))
    print(diff(*args))

MyMathShower(10,4,1,1)