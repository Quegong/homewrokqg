
# coding: utf-8

# In[25]:


incomelist=[]
paylist=[]
getdic={}
_Days = ('周一','周二','周三','周四','周五','周六','周日')
i = 0
j = 0
_sum = 0

while i<7:
    incomelist.append(input('Please input income of '+ _Days[i] +' Days:'))
    if not incomelist[i]:
          incomelist[i] = 0
    i = i+1
print(incomelist)

while j<7:
    paylist.append(input('Please input payment of '+ _Days[j] +' Days:'))
    if not paylist[j]:
          paylist[j] = 0
    j = j +1
    
i = 0
while i<7:        
    getdic[i]=float(incomelist[i])-float(paylist[i])
    i = i + 1
for each in getdic:
    _sum = each + _sum
j = 0    
for each in incomelist:    
    print(_Days[j]+'收入为：',each)
    j = j+1
j = 0
for each in paylist:    
    print(_Days[j]+'支出为：',each)
    j = j+1    
j=0
for each in getdic:
    print(_Days[j]+'结余：',getdic[each])

#print(incomelist)
#print(paylist)    
#print(getdic)
print('7天总收入：',_sum)


# ### 

# #### 

# ## 

# In[ ]:





# #### 
