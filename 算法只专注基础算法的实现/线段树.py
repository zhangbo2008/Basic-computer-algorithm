#线段树:线段树的基本定义:线段树是解决数列维护问题的一种常用手段.基本能保证每一个操作
#的复杂度都是O(logn)的级别.而我们知道正常一个数组的查询是需要O(n)的也就是遍历.
'''所以当n的级别很大到10亿以上,如果我们还需要1s内解决问题就需要用线段树来查询和修改'''
'''对于二叉树而言:n0表示叶子节点的数目,n1为度为1的节点数目,n2为度为2的节点数目,
边的数目S=n1+2*n2'''
'''度为0的节点数比度为2的节点数多1:证明:首先二叉树中子树的节点有n1+2n2个,所以二叉树的
总共节点数是1+n1+2n2,另外一种是n0+n1+2n2,所以证毕,并且也知道一个结论是二叉树的
节点数比边数多1'''
'''利用上面2个结论我们知道线段树这个2叉树的节点数目是2n-1'''


'''线段树处理这样的问题:
把问题简化一下：

在自然数，且所有的数不大于30000的范围内讨论一个问题：现在已知n条线段，把端点依次输入告诉你，然后有m个询问，每个询问输入一个点，要求这个点在多少条线段上出现过；

最基本的解法当然就是读一个点，就把所有线段比一下，看看在不在线段中；

每次询问都要把n条线段查一次，那么m次询问，就要运算m*n次，复杂度就是O(m*n)

这道题m和n都是30000，那么计算量达到了10^9；而计算机1秒的计算量大约是10^8的数量级，所以这种方法无论怎么优化都是超时

—–

因为n条线段是固定的，所以某种程度上说每次都把n条线段查一遍有大量的重复和浪费；

线段树就是可以解决这类问题的数据结构

举例说明：已知线段[2,5] [4,6] [0,7]；求点2,4,7分别出现了多少次'''

'''http://hzwer.com/670.html
下面我写的不清楚就继续看上面这个url,又是一个不懂感觉很神秘,懂了感觉很平凡的东西.发明的
人还是吊.
这个网址上面的题目和代码,从他的分析可以看出
用线段树把原来O(mn) 的算法变成了O(mlog30000+nlog30000)   的算法,m和n也都取成3万,
那么我们有左边是10亿右边是几十万,这就是线段树的快捷地方,他快捷的本质是其实不用每一次都
重新问一个数字是否在一个线段里面,而只需要把线段的信息都一次储存好,然后直接询问每一个
要找的数字即可'''

#下面开始实现这个问题
#每一个节点
class jiedian:
      def __init__(self,start,end):
            self.start,self.end=start,end
            self.left,self.right=None,None
            self.count=0#在这个题目里面作为计数的工具使用
#创立这个二叉树,我们问题里面start就是0,end就是30000,因为是线段
#所以需要包含端点,0是自然数.
def build(start,end):
      if start>end:
            return None
      root=jiedian(start,end)
      if start==end:
            return root
      root.left=build(start,(start+end)//2)
      root.right=build((start+end)//2+1,end)
      return root
#下面我们就开始创立我们的简单例子里面[0,7]这个线段树.
a=build(0,7)

#下面我们写一个把一个区间插入到线段树里面的函数,然后把对应的拆分的count+1
#对于插入的区间要分类讨论,比如我插入一个[-99,0]的这种不合逻辑的也需要加强程序鲁邦性.
def charu(root,start,end):#用函数的封装root来实现迭代
            if start<root.start:
              start=root.start
            if end >root.end:
              end=root.end
            if root.start==start and root.end==end:
                  root.count+=1
                  return 
            if root.start>end:
                  return 
            if root.end<start:
                  return 
            if end<=root.left.end:
                  charu(root.left,start,end)
            if start>=root.left.end+1:
                  charu(root.right,start,end)
##charu(a,-99,99)
##print (a.count)#经过实验这里面成功输出1这个数字.基本上讨论了所有情况.
#下面写查询代码即可,相类似.因为这个题目只是每一次找一个数字不是区间所以比上面更容易一点.
def chaxun(root,obj):
      if obj>root.end:
            return 0
      if obj<root.start:
            return 0
      if obj==root.start==root.end:
            return root.count
      if obj<=(root.start+root.end)//2:
            return chaxun(root.left,obj)+root.count
      if obj>=(root.start+root.end)//2+1:
            return chaxun(root.right,obj)+root.count
#下面开始重头插入和查询
charu(a,-99,0)
charu(a,-99,0)
charu(a,-99,0)
charu(a,-99,0)
charu(a,-99,1)
answer=chaxun(a,1)
print (answer)
                  


      
      




























