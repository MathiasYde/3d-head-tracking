import MeshRenderer as mr
import FacialRecognition as fr

mesh = mr.MeshRenderer.readObjFile("monkey.obj")
renderer = mr.MeshRenderer(mesh=mesh, size=(600,600))

facial = fr.FacialRecognition()
offset = facial.size()

pixelsPerDegree = 12

while True:
  faces = facial.getFaces()

  if (len(faces) >= 1):
    face = faces[0]

    fx, fy = int(face[0]+face[2]/2), int(face[1]+face[3]/2) #face x and y

    x = offset[0]/2-fx
    y = offset[1]/2-fy
    z = face[2]+face[3]/2

    renderer.rotation = [
      (y/pixelsPerDegree),
      -(x/pixelsPerDegree),
      0
    ]
    
    print(renderer.rotation)
  else:
    print("NO FACE FOUND")
  facial.showImage()
  renderer.run()

facial.release()