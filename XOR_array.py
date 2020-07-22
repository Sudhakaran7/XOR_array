arr=list(map(int,input().split()))
res=[]
for i in range(len(arr)):
  for j in range(i+1,len(arr)):
    val=arr[i]^arr[j]
    res.append(val)
res.sort()
print(max(res))
