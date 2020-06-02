import cv2,time
video = cv2.VideoCapture("E:\\smart.mp4")
a=1
def  rec():
  while True:
       global a
       a= a+1
       check,frame= video.read()
       print(frame)
       cv2.imshow("legends" , frame)
       key = cv2.waitKey(1)
       if key == ord('s'):
           check=False
           break


fun = rec()
print(a)
video.release()
cv2.destroyAllWindows()