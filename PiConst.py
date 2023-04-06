#Original
class ConstantError(Exception):
  pass
 
def Search(name=str,filename=str):
   f= open(filename,'r')
   while True:
    line=str(f.readline())
    if not line:
      break
    if f"{name}" in line and "=" in line and not "if" in line and not "Const(" in line:
      raise ConstantError("Value can't be changed!")
    else: pass
def Take_Variable(string=str,filename=str):
  variable=string[0:int(string.find("="))]
  Search(variable,filename) 
def Read_File(Filename):
  f= open(Filename,'r')
  while True:
    line=str(f.readline())
    if not line:
      break
    if "Const(" in line:
      Take_Variable(line,Filename)
       
class Const():
  def __init__(self,value,filename=str):
    Read_File(filename)
    self.const=value
