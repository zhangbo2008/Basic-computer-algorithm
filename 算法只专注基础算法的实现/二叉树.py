#二叉树的各种遍历的递归实现:
#深度:前序,后序,中序.和广度优先遍历.这么一共4中方法.
class node(object):
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
#深度遍历里面的前序遍历:把root放前面,所以遍历顺序是root,left,right
def front_depth(root):
      print (root.data)
      if root.left!=None:
       front_depth(root.left)
      if root.right!=None:
       front_depth(root.right)
aa=node(4)
bb=node(5)
a=node(2,aa,bb)
b=node(3)
root=node(1,a,b)

front_depth(root)
#成功输出12453
#其他后序,中序都类似.所以再写一个广度优先
print ('**********************')
def wide(root):
      #用数组来实现
      if type(root)!=list:
       root=[root]
       b=[]
      if type(root)==list:
       b=[]
      for i in root:
            print (i.data)
      for i in root:
            if i.left!=None:
             b.append(i.left)
            if i.right!=None: 
             b.append(i.right)
      if b!=[]:
       wide(b)

wide(root)
#输出了12345



            
            
