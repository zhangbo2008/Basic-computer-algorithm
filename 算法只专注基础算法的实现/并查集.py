# -*- coding: utf-8 -*-
'''并查集(Union-Find)算法详解'''
##原始地址下面,写的很好
'''https://www.cnblogs.com/learnbydoing/p/6896472.html?utm_source=itdadao&utm_medium=referral'''
class QuickFind(object):
    id=[]#n给多少就产生多少个id,从0到n-1这n个id
    count=0
    #下面函数就是生成id而已
    def __init__(self,n):
        self.count = n
        i=0
        while i<n:
            self.id.append(i)
            i+=1
    #判断2个id是否相连的函数
    def connected(self,p,q):
        return self.find(p) == self.find(q)
    
    def find(self,p):    
        return self.id[p]
    #下面就是并查集的核心代码!union函数
#union函数理解:把p,q这2个index对应的点进行相连,那么就等价于
    def union(self,p,q):
        idp = self.find(p)#这地方需要先记录一下self.find(p)因为一会儿要复制改变数组,这个等式右边会变化.
        if not self.connected(p,q):
            for i in range(len(self.id)):
                if self.id[i]==idp: # 将p所在组内的所有节点的id都设为q的当前id,显然每一次union的复杂度是O(N).
                                    #算法也不是很快,但是也基本上没有更快的了.log(N),感觉好像存在.每一次用二分方法来查找
                                    #替代这个for循环.
#即表示把所有跟p相连的都改成q的id,
#这个步奏很叼,可以把union(p,q) 等效于union(q,p).证明很显然,因为你把所有是p的都改成q,跟把所有是q的都改成p是一样的.
                    self.id[i] = self.id[q]

            self.count -= 1
            #count来输出最后这个set分成多少个不相交的集合.
    

# -*- coding: utf-8 -*-



qf = QuickFind(10)



print ("initial id list is %s" % (",").join(str(x) for x in qf.id))

list = [
        (4,3),
        (3,8),
        (6,5),
        (9,4),
        (2,1),
        (8,9),
        (5,0),
        (7,2),
        (6,1),
        (1,0),
        (6,7)
        ]

for k in list:
    p =  k[0]
    q =  k[1]
    #把p,q进行union操作
    qf.union(p,q)
    print ("%d and %d is connected? %s" % (p,q,str(qf.connected(p,q)    )))
    
print ("final id list is %s" % (",").join(str(x) for x in qf.id))
print ("count of components is: %d" % qf.count)
#从下面打印可以看出来相同的元素对应的id也是相同的.就是通过union函数实现的这个功能.
print (qf.id)









