# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    if len(A) == 0: #if the A is empty, stop the function and return A. 
        return A
    while K: #repeat if the K do not equal to 0
        last=A.pop()#delete the last element of A and store it as "last"
        A.insert(0,last)# insert the element that we delete 
        K=K-1#every time the K will minus 1 so that it will repeat just K times
    return A 
