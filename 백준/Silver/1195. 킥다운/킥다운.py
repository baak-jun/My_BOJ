import sys
def input():return sys.stdin.readline().rstrip()

a = input()

b = input()

al = len(a)
bl = len(b)

if not al>bl:
    a,b = b,a
    al,bl = bl,al
mlen = min(al,bl)

#print(a,b)

k =  ["0" for i in range(al)]
for i in b:
    k.append(i)

k+=["0" for i in range(al)]
jk = "".join(k)

realbl = al*2+bl

mindis = realbl


for i in range(realbl-al+1):
    for j in range(al):
        if int(a[j])+int(jk[i+j])<4 or jk[i+j]=="0":
            pass
        else:
            break
    else:
        #print((" "*i)+a)
        #print(jk)
        #i가 al보다 크면 원래 것 부터 더함
        # 아니면 i+al이랑 al-i+bl이랑 더 긴거로 정함
        if i>bl:
            if i<al:
                print(al)
                exit()
            else:
                #print(i)
                mindis = min(mindis,i)
                
            
            
        else:
            mindis = min(mindis,max(i+al-bl,al-i+bl))
            #print(max(i+al-bl,al-i+bl),1)
print(mindis)



















        
