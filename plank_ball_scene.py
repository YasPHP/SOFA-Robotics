# imports
from stlib.scene import MainHeader
from stlib.solver import DefaultSolver
from stlib.physics.rigid import Floor


def createScene(rootNode):
  
  MainHeader(rootNode, gravity=[0.0, -981.0, 0.0])
  
  cube = rootNode.createChild("Cube")
  

