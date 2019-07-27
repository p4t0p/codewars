def is_odd(n):
    return n % 2 == 1
    
def odd_count(n):
    if is_odd(n):
        return(n-1)/2
    else:
        return n/2 
    