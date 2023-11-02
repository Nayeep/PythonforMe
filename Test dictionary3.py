Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao1 = turtle.Pen()
tao1.shape('turtle')
t1dict = {'color':'green','dis':100}
t2dict = {'color':'red','dis':50}
t3dict = {'color':'pink','dis':150}
def drawrect(tao,tdict):
...     for i in range(4):
...         tao.forward(tdict['dis'])
...         tao.left(90)
... 
...         
>>> drawrect(tao1,t1dict)
>>> drawrect(tao1,t2dict)
>>> def drawhexa(tao,tdict):
...     for i in range(6):
...         tao.color(tdict['color'])
...         tao.forward(tdict['dis'])
...         tao.left(60)
... 
...         
>>> drawhexa(tao1,t1dict)
>>> drawhexa(tao1,t2dict)
>>> drawhexa(tao1,t3dict)
print(t1dict)
print('Hello world')



