import cv2, time

video=cv2.VideoCapture(0)#it capture the video
a=0
while True:
	a=a+1
	check, fram=video.read()#It capture the video dimension 

	print(check)
	print(fram)
	#time.sleep(3)
	 
	cv2.imshow("Capture",fram)

	k=cv2.waitKey(1)
	if k==ord('q'):#when we press q then stop video.
		break;
print(a)#here print number of frame in  pics. capture
video.release()
cv2.destroyAllWindows()