a = 300
def setup():
    size(400,400)
    #frameRate(2)
def draw():
     global a
     ellipse (200,200,a,a)
     stroke ( random ( 0,255 ),random ( 0,255),random ( 0,255))
     a = a - 1
     if a == 0:
         noLoop()
     
    
