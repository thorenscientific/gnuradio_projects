# this module will be imported in the into your flowgraph

f1 = 100
f2 = 200
f = f1
step = 10

a1 = 0.1
a2 = 1.5
a = a1
astep = 0.1
fcount = 0
acount = 0
def sweeper(prob_lvl):
    global f1,f2,f,step
    if(prob_lvl):#prob_lvl
        f+=step
        print("f: ", f)
    else:
        print("f sweeper called without probe")
#        fcount += 1
    if(f>f2):
        f=f1
        
    return f

def amplitude_sweeper(prob_lvl):
    global a1,a2,a,astep

    if(prob_lvl):#prob_lvl
        a+=astep
        print("a: ", a)
    else:
        print("a sweeper called without probe")
#        acount += 1
    if(a>a2):
        a=a1
        
    return a 
