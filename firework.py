import numpy as np
import cv2 as cv


class FireWork:
    def __init__(self, v0: list, r0: list, windowSize: list, r= 4) -> None:
        self.vx= v0[0]
        self.vy= v0[1]
        self.x= r0[0]
        self.y= r0[1]
        self.ax= 0
        self.ay= 0
        self.windowWidth= windowSize[0]
        self.windowHeight= windowSize[1]
        self.r= r
        self.color= list(
            cv.cvtColor(
                np.array(
                    [[[np.random.randint(0, 256),255,255]]],
                    np.uint8
                ),
                cv.COLOR_HSV2BGR_FULL
            )[0][0]
        )

    def applyAcceleration(self, a: list):
        self.ax += a[0]
        self.ay += a[1]

    def update(self, walls= True):
        self.x += self.vx
        self.y += self.vy
        self.vx += self.ax
        self.vy += self.ay
        if walls:
            if self.x <= 0 or self.x >= self.windowWidth: self.vx = -self.vx
            if self.y <= 0 or self.y >= self.windowHeight: self.vy= -self.vy

    def draw(self, canvas: np.array):
        b= int(self.color[0])
        g= int(self.color[1])
        r= int(self.color[2])
        cv.circle(canvas, (int(self.x), int(self.y)), self.r, (b, g, r), -1)
