#MOTION DETECTOR
#press 's' to exit from frame
import cv2,time,pandas
from datetime import  datetime
init_frame = None
motion_list = [ None, None]
time = []
df = pandas.DataFrame(columns=['start','end'])
video = cv2.VideoCapture(0)

while True:
    check,frame = video.read()
    motion = 0

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if init_frame is None :
        init_frame = gray
        continue
    diff_fr = cv2.absdiff( init_frame,gray)
    thres = cv2.threshold(diff_fr,30,255,cv2.THRESH_BINARY)[1]
    thres = cv2.dilate(thres , None , iterations = 2)

    contours, hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
         if cv2.contourArea(contour) < -5:
             continue
         motion = 1
         (x,y,w,h) = cv2.boundingRect(contour)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    motion_list.append(motion)
    motion_list = motion_list[-2:]

    if motion_list[-1:]==1 and motion_list[-2:]==0:
         time.append(datetime.now())
    if motion_list[-1:]==0 and motion_list[-2:]==1:
         time.append(datetime.now())

    cv2.imshow("color", frame)
    #uncommeneting these lines of code gives different frames also
    #cv2.imshow("diff",  diff_fr)
    #cv2.imshow("gray",  gray)
    #cv2.imshow("thresh",thres)

    key = cv2.waitKey(1)
    if key == ord('s'):
         if motion == 1:
             time.append(datetime.now())
         break

for i in range(0,len(time),2):
    df=df.append({'start': time[i],'end': time[i+1]},ignore_index= True)

video.release()
cv2.destroyAllWindows()