def convert(s,f,t,n=0,r='',x='abcdefghijklmnopqrstuvwxyz'):
    a='0123456789'+x+x.upper()
    for e in s:n=n*f+a.find(e)
    while n:r,n=a[n%t]+r,n//t
    return r or'0'
  
