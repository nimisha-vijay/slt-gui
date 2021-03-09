import cv2


camera = cv2.VideoCapture(0)

fr = 0

while fr < 1000:
	ret, frame = camera.read()
	fr += 1
	print(fr)
	cv2.imshow("Sign Language Translator",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
camera.release()
cv2.destroyAllWindows()