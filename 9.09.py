##
##该程序用二分法求函数根，无论函数递增或递减均使用
import numpy as np
def h(x1):
    f=np.sin(3.14 * x1) * 2 + np.cos(3.14 * x1)
    # f=-x1+1/2   ##递增函数
    # f=x1-1/2     ##递减函数
    return f
while(True):
    a=float(input('请输入左端点值：'))
    b=float(input('请输入右端点值：'))
    equ=float(input('请输入精度：'))
    k=0
    if h(a)*h(b)>0:
        print("please enter others number:")
    else:
       while (True):
         if h(a)*h(b)==0.0:
            if h(a)==0.0:
               print(a,k)
            else:
               print(b,k)
            break
         else:
            m=(a+b)/2
            if abs(b-a)<equ:
               print(m,k)
               break
            else:
               if h(a)*h(m)>0:
                 a=m
               else:
                  b=m
               k=k+1
