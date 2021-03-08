# imports (SmallTalk LIBrary)
from stlib.scene import MainHeader, ContactHeader
from stlib.visuals import ShowGrid
from stlib.physics import Floor
from stlib.physics import Cube

def createScene(rootNode):
  MainHeader(rootNode, grvaity=[0.0,-981.0,0.0])
  
  ContactHeader(rootNode, alarmDistance=8,
               contactDistance=5)

  ShowGrid(rootNode)
  
  
  
  
  
  
  return rootNode
