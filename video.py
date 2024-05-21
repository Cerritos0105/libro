import cv2
import numpy as np
camara = cv2.VideoCapture(0)
videopro=cv2.VideoWriter('SalidaVideo.avi',cv2.VideoWriter_fourcc(*'XVID'),30.0, (640,480))
while(camara.isOpened()):
    r,img=camara.read()
    if r ==True:
        cv2.imshow("Video pro", img)
        videopro.write(img)
        if cv2.waitKey(1) ==ord('p'):
            break
camara.release()
cv2.destroyAllWindows()
