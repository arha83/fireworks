import numpy as np
import cv2 as cv
import time
from firework import FireWork

def randomFireworks(x: int, y: int, n: int):
    fireworks= []
    for i in range(n):
        angle= np.random.rand()*2*np.pi
        magnitude= np.random.rand()*1.5
        v0= [magnitude*np.cos(angle), magnitude*np.sin(angle)]
        f= FireWork(v0, [x,y], [windowWidth,windowHeight], 2)
        fireworks.append(f)
    return fireworks

    


windowWidth= 800
windowHeight= 600

firework= FireWork([0.5,-2], [windowWidth//4,windowHeight], [windowWidth,windowHeight])
firework.applyAcceleration([0, 0.005])
fireworks= []
# fireworks= randomFireworks(windowWidth//2, windowHeight//2, 1000)
# for f in fireworks:
#     f.applyAcceleration([0, 0.005])
canvas= np.zeros((windowHeight, windowWidth, 3), np.uint8)
tic= time.time()
while True:
    canvas= (canvas.astype(np.float64)*245/255).astype(np.uint8)

    if firework:
        firework.draw(canvas)
        firework.update()
        if firework.vy > 0:
            fireworks= randomFireworks(firework.x, firework.y, 500)
            for f in fireworks:
                f.applyAcceleration([0, 0.005])
            firework= None

    for f in fireworks:
        f.draw(canvas)
        f.update(False)


    # # toc= time.time()
    # # try: cv.putText(canvas, str(int(1/(toc-tic))), (3, 14), cv.FONT_HERSHEY_COMPLEX, (0.5), (0,255,0), 1)
    # # except: cv.putText(canvas, 'a lot', (3, 14), cv.FONT_HERSHEY_COMPLEX, (0.5), (0,255,0), 1)
    # tic= toc
    cv.imshow('canvas', canvas)
    if cv.waitKey(1) == ord('q'): break

cv.destroyAllWindows()