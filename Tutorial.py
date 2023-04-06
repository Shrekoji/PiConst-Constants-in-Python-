#This code is just an example of how to use this module
from PiConst import Const
a=Const(2,'Tutorial.py') #You have to Provide the name of the file while declaring any constant.If u can fix it then Congratulations! 

 # a=3 Will throw an error
'Not use "#" Because qutotaions will throw errors '
print(a.const)#Do stuff with the value
if(a.const==0):
    print("Hi")