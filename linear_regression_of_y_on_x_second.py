import numpy as np

def regression_line(x, y):
    """ Return the a (intercept)
        and b (slope) of Regression Line
        (Y on X).
    """
    a,b = np.polyfit(x,y,1)
    return round(b,4),round(a,4)


print(regression_line([25,30,35,40,45,50], [78,70,65,58,48,42]))
print(regression_line([56,42,72,36,63,47,55,49,38,42,68,60], [147,125,160,118,149,128,150,145,115,140,152,155]))