
# coding: utf-8

# In[5]:


incomelist=[]
paylist=[]
getdic={}
i = 0
j = 0
_sum = 0
while i<7:
    i=i+1
    incomelist.append(input('Please input income of '+ '%d'%i +' Days:'))
    
while j<7:
    j = j+1
    paylist.append(input('Please input payment of '+ '%d'%j +' Days:'))
i = 0
while i<7:
    getdic[i]=float(incomelist[i])-float(paylist[i])
    i = i + 1
for each in getdic:
    _sum = each + _sum

print(incomelist)
print(paylist)    
print(getdic)
print('7天总收入：',_sum)

