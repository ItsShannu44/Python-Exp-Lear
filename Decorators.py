#_____________Decorators_____________________

def wrap(f):
    def inner():
        print('Got Decorated')
        f() #calling outerone inside inner
    return inner

d = wrap(10)
print(d)



def div(x,y):
    print(x/y)

#wrapper func
def check(f):
    def value(x, y):
        if x<y:
            x,y=y,x
            return f(x,y)
        return f(x,y)
    return value
#decorate the normal func
df=check(div)
df(10,12)

#______________Syntactic Decorators__________

def split_val(f):
    def val():
        func=f()
        u_v=func.split()
        return u_v
    return val


def upper_val(f):
    def val():
        func=f()
        u_v=func.upper()
        return u_v
    return val

#Applying decorators on the normal program

@upper_val
def input_val():
    return 'this is python'
print(input_val())

@split_val
def input_val():
    return 'this is python'
print(input_val())


#Applying Decorator functions that can take parameters or on functions do not take

#___________________Wrapper Function_____________________________

def dec(f):
    def wrap(*args, **kwargs):
        print(f"The positional args are {args}")
        print(f"The keyword args are {kwargs}")
        f(*args)
    return wrap

#apply decorator on afunc that take parameters
@dec
def func_no():
    print("No Args Passed")
print(func_no())

#Apply the decorator on a function that take the positional args

@dec 
def f_pos(a,b,c):
    print(f"The parameters are {a}, {b}, {c}")
print(f_pos(2,4,8))

#Apply the decorator on a function that take the Kw args
@dec 
def f_key():
    print("The function takes keyword args")

print(f_key(f_name='Harry', l_name="Potter", age=11))


