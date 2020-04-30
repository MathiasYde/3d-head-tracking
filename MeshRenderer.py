import pygame as pg
from pygame.locals import *
import math

from OpenGL.GL import *
from OpenGL.GLU import *

class Mesh:
  def __init__(self, vertices=[], triangles=[]):
    self.vertices = vertices
    self.triangles = triangles

  def render(self):
    """Calls OpenGL functions to render this mesh"""
    for triangle in self.triangles:
      glBegin(GL_TRIANGLES)
      for vertex_index in triangle:
        x, y, z = self.vertices[vertex_index-1]
        glVertex3f(x, y, z)
      glColor3fv((x, y, z))
      glEnd()

class MeshRenderer:
  def __init__(self, mesh=Mesh(), size=(800,800)):
    self.size = size
    self.mesh = mesh

    self.rotation = [0, 0, 0]
    
    pg.init()
    pg.display.set_mode(size, DOUBLEBUF|OPENGL)
    gluPerspective(45, (size[0]/size[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0,-6.0)

    glEnable(GL_DEPTH_TEST)

  @staticmethod
  def readObjFile(file):
    """Read a .obj file and parse it into a Mesh() object"""
    mesh = Mesh()

    with open(file, "r") as lines:
      for line in lines:
        sections = line.split()

        if sections[0] == "v":
          mesh.vertices.append([float(sections[1]), float(sections[2]), float(sections[3])])

        if sections[0] == "f":
          face = [
            int(sections[1].split("/")[0]),
            int(sections[2].split("/")[0]),
            int(sections[3].split("/")[0])
          ]
          mesh.triangles.append(face)
    return mesh
  
  def run(self):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        quit()

    glPushMatrix()
    glRotatef(self.rotation[0], 1, 0, 0)
    glRotatef(self.rotation[1], 0, 1, 0)
    glRotatef(self.rotation[2], 0, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    self.mesh.render()
    glPopMatrix()

    pg.display.flip()


if __name__ == "__main__":
  #Basic usage
  mesh = MeshRenderer.readObjFile("monkey.obj")
  renderer = MeshRenderer(mesh=mesh, size=(600,600))

  t = 0
  while True:
    renderer.run()

    renderer.rotation = [
      math.sin(t)*40,
      math.cos(t)*40,
      0
    ]
    t += 0.03