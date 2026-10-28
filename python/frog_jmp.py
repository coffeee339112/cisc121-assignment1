# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # Implement your solution here
    T=0#state the variable T equals to zero
    if X>=Y:#if the frog already at or beyond the target, the frog do not need to jum so the step is zero
        return T
    while True:#this function will always run until the frog gets the target
        X=X+D#calculate where the frog is
        T=T+1#calculate how many times the frog jumped
        if X>=Y:#if the frog gets or exceeds the target, return how many steps the frog used and stop the function
            return T
    
