# this module will be imported in the into your flowgraph

a1 = 0.1
a2 = 1.5
a = a1
astep = 0.1


def sweeper(prob_lvl):
    global a1,a2,a,astep

    if(prob_lvl):#prob_lvl
        a+=astep
        print("a: ", a)
    if(a>a2):
        a=a1
        
    return a 
