def legal(a):
    for i in range(len(a)):
        if a[i]!=a[i-1]:
            return False
    return True
    

def Subset(a,k):
    if k==0:
        return True
    sums = [0]*k
    return Subset_aux(a,sums,k,len(a)-1)


def Subset_aux(a,sums, k,n):
    if legal(sums) and n<0:
        return True
    if not legal(sums) and n<0:
        return False
    for i in range(k):
        sums[i] = sums[i]+a[n]
        if Subset_aux(a,sums, k,n-1)==True:
            return True
        sums[i] = sums[i]-a[n]
    return False

# The problem could be solve by thinking about the k set as cells
# Each time we will add a element to a cell from the array
# if not all the cells sums are equal and we reached the end of the array then we call the stack for n+1  
# we will keep calling the stack and try all different option
# if non of them gives equal cell then we return false, otherwise true


a = [3,1,2,5,-2]
print(Subset(a,3))
