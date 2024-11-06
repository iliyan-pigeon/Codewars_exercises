def find_the_crossing(a, b, c, d):
    if a == b or c == d:
        return # tuples must be different to make a line
    dx1, dy1 = (y-x for x,y in zip(a,b))
    dx2, dy2 = (y-x for x,y in zip(c,d))
    if dy1*dx2 == dy2*dx1:
        return # lines are parallel
    x = (dx2*dy1*a[0] - c[0]*dx1*dy2 + (c[1]-a[1])*dx2*dx1)/(dx2*dy1 - dx1*dy2)
    y = dy1/dx1*(x-a[0])+a[1] if dx1 else dy2/dx2*(x-c[0])+c[1]
    return x,y
  
