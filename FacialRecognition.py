import cv2

class FacialRecognition:
  def __init__(self):
    self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    self.video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    self.faces = []

  def size(self):
    return (
      int(self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
      int(self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    )

  def release():
    video_capture.release()
    cv2.destroyAllWindows()

  def getFaces(self):
    _, self.frame = self.video_capture.read()
    self.faces = self.faceCascade.detectMultiScale(
      cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY),
      scaleFactor=1.1,
      minNeighbors=5,
      minSize=(30, 30),
      flags=cv2.CASCADE_SCALE_IMAGE
    )
    return self.faces

  def showImage(self):
    fw, fh = self.size() #frame width and height
    cv2.circle(self.frame, (int(fw/2), int(fh/2)), 2, (0, 0, 255), 1)
    for (x, y, w, h) in self.faces:
      cv2.rectangle(self.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
      cv2.circle(self.frame, (int(x+w/2), int(y+h/2)), 4, (255, 0, 0), 2)
        
    cv2.imshow('Video', self.frame)