# this module will be imported in the into your flowgraph

f1 = 100
f2 = 200
f = f1
step = 10

def sweeper(prob_lvl):
    global f1,f2,f,step
    global a1,a2,a,astep
    if(prob_lvl):#prob_lvl
        f+=step
        print("f: ", f)
    else:
        print("f sweeper called without probe...")
    if(f>f2):
        f=f1
        
    return f
