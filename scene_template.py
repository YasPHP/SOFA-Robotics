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

  # Mechanical Model
  
  totalMass = 0.0
  volume = 0.0
  inertiaMatrix = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
  
  # create an Object
  cube.createObject('ObjectName', name="name", 
                    template="Rigid", translation=[0.0, 0.0, 0.0], 
                    rotation = [0.0, 0.0, 0.0])
  
  # create a Uniform Mass Object
  cube.createObject('UniformMass', name="Mass", 
                    mass=[totalMass, volume, inertiaMatrix[:]])

  # Time Integration Scheme
  cube.createObject('EulerImplicit', name="")
  
  # Solving Method
  cube.createObject('CGLinearSolver', name="")
  
  # create a visual object of child object (ie. cube)
  visual = cube.createChild("Cube Visual")
  
  # Visual Ogl Model
  visual.createObject('OglModel', name="Visual",
                      fileMesh="mesh/name.ob", 
                      colour=[0.0,0.0,0.0],
                      scale=0.0)
  
  # Rigid Mapping Object
  visual.createObject('RigidMapping')
  
  # Collision Model for the Cube
  
  collision = cube.createChild("Cube Collision Model")
  
  # Creating Collision Objects
  collision.createObject('MeshObjLoader', name="Loader",
                        filename="mesh/smCube27.obj",
                        triangulate="true", scale=20.0)
  
  collision.createObject('Mesh', src="@loader")
  
  collision.createObject('MechanicalObject')
  
  collision.createObject('Triangle')
  collision.createObject('Line')
  collision.createObject('Point')
  
  collision.createObject('RigidMapping')
    
    
  
  return rootNode
