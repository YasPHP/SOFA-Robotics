# imports (SmallTalk LIBrary)
from stlib.scene import MainHeader, ContactHeader
from stlib.visuals import ShowGrid
from stlib.physics import Floor
from stlib.physics import Cube
from stlib.solver import DefaultSolver

# create a scene with a root node
def createScene(rootNode):

  # main header (rootNode + gravity)
  MainHeader(rootNode, gravity=[])
  
  # contact header
  ContactHeader(rootNode, alarmDistance=0,
               contactDistance=)

  # shows the grid outline
  ShowGrid(rootNode)
  
  # base floor
  Floor(rootNode,
       translation=[],
       uniformScale=0.0,
       isAStaticObject=True)
  
  # obstacle floor
  Floor(rootNode,
        name="Floor Obstacle",
        translation=[],
        color=[],
        uniformScale=0.0,
        isAStaticObject=True)
  
  # creates cubes
  for i in range(0):
    Cube(rootNode,
         name=,
         translation=[],
         color=[],
         uniformScale=0.0)
    
    
   # creating children (ie. a cube) for the root node
  
    cube = rootNode.createChild("Cube")

    
    
    
    
    
    
    
    
    
    
    
  
  return rootNode
