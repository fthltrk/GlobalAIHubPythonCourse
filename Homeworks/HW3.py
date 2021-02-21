primeFirst=[]
primeSecond=[]
def prime_first(first):
    primeFirst.append(first)
    if first==499:
        print("Until 500: ",primeFirst)

def prime_second(second):
    primeSecond.append(second)
    if second==997:
        print("After 500: ",primeSecond)


for i in range(2,1000):
    prime=True
    if i<500:
        for j in range(2,i):
            if i%j==0:
                prime=False
        if prime:
            prime_first(i)
    else:
        for j in range(2,i):
            if i%j==0:
                prime=False
        if prime:
            prime_second(i)