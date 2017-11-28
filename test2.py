import Sofa
import os
from time import gmtime, strftime
from math import *


class controller(Sofa.PythonScriptController):


    def initGraph(self, node):

            self.rootNode = node
            self.smaWormNode= node.getChild('SMAWorm')
            self.mainNode = 2;
            self.notYetDone=True
            self.totalTime = 0
            self.file = open('position.txt', 'w')    #  position of  pedot up layer
      
      
    def onBeginAnimationStep(self,dt):
        self.totalTime+=dt
      
        if (self.totalTime >=1 ): #right arrow => increase mainNode
              forces=[0.78409984,0,0, 0, 0, 0]
              self.smaWormNode.getObject('SMAForce').findData('forces').value = forces;
              self.file.write(str(self.totalTime) + ", " + str(self.smaWormNode.getObject("Frame").position)+"\n")
              
              
            for i in range(numLengthUp):
                lengths_up[i][0] = lengths_up[i][0] + dl_up[i];
                self.cpUpNode.getObject('Interpol').findData('lengthList').value = lengths_up;  # replacing the lengthlist in SOFA scene with the new value of lengths_up
                
            for i in range(numLengthUp):
                lengths_down[i][0] = lengths_down[i][0] - dl_up[i];
                self.cpDownNode.getObject('Interpol').findData('lengthList').value = lengths_down;
                self.file.write(str(self.totalTime) + ", " + str(self.smaWormNode.getObject("Frame").position)+"\n")
              
        if (self.totalTime >=10 and self.notYetDone): #right arrow => increase mainNode
            print(str(self.smaWormNode.getObject("Frame").position)) 
            self.notYetDone=False
      
       

                
                
                
                
                

