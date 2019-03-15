import cv2
cup_cascade = cv2.CascadeClassifier('images/data/cascade.xml')

def createTrackerByID(trackerType):
	tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
	# Create a tracker based on tracker name
	if trackerType == 0:
		tracker = cv2.TrackerBoosting_create()
	elif trackerType == 1:
		tracker = cv2.TrackerMIL_create()
	elif trackerType == 2:
		tracker = cv2.TrackerKCF_create()
	elif trackerType == 3:
		tracker = cv2.TrackerTLD_create()
	elif trackerType == 4:
		tracker = cv2.TrackerMedianFlow_create()
	elif trackerType == 5:
		tracker = cv2.TrackerGOTURN_create()
	elif trackerType == 6:
		tracker = cv2.TrackerMOSSE_create()
	elif trackerType == 7:
		tracker = cv2.TrackerCSRT_create()
	else:
		tracker = None
		print('Incorrect tracker name')
		print('Available trackers are:')
		for t in trackerTypes:
			print(t)
	return tracker


class Worker(object):
	def __init_tracker__(self):
		self.bbox = cv2.selectROI(self.image, False)
		self.tracker = createTrackerByID(2)
		self.tracker.init(self.image, self.bbox)

	def __init__(self):
		self.cam = cv2.VideoCapture(0)
		self.stream = self.capture_video()
		self.image = next(self.stream)

	def capture_video(self):
		while(True):
			ret, frame = self.cam.read()
			if ret:
				yield frame

	def next_slide(self):
		self.image = next(self.stream)
		gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
		cups = cup_cascade.detectMultiScale(gray,50,50)
		for (x,y,w,h) in cups:
			cv2.rectangle(self.image,(x,y),(x+w,y+h),(255,255,0),2)

	def show(self):
		cv2.imshow('frame',self.image)

	def __del__(self):
		self.cam.release()
		cv2.destroyAllWindows()

	def track(self):
		timer = cv2.getTickCount()
		# Update tracker
		ok, self.bbox = self.tracker.update(self.image)
		# Draw bounding box
		if ok:
			# Tracking success
			p1 = (int(self.bbox[0]), int(self.bbox[1]))
			p2 = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))
			cv2.rectangle(self.image, p1, p2, (255,0,0), 2, 1)
		else:
			#TODO insert moment into database
			print ("lost an object")

worker = Worker()
while(True):
	worker.next_slide()
	worker.show()

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
