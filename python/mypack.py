marks=100
def predict(x):
    return(x*2)+1
def myprimes(*val):
    #docstring
    'thiss functions returns a list of prime values by taking multiple numbers as input'
    l=[]
    for i in val:
        #print(i)
        if isprime(i):
            l.append(i)
    return l
def isprime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
        i=i+1
    if(count==2):
        return True
    else:
        return False
def welcome(**nam):
    for k,v in nam.items():
        print(k,v)
def mytable(n,start=1,stop=10):
    i=start
    while(i<=stop):
        print(str(n)+' * '+str(i)+' = '+str(n*i))
        i=i+1