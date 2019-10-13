
# coding: utf-8

# In[5]:


_selection = ('1','2','3','4')
_result = 0

while True:
    print("===========")
    print("1.查询余额")
    print("2.存款")
    print("3.取款")
    print("4.退出")
    print("===========")
    _temp = input("请选择需要的操作：")
    if _temp and _temp != '4':
        if _temp in _selection:
            if _temp == '1':   
                print("余额为：",_result)       
            elif _temp =='2':
                _result =_result + float(input("存入金额："))
                print('账户金额：',_result)
            elif _temp =='3':
                _qukuan =float(input("请输入要取的金额："))
                if _qukuan>_result:
                    print('余额不足！余额: ',_result)
                else:
                    _result-=_qukuan
                    print('剩余金额：',_result)
        else:
            print("输入1到4之间数字")
        _temp = ''
        
    if _temp == '4':
        break;
    

