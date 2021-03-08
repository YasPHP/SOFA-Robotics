# imports
from stlib.scene import MainHeader
from stlib.solver import DefaultSolver
from stlib.physics.rigid import Floor

# NOTE: double quotations for name param and single for function param
def createScene(rootNode):
  
  MainHeader(rootNode, gravity=[0.0, -981.0, 0.0])
  
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
  cube.createObject('EulerImplicit', name="odesolver")
  
  # Solving Method
  cube.CreateObject('CGLinearSolver', name="solver")
