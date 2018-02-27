'''快速排序'''
'''我最新理解是,给数组头和尾两个指针,
然后分别向中间跑,如果发现逆序就交换,一直交换到指针相碰就停止就写好了fenge函数'''
#关键就是这个分割函数的写法
def fenge(a):
      left=0
      right=len(a)-1
      tmp=a[0]#tmp就是分割的点的值
      for i in range(len(a)):
            if left==right: #主体思想是2重循环来写,然后每一个循环都先加入break条件.
                  break
            while 1:
                  if left==right:
                   break
                  if a[right]<tmp:  #如果有反序就交换过来
                        
                        a[right],a[left]=a[left],a[right]
                        break
                  else:
                        right-=1
            while 1:           #更上面完全类似了.
                  if left==right:
                   break
                  if a[left]>tmp:
                        
                        a[right],a[left]=a[left],a[right]
                        break
                  else:
                        left+=1
      
      return a,left    
def sort(a):
      if len(a)==0:
            return []
      if len(a)==2:
            if  a[0]>a[1]:
                  return [a[1],a[0]]
            else:
                  return a
      if len(a)==1:
            return a
      a,left=fenge(a)
      #[a[left]]把一个数变成数组
      return sort(a[:left])+[a[left]]+sort(a[left+1:])
a=[34,57,4,101,5,97,99,234,3423423]
import random
a=range(1,1000)
a=list(a)
random.shuffle(a)

print (sort(a)[:100])#百万级别还是有点慢大概10s不到的样子
