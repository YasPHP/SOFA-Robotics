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
  
  Floor(rootNode,
       translation=[0.0,-180.0,0.0],
       uniformScale=5.0,
       isAStaticObject=True)
  
  Floor(rootNode,
        name="Floor Obstacle",
        translation=[0.0,-90.0,0.0],
        color=[0.0,1.0,0.0],
        uniformScale=0.8,
        isAStaticObject=True)
  
  
  
  
  return rootNode
