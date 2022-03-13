s = input()
n = int(input())
s_list = [input() for i in range(n)]
count = 0
beauty = 0
for Str in s_list:
    s = s.replace(Str,' ')
    beauty += (s.count(' ')-count)*len(Str)
    count = s.count(' ')
print(beauty)



'''import itertools
n = int(input())
l = [int(input()) for i in range(n)]

Set = set(l)
for i in range(2,n):
    for comb in itertools.combinations(l,i):
        Set.add(sum(comb))
Set.add(sum(l))
List = sorted(Set)
if len(List)==1:
    print(0^List[0])
else:
    S = List[0]
    for i in range(1,len(List)):
        S ^= List[i]
    print(S)'''


'''k = int(input())
n = int(input())
Qpower = [int(input()) for i in range(k)]
fav_s = [int(input()) for i in range(n)]
power = []
count = 0
for i in range(n):
    k = int(input())
    if Qpower[fav_s[i]-1]>0:
        count += 1
        Qpower[fav_s[i]-1] -= k
print(count)'''




