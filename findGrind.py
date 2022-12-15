import math
import sys
import GridDrawer as gd
import ScadCaller as oScad

#TODO: convert between metric and imperial
isMetric=True

useArgs = len(sys.argv) == 6 #Determine whether to use arguments or user inputs

length=float(sys.argv[1])   if useArgs == True else float(input("Length: "))
width=float(sys.argv[2])    if useArgs == True else float(input("Width: "))
height=float(sys.argv[3])   if useArgs == True else float(input("Height: "))

minGridResolution=int(sys.argv[4]) if useArgs == True else int(input("minGridResolution: "))
maxGridResolution=int(sys.argv[5]) if useArgs == True else int(input("maxGridResolution: "))

smalletsGrid = 0
smalletsLossAreal = length*width #Initial value of max areal
gridAreal = 0
lossLengthExt = 0
lossWidthExt = 0

#Multipy by 10 for milimeter precisison
for x in range((minGridResolution*10),(maxGridResolution)*10+1):
    
    res = x/10 #Devide by 10 to go back to cm, but with decimals
    
    maxLengthRows = math.floor(length/res)  #Ex Only 3 lengths of 3cm fit inside 10cm, hence floor
    possibleLengthMax = (res*maxLengthRows) #Ex 3 lengths of 3cm makes 9cm
    lossLength = (length-possibleLengthMax) #Ex 10cm - 9cm is a loss of 1cm

    maxWidthRows = math.floor(width/res)
    possibleWidthMax = (res*maxWidthRows)
    lossWidth = (width-possibleWidthMax)

    arealLossLength = lossLength*width
    arealLossWidth = lossWidth*length

    lossTotalAreal = arealLossWidth+arealLossLength

    if lossTotalAreal < smalletsLossAreal:
        gridAreal = possibleLengthMax*possibleWidthMax
        smalletsLossAreal=lossTotalAreal 
        smalletsGrid = res
        lossLengthExt=lossLength
        lossWidthExt=lossWidth

gridWidth=math.floor(width/smalletsGrid)
gridLength=math.floor(length/smalletsGrid)

drawerAreal = length*width
lossPercent = ((drawerAreal-gridAreal)/drawerAreal)*100

print(
    "The total areal for the drawer is: ", drawerAreal, "cm²\n"+
    "The total areal for the ideal grid is: ", gridAreal, "cm²\n"+
    "The loss is: ", drawerAreal-gridAreal, "cm², or a loss of ",round(lossPercent,2),"%"
)


if lossLengthExt != 0 and lossWidthExt != 0:
    print("Loss os both")
elif lossLengthExt != 0:
    wwAreal = width*lossLengthExt
    wwArealSplitted = width*(lossLengthExt/2)    #Split it into 2 parts, so that its is padding on each side
    print("wwAreal: ",wwAreal)
    print("wwArealSplitted: ",wwArealSplitted)
    print("splitted XYZ = ", width,(lossLengthExt/2),height)
    #TODO Split into multiple smaller parts
    #oScad.createStlPaddingLength(width,height,lossLengthExt)
elif lossWidthExt != 0:
    print("Loss on width")

print("The best grid size is",smalletsGrid,"x",smalletsGrid,"cm . The grid will be [WxL]: ",gridWidth,"x",gridLength)

openOpenScad = input(
    "--Functions--- \n"+
    "openscad - Open openSCAD with the correct values \n"+
    "draw - Draws how the grid will look like \n"+
    "createStlFiles - Creates some default sizes \n"+
    "exit\n")
if openOpenScad == "openscad":
    print("Create 1 box")
    numberOfLengths=input("Number of lengths: ")
    numberOfWidth=input("Number of widths: ")
    oScad.openScad(numberOfLengths,numberOfWidth,smalletsGrid,height)
elif openOpenScad == "draw":
    gd.drawGrid(gridWidth,gridLength)
elif openOpenScad == "createStlFiles":
    outputFolder=input("Folder to store STL files: ")
    oScad.createStlFiles(outputFolder,smalletsGrid,height)