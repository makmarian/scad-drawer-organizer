
import os

def openScad(numberOfLengths,numberOfWidth,smalletsGrid,height):
    os.popen("openscad -D 'numberOfLengths'="+numberOfLengths+" -D 'numberOfWidth'="+numberOfWidth+" -D 'gridSize'="+str(smalletsGrid*10)+" -D 'height'="+str(height*10)+" scalable_box.scad")

def createStlFiles(outputFolder,smalletsGrid,height):
    arr=[("1","1"),("1","2"),("2","2"),("1","3"),("2","3"),("3","3")]
    for x in arr:
        os.popen("openscad -o "+outputFolder+"/"+x[0]+"x"+x[1]+".stl -D 'numberOfLengths'="+x[0]+" -D 'numberOfWidth'="+x[1]+" -D 'gridSize'="+str(smalletsGrid*10)+" -D 'height'="+str(height*10)+" scalable_box.scad")

def createStlPaddingLength(width,height,lossLengthExt ):
    os.popen("openscad -D 'width'="+str(width*10)+" -D 'height'="+str(height*10)+" -D 'length'="+str((lossLengthExt/2)*10)+" padding.scad")