class Solution:
    def mergeArrays(self, a, b):
        # code here
        length = len(a)
        length_b= len(b)
        a.extend(b)
        a.sort()
        
        idx = 0
        while(idx<length_b):
            b[idx]=a[idx+length]
            idx+=1
        del a[length:]
