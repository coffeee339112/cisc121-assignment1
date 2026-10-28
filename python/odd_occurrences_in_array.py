# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    counts={}#create a empty dictionary named counts
    for i in A:
        if i in counts:#if the dictionary has that value
            counts[i]=counts[i]+1#the appear times of that value plus one
        else:#if the dictionary do not have that value
            counts[i]=1#insert that value t the dictionary and set it appears one time
    for i,count in counts.items():#give the value in counts to i and give how many times that the value appears to count
        if count%2==1:#if the value appears the odd times
            return i#return that value
