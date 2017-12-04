import Sofa
import os
from time import gmtime, strftime
from math import *


class controller(Sofa.PythonScriptController):


    def initGraph(self, node):

            self.rootNode = node
            self.smawormNode= node.getChild('SMAWorm')
            self.mainNode = 2;
            self.notYetDone=True
            self.totalTime = 0
            self.file = open('position.txt', 'w')    #  position of  pedot up layer
      
      
    def onBeginAnimationStep(self,dt):
        self.totalTime+=dt
      
        if (self.totalTime >=1 ): #right arrow => increase mainNode
              forces=[0,0,1011.77967, 0, 0, 0]
              self.smawormNode.getObject('SMAForce').findData('forces').value = forces;
              self.file.write(str(self.totalTime) + ", " + str(self.smawormNode.getObject("Frame").position)+"\n")
              
        if (self.totalTime >=10 and self.notYetDone): #right arrow => increase mainNode
            print(str(self.smawormNode.getObject("Frame").position)) 
            self.notYetDone=False
      
       
        
