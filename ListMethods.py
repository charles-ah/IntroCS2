def sum3(nums):
      sum = 0
      x = 0
      while x < len(nums):
          sum = sum + nums[x]
          x = x + 1
      return sum

  
def removeValuesFromXtoYList(L,x,y):
    counter = 0
    newL = []
    while counter < len(L):
        if L[counter] > x and L[counter] < y:
            counter = counter + 1
        else:
            newL = newL + [L[counter]]
            counter = counter + 1
    return newL

L=[ 1, 3, -5, 10, -2, 0, -6.0, 0 , 1]
print removeValuesFromXtoYList(L,-3,3)

def moveNegativeToEnd(L):
    x = 0
    negL=[]
    while x <len(L) - 1:
        if L[x] < 0:
            negL = negL + L[x]
            x=x+1
        else:
            x=x+1
    
            
def first_last6(nums):
      if nums[0] == 6 or nums[-1] == 6:
            return True
      else:
            return False

def same_first_last(nums):
      if nums[0] == nums[-1]:
            return True
      else:
            return False

def count_evens(nums):
      x = 0
      counter=0
      while x < len(nums):
            if nums[x]%2==0:
                  counter=counter+1
                  x=x+1
            else:
                  x=x+1
      return counter

def big_diff(nums):
      x=0
      while x<len(nums):
            
      
