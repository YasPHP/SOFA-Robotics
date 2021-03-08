# imports
from stlib.scene import MainHeader
from stlib.solver import DefaultSolver
from stlib.physics.rigid import Floor

# NOTE: double quotations for name param and single for function param
def createScene(rootNode):
  """
  Following the Defrost team of the INRIA Lille Nord Europe's tutorial.
  """
  MainHeader(rootNode, gravity=[0.0, -981.0, 0.0])
  
  # Collision Handling Built-in Function
  ContactHeader(rootNode, alarmDistance=10,
               contactDistance=5)
  
  cube = rootNode.createChild("Cube")
  
  # Mechanical Model
  
  totalMass = 5.0
  volume = 5.0
  inertiaMatrix = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
  
  cube.createObject('MechanicalObject', name="DOF", 
                    template="Rigid", translation=[0.0, 0.0, 0.0], 
                    rotation = [0.0, 0.0, 0.0])
  
  cube.createObject('UniformMass', name="Mass", 
                    mass=[totalMass, volume, inertiaMatrix[:]])

  # Time Integration Scheme
  cube.createObject('EulerImplicit', name="Odesolver")
  
  # Solving Method
  cube.createObject('CGLinearSolver', name="Solver")
  
  # Visual Object of Cube
  visual = cube.createChild("Cube Visual")
  
  visual.createObject('OglModel', name="Visual",
                      fileMesh="mesh/smCube27.ob", 
                      colour=[0.1,0.1,1.0],
                      scale=25.0)
  
  visual.createObject('RigidMapping')
  
  # Collision Model for the Cube
  
  collision = cube.createChild("Cube Collision Model")
  
  collision.createObject('MeshObjLoader', name="Loader",
                        filename="mesh/smCube27.obj",
                        triangulate="true", scale=20.0)
  
  collision.createObject('Mesh', src="@loader")
  
  collision.createObject('MechanicalObject')
  
  collision.createObject('Triangle')
  collision.createObject('Line')
  collision.createObject('Point')
  
  collision.createObject('RigidMapping')
  
  
  # Floor in the Scene
  
  floor = Floor(rootNode, name="Floor",
                translation=[0.0, -3200.0, 0.0],
                uniformScale=7.0,
                isAStaticObject=True)
  
  return rootNode
