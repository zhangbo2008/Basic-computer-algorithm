'''堆的定义:
堆是一种特殊的树形数据结构，每个节点都有一个值，
通常我们所说的堆的数据结构指的是二叉树。堆的特点是根节点的值最大（或者最小）'''
'''那么我们为什么要用堆而不用list呢,因为堆的插入查找,特别是查找前n个大的元素,
这些操作都是log(N)的,而list是O(N)的'''
'''heapq这个模块是最小堆的实现
heap = [] #创建了一个空堆 
heappush(heap,item) #往堆中插入一条新的值 
item = heappop(heap) #从堆中弹出最小值 
item = heap[0] #查看堆中最小值，不弹出 
heapify(x) #以线性时间讲一个列表转化为堆
#!!然后像数组一样用下表来访问就行了,下面是2个更封装的方法
    nlargest(n, iterable, key=None)
        Find the n largest elements in a dataset.
        
        Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]
    
    nsmallest(n, iterable, key=None)
        Find the n smallest elements in a dataset.
        
'''
'''用上面这些命令来做堆就够了,当然是从实用方面讲'''
from heapq import *
a=[1,23,2,13,2,4,32,432,4,2]

heapify(a)
print (a)#这时候打印就知道了,a还是一个list的类型,但是他已经是一个
#heap排列的数组了.本质上还是heap.
heappush(a,9999)
print (a[3]) #访问第四小
print (a[-1])#访问最大.
print (type(a))
print (nsmallest(3,a))#打印前3个最小的
#堆的缺陷:他不是稳定的算法.堆里面元素的波动太大了,都是块的移动.
'''下面进行改进把他改成稳定的算法'''
b = [(1,1),(1,2),(1,-1),(1,-2131),(2,34234),(543,4534),(1,1342),(1,5461),(1,1342),(1,5461),(1,1342),(1,5461),]

shuchu=nsmallest(len(b),b,key=lambda x:x[0])
print (shuchu)
#经过实验python自带的堆排序也是稳定的.anyway,其实加一个索引就能让一个不稳定的排序变稳定.
#一个方法是建一个字典,然后扫一次list,遇到相同的才储存进去,也就是按照第一个元素去掉只有一次的.
#那么这个字典也就记录了第一个元素有重复的那些数据,然后堆排序之后,再从字典里面换就行了.
#但是这个建立字典速度很慢.先放着
'''下面手动写堆'''
'''做大根堆然后输出升序排列'''
'''https://www.cnblogs.com/chengxiao/p/6129630.html'''
def adjust(heap,heapsize,root):#root是这个数组其中一个角标
      
      left=2*root+1#首先得到左右的坐标
      right=left+1
      #需要判断left是否超过了数组长度,也就是是否有
      #左右kid
      larger=root
      
      if left<heapsize and heap[larger]<heap[left]:
            
            
            #larger表示变动的index
            larger=left
      if right<heapsize and heap[larger]<heap[right]:
            
            larger=right
      if larger!=root:
        heap[larger],heap[root]=heap[root],heap[larger]
        adjust(heap,heapsize,larger)#本质就是这里面只需要adjust一个,而不用adjust两个.做了二分所以是logn
                                    #那么为什么只需要一个adjust呢,因为下面sort函数是从下往上建立的
        　　　　　　　　　　　　　　　#每一次你adjust如果这个根子叔的root没变那么他是不用adjust的,因为下面层已经
                                   #在之前的for循环里面拍好了
       #上面这2步要递归因为破坏了下面的堆

def sort(heap):
      #倒着拍好堆,为什么要倒着拍.因为要让大的数一直上去,
      #所以要从下往上升才行.
      
      for i in range(len(heap)):
            j=len(heap)//2-1-i#最后一个非叶子节点开始,也就是for所有的有叶子的节点逆着走
            
            if j<0:
                  break
            adjust(heap,len(heap),j)
      
      #下面就是出数了,首先交换堆顶和堆尾
      for i in range(len(heap)):
            j=len(heap)-i-1
            
            if j<0:
                  break
            heap[0],heap[j]=heap[j],heap[0]
            adjust(heap,j,0)
      return heap

      
import copy
#下面做测试:
import random
a=range(10000)
a=list(a)

random.shuffle(a)




print (sort(a)[:100])





