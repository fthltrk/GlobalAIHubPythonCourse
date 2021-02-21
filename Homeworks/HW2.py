grades=[[50,60,70], [30,40,70], [80,90,70], [20,50,90], [70,60,40]]
students=["fatih ulutürk", "ezgi subaşı", "aslı sarı", "merve coşkun", "deniz görgülü"]

d={}

for i in range(5):
    d[students[i]]=grades[i]   
print(d)
l=[]
for k in range(5):
    a=grades[k]
    t=sum(a)
    l.append(t)

for n in range(5):
    d[students[n]]=l[n]
print(d)

set_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
for i in set_d:
	k=i[0],i[1]
print(set_d)
f=set_d[0]
print("Tebrikler ",f[0])