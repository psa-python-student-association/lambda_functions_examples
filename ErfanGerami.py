def new(l):
    li=[]
    for t in l:
        if abs(t)==t:
            li.append(t)
    return li
mylist=lambda l: [i  for i in l if i>=0]
