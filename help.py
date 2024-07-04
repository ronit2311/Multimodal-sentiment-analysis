numerator=int(input("enter number"))
denominator=int(input("enter denominator"))
num = [int(a) for a in str(numerator)]
den = [int(a) for a in str(denominator)]

if len(num)>len(den):
    short= len(den)
elif len(num)<len(den):
    short= len(num)
else:
    short = len(den)

def remove():
    for i in num:
        for j in den:
            if i==j:
                num.remove(i)
                den.remove(j)

for k in range(short):
    remove()


if num == [] :
    print("1")

elif den==[0]:
    print("-1")
else:
    n = [str(i) for i in num]
    val = int("".join(n))
    d = [str(j) for j in den]
    val1 = int("".join(d))
    print(val/val1)



        



