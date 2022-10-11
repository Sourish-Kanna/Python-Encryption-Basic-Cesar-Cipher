def One(x):
    print(x+1,x)

def Two(x):
    print(x+2,x)

def Three(x):
    print(x+3,x)

def Def(x):
    print(x+0,x)


x=5

dictt = {1:One,2:Two,3:Three}

pic= dictt.get(x,Def)

pic(x)
