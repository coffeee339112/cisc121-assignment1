# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A):
    # Implement your solution here
    a1=[]#create a empty list named a1
    a=len(A)
    for i in range(1,a+1):#get all varaibles of A if there's no missing variable
        a1.append(i)#make those variable in a list
    if a1==sorted(A):#determine wheather the list A is a permutation
        return 1
    else:
        return 0
