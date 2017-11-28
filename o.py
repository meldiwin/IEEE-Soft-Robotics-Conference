import Sofa
import os
from time import gmtime, strftime
import numpy
import sys
from math import *

class controller(Sofa.PythonScriptController):
    
    
    def initGraph(self, node):

            self.rootNode = node
            self.smawormNode= node.getChild('SMAWorm')
            self.cpUpNode= self.smawormNode.getChild('CP_up')
            self.cpDownNode= self.smawormNode.getChild('CP_down')
            self.speNode= self.smawormNode.getChild('SPE')
            self.mainNode = 2;
            self.notYetDone=True
            self.totalTime = 0
            self.file = open('position.txt', 'w')    #  position of  pedot up layer
            
    
    



    def onBeginAnimationStep(self,dt):
        self.totalTime+=dt
        lengths_up = self.cpUpNode.getObject('Interpol').findData('lengthList').value
        lengths_down = self.cpDownNode.getObject('Interpol').findData('lengthList').value
        YoungModulus1 = self.speNode.getObject('Interpol').findData('defaultYoungModulus').value
        YoungModulus2 = self.cpUpNode.getObject('Interpol').findData('defaultYoungModulus').value
        YoungModulus3 = self.cpDownNode.getObject('Interpol').findData('defaultYoungModulus').value
        position=self.smawormNode.getObject('Frame').findData('position').value
        
        DL_1 = 0.00024640048;  # this is analogy of the voltage  value for each test mapping 
        numLengthUp = 5
        length_up=0.0; 
        
        
        for i in range(numLengthUp):
            length_up = length_up + lengths_up[i][0]  
            
            
            
            dl_up=[0]*numLengthUp;  
            
            
            
        for i in range(numLengthUp):
            dl_up[i] =  DL_1*lengths_up[i][0]/length_up; 
            
            print dl_up[i]
            
        if (self.totalTime<=2.96): 
            
            for i in range(numLengthUp):
                lengths_up[i][0] = lengths_up[i][0] - dl_up[i];
                self.cpUpNode.getObject('Interpol').findData('lengthList').value = lengths_up;  # replacing the lengthlist in SOFA scene with the new value of lengths_up
                #print lengths_up[i][0]
                
                
            for i in range(numLengthUp):
                lengths_down[i][0] = lengths_down[i][0] + dl_up[i];
                self.cpDownNode.getObject('Interpol').findData('lengthList').value = lengths_down;            
                self.file.write(str(self.totalTime) + ", " + str(self.smawormNode.getObject("Frame").position)+"\n")
                
                
                
        if (self.totalTime>=2.96): 
            
            for i in range(numLengthUp):
                lengths_up[i][0] = lengths_up[i][0] + dl_up[i];
                self.cpUpNode.getObject('Interpol').findData('lengthList').value = lengths_up;  # replacing the lengthlist in SOFA scene with the new value of lengths_up
                #print lengths_up[i][0]
                
                
            for i in range(numLengthUp):
                lengths_down[i][0] = lengths_down[i][0] - dl_up[i];
                self.cpDownNode.getObject('Interpol').findData('lengthList').value = lengths_down;            
                self.file.write(str(self.totalTime) + ", " + str(self.smawormNode.getObject("Frame").position)+"\n")        
                
                
        if (self.totalTime>=5.92): 
            
            for i in range(numLengthUp):
                lengths_up[i][0] = lengths_up[i][0];
                self.cpUpNode.getObject('Interpol').findData('lengthList').value = lengths_up;  # replacing the lengthlist in SOFA scene with the new value of lengths_up
                #print lengths_up[i][0]
                
                
            for i in range(numLengthUp):
                lengths_down[i][0] = lengths_down[i][0];
                self.cpDownNode.getObject('Interpol').findData('lengthList').value = lengths_down;            
                self.file.write(str(self.totalTime) + ", " + str(self.smawormNode.getObject("Frame").position)+"\n")        
                  
                
                
                
        if (self.totalTime >=10 and self.notYetDone): #right arrow => increase mainNode
            print(str(self.smawormNode.getObject('Frame').position)) 
            self.notYetDone=False                