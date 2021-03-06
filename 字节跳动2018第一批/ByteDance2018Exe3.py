'''
产品经理(PM)有很多好的idea，而这些idea需要程序员实现。
现在有N个PM，在某个时间会想出一个 idea，每个 idea 有提出时间、所需时间和优先等级。
对于一个PM来说，最想实现的idea首先考虑优先等级高的，相同的情况下优先所需时间最小的，还相同的情况下选择最早想出的，
没有 PM 会在同一时刻提出两个 idea。

同时有M个程序员，每个程序员空闲的时候就会查看每个PM尚未执行并且最想完成的一个idea,
然后从中挑选出所需时间最小的一个idea独立实现，如果所需时间相同则选择PM序号最小的。
直到完成了idea才会重复上述操作。如果有多个同时处于空闲状态的程序员，那么他们会依次进行查看idea的操作。

求每个idea实现的时间。

输入第一行三个数N、M、P，分别表示有N个PM，M个程序员，P个idea。随后有P行，
每行有4个数字，分别是PM序号、提出时间、优先等级和所需时间。输出P行，分别表示每个idea实现的时间点。
'''

aux =list(map(int,input().split()))
nbcxy = aux[0]
nbpm = aux[1]
nbjob = aux[2]
listjob = []
for _ in range(nbjob):
    listjob.append(list(map(int,input().split())))
def distibu(jobs):
    idx = 0
    for i in range(1,len(jobs)):
        for j in [2,3,1,0]:
            if jobs[i][j]>jobs[idx][j]:
                break
            if jobs[i][j]<jobs[idx][j]:
                idx = i
                break
    return idx

copie = listjob.copy()
listjob.sort(key = lambda x:x[1])
listwait = []
listjobtemp=[0]*nbjob
temp = 0
wroking=[0]*nbcxy
while listjob or listwait:
    #depose idee
    while True:
        if listjob and temp >= listjob[0][1]:
            listwait.append(listjob[0])
            listjob.pop(0)
        else:
            break
    for i in range(len(wroking)):
        if(wroking[i] <= 0)and listwait != []:
            idx = distibu(listwait)
            wroking[i] = listwait[idx][3]
            # print(listwait[idx])
            # print(listjob)
            listjobtemp[copie.index(listwait[idx])] = temp + listwait[idx][3]
            listwait.pop(idx)
        wroking[i] -= 1
    temp += 1
for i in listjobtemp:
    print(i)
'''
input:
2 2 5
1 1 1 2
1 2 1 1
1 3 2 2
2 1 1 2
2 3 5 5
output:
3
4
5
3
9
'''
