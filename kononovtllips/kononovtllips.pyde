x = 200
y = 300
t = 200
h = 300
r = 200
l = 300
f = 200
a = 300
def setup():
    size(400,600)
    frameRate(2)
    background(0,0,0)
def draw():
    global x,y,t,h,r,l,f,a
    strokeWeight ( 10)
    stroke ( random ( 0,255 ),random ( 0,255),random ( 0,255))
    ellipse(x,y,20,20)
    x = x + 1
    y = y + 1
    stroke ( random ( 0,255 ),random ( 0,255),random ( 0,255))
    ellipse(t,h,20,20)
    t = t - 1
    h = h + 1
    stroke ( random ( 0,255 ),random ( 0,255),random ( 0,255))
    ellipse(r,l,20,20)
    r = r + 1
    l = l - 1 
    stroke ( random ( 0,255 ),random ( 0,255),random ( 0,255))
    ellipse(f,a,20,20)
    f = f - 1
    a = a - 1
