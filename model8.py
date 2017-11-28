import Sofa
from math import sin,cos

#path = os.path.dirname(os.path.abspath(__file__))+'/'

#One of the problem is the dimensions

def createScene(rootNode):
    
                rootNode.createObject('RequiredPlugin', pluginName='SoftRobots')
                rootNode.createObject('RequiredPlugin', pluginName='BeamAdapter')
                rootNode.createObject('VisualStyle', displayFlags='showVisualModels showBehaviorModels showCollisionModels hideBoundingCollisionModels showForceFields showInteractionForceFields hideWireframe')
            
                rootNode.findData('dt').value= 0.01
                rootNode.findData('gravity').value= '0 -9810 0'  # the gravity in mm  -9810 

                #rootNode.createObject('FreeMotionAnimationLoop')
                #rootNode.createObject('LCPConstraintSolver',  tolerance='1e-1', maxIt='1e1')
                rootNode.createObject('BackgroundSetting', color='0 0.168627 0.211765')
                rootNode.createObject('OglSceneFrame', style="Arrows", alignment="TopRight")
                
                #rootNode.createObject('PythonScriptController', classname="controller", filename="animation.py")
                
                rootNode.createObject('PythonScriptController', classname="controller", filename="o.py")
                
                smawormNode = rootNode.createChild('SMAWorm')
                smawormNode.createObject('EulerImplicit')
                smawormNode.createObject('PCGLinearSolver', preconditioners='linearSolver')
                smawormNode.createObject('BTDLinearSolver', name='linearSolver')
                
                smawormNode.createObject('Mesh', edges='0 1  1 2  2 3  3 4  4 5')
                
                smawormNode.createObject('MechanicalObject', template='Rigid', position='0 0 0 0 0 0 1   2.1432 0 0 0 0 0 1  4.2864 0 0 0 0 0 1  6.4296 0 0 0 0 0 1   8.5728 0 0 0 0 0 1   10.716 0 0 0 0 0 1', name='Frame') 
                
                #smawormNode.createObject('ConstantForceField',name='SMAForce', forces='0 0 0 0 0 0    0 0 -20 0 -200 0   0 0 40 0 0 0   0 0 -20 0 200 0 ')
                
                smawormNode.createObject('RestShapeSpringsForceField', name="MeasurementFF", points="0" , stiffness="1000e10",  recompute_indices="1", angularStiffness="100e100" , drawSpring="1" , springColor="1 0 0 1")
                
         #SPE Layer
                speNode = smawormNode.createChild('SPE')
                speNode.createObject('Mesh', edges='0 1  1 2  2 3  3 4  4 5')
                speNode.createObject('BeamInterpolation', name='Interpol', crossSectionShape='rectangular', lengthY='2.167', lengthZ='0.25', defaultYoungModulus='0.8e6')  # thickness 0.2 mm
                speNode.createObject('AdaptiveBeamForceFieldAndMass',  name="BeamForceField", computeMass="1", massDensity="0.0017")
                
                
                #PEDOT layer or electrodes layer
                
                #Upper Layer  check the youngModulus again conversion 
                cp_upNode = smawormNode.createChild('CP_up')
                cp_upNode.createObject('Mesh', edges='0 1  1 2  2 3  3 4  4 5')
                cp_upNode.createObject('BeamInterpolation', name='Interpol', crossSectionShape='rectangular', lengthY='2.167', lengthZ='0.25', defaultYoungModulus='1.4e6', dofsAndBeamsAligned='0', DOF0TransformNode0="0 0 0.1 0 0 0 1   0 0 0.1 0 0 0 1  0 0 0.1 0 0 0 1  0 0 0.1 0 0 0 1   0 0 0.1 0 0 0 1  0 0 0.1 0 0 0 1 ", DOF1TransformNode1="0 0 0.1 0 0 0 1   0 0 0.1 0 0 0 1  0 0 0.1 0 0 0 1  0 0 0.1 0 0 0 1  0 0 0.1 0 0 0 1  0 0 0.1 0 0 0 1 ") 
                cp_upNode.createObject('AdaptiveBeamForceFieldAndMass',  name="BeamForceField", computeMass="1", massDensity="0.0017")
                
                
                #downlayer
                cp_downNode=smawormNode.createChild('CP_down')
                cp_downNode.createObject('Mesh', edges='0 1  1 2  2 3  3 4  4 5')
                cp_downNode.createObject('BeamInterpolation', name='Interpol', crossSectionShape='rectangular', lengthY='2.167', lengthZ='0.25', defaultYoungModulus='1.4e6', dofsAndBeamsAligned='0', DOF0TransformNode0="0 0 -0.1 0 0 0 1   0 0 -0.1 0 0 0 1  0 0 -0.1 0 0 0 1   0 0 -0.1 0 0 0 1  0 0 -0.1 0 0 0 1   0 0 -0.1 0 0 0 1   ", DOF1TransformNode1="0 0 -0.1 0 0 0 1   0 0 -0.1 0 0 0 1  0 0 -0.1 0 0 0 1 ") 
                cp_downNode.createObject('AdaptiveBeamForceFieldAndMass',  name="BeamForceField", computeMass="1", massDensity="0.0017")
                
                                
                
                
                 
                visuNode = smawormNode.createChild('visualization')
                visuNode.createObject('RegularGridTopology', name='topology', n="10 4 2" , min="0 -0.3 -0.05", max="10.716 0.5 0.05")
                visuNode.createObject('MechanicalObject', name='test', src='@topology')
                visuNode.createObject('AdaptiveBeamMapping', interpolation="@../SPE/Interpol", input="@../Frame", output="@test")
                
                oglNode = visuNode.createChild('ogl')
                oglNode.createObject('OglModel', name='visualModel', color='0 1 0 1')
                oglNode.createObject('IdentityMapping')
                
                
                 
                visuNode2 = smawormNode.createChild('visualization2')
                visuNode2.createObject('RegularGridTopology', name='topology', n="10 4 2" , min="0 -0.3 -0.05", max="10.716 0.5 0.05")
                visuNode2.createObject('MechanicalObject', name='test', src='@topology')
                visuNode2.createObject('AdaptiveBeamMapping', interpolation="@../CP_up/Interpol", input="@../Frame", output="@test")
                
                oglNode2 = visuNode2.createChild('ogl')
                oglNode2.createObject('OglModel', name='visualModel', color='1 0 0 1')
                oglNode2.createObject('IdentityMapping')               
        
                
                visuNode3 = smawormNode.createChild('visualization3')
                visuNode3.createObject('RegularGridTopology', name='topology', n="10 4 2" , min="0 -0.3 -0.05", max="10.716 0.5 0.05")
                visuNode3.createObject('MechanicalObject', name='test', src='@topology')
                visuNode3.createObject('AdaptiveBeamMapping', interpolation="@../CP_down/Interpol", input="@../Frame", output="@test")
                
                oglNode3 = visuNode3.createChild('ogl')
                oglNode3.createObject('OglModel', name='visualModel', color='1 0 0 1')
                oglNode3.createObject('IdentityMapping')                               
                           

                return rootNode



 
