from PIL import Image, ImageDraw

def drawGrid(gridWidth,gridLength):
    im = Image.new('RGB', (500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    largest = gridWidth if gridWidth > gridLength else gridLength #Determine which one that takes up most space

    drawScaleFactor=(500/(largest*1.1)) #Scale based on window size
    offsettPxs=4

    #Grid-outline-points (x,y)
    upperLeftP=(offsettPxs, offsettPxs)
    upperRightP=(((gridWidth*drawScaleFactor)+offsettPxs), offsettPxs)
    lowerLeftP=(offsettPxs, ((gridLength*drawScaleFactor)+offsettPxs))
    lowerRightP=(((gridWidth*drawScaleFactor)+offsettPxs), (((gridLength*drawScaleFactor)+offsettPxs)))

    #Grid-outline-drawing
    draw.line((upperLeftP[0], upperLeftP[1], upperRightP[0], upperRightP[1]), fill=128, width=3)
    draw.line((upperLeftP[0], upperLeftP[1], lowerLeftP[0], lowerLeftP[1]), fill=128, width=3)
    draw.line((lowerLeftP[0], lowerLeftP[1], lowerRightP[0], lowerRightP[1] ), fill=128, width=3)
    draw.line((upperRightP[0], upperRightP[1], lowerRightP[0], lowerRightP[1] ), fill=128, width=3)

    #Draw grid-column-lines
    for x in range(gridWidth):
        draw.line((x*drawScaleFactor+offsettPxs, offsettPxs, x*drawScaleFactor+offsettPxs, lowerRightP[1]), fill=128, width=1)
    #Draw grid-row-lines
    for x in range(gridLength):
        draw.line((offsettPxs,x*drawScaleFactor+offsettPxs,lowerRightP[0],x*drawScaleFactor+offsettPxs), fill=128, width=1)

    im.show()