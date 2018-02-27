#主要关注边界值的问题
def binsear(obj,li,left,right):
      if right-left==1:
            if li[left]==obj:
                  return left
            if li[right]==obj:
                  return right
            return None
      if right-left==0:
            if li[left]==obj:
                  return left
            
            return None
      if li[(left+right)//2]==obj: #//才是之前的整数除法
             return (left+right)//2
      if li[(left+right)//2]<obj:
             return binsear(obj ,li,(left+right)//2+1,right)
      if li[(left+right)//2]>obj:
             return binsear(obj ,li,left,(left+right)//2)
daan=binsear(1,[1],0,0)
print (daan)
#话说我是有点强啊,一次写完直接跑一次就成功.
