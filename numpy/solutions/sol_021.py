def Theta(x):
    """
    Vector-aware implemenation of the Heaviside step function.
    """
    return 1 * (x >= 0)
    
## Testing the function
print(Theta(array([-3,-2,-1,0,1,2,3])))

# and also works with scalars as well
print(Theta(-1.2), Theta(2.6))