# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    L=len(A)+1
    i1=[]
    for i in range(1,L+1):#find all variables if there's no missing variable
        i1.append(i)#make the variables as a list
    for x in i1:#get all variables in i1
        if x not in A:#compare which variable is at ii but not in a
            return x
