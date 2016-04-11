
from decimal import *
from PIL import Image, ImageChops, ImageOps
import math, operator
import sys
import Queue



def main():

    image1 = Image.open("newImage3.png").convert("1") # convert to bilevel from RGB
    #print str(list(image1.getdata()))


    shapes = connectedComponentLabeling(image1)


    im = Image.new("1", image1.size, "white")
    #im.putdata(list(image1.getdata()))
    counter = 1

    for shape in shapes:
        im = Image.new("1", image1.size, "white")
        for pixel in shape:
            im.putpixel(pixel, 0)
        im.save("image" + str(counter) + ".png", "png")
        counter += 1

    #im.save("imageClone.png", "png")

    # list_of_pixels = list(im.getdata())
    # # Do something to the pixels...
    # im2 = Image.new(im.mode, im.size)
    # im2.putdata(list_of_pixels)

    # for shape in shapes:
    #     print shape


# return a list of connected components in an image
def connectedComponentLabeling(image):
    shapes = []

    setOfPoints = getSetOfBlackPoints(image)
    q = Queue.Queue()  # for holding connected pixels

    while (len(setOfPoints) > 0):
        # get and pop point from set
        node = setOfPoints.pop()
        # print node
        # put into queue
        q.put(node)
        # create empty set
        shape = set()

        while (not q.empty()):
            point = q.get()
            getNeighboringPoints(point, setOfPoints, q)
            shape.add(point)

        shapes.append(shape)

    # print len(shapes)
    return shapes

def getNeighboringPoints(point, setOfPoints, queue):
    up = (point[0], point[1] + 1)
    down = (point[0], point[1] - 1)
    left = (point[0] - 1, point[1])
    right = (point[0] + 1, point[1])

    if up in setOfPoints:
        setOfPoints.discard(up)
        queue.put(up)
    if down in setOfPoints:
        setOfPoints.discard(down)
        queue.put(down)
    if left in setOfPoints:
        setOfPoints.discard(left)
        queue.put(left)
    if right in setOfPoints:
        setOfPoints.discard(right)
        queue.put(right)


# returns tuples of black pixel coordinates
def getSetOfBlackPoints(image):
    counter = 0
    imagePoints = set()
    for y in range(0, image.size[1]):
        for x in range(0, image.size[0]):
            counter += 1
            p1 = image.getpixel((x,y))
            if p1 == 0: # if black
                imagePoints.add((x,y))

    return imagePoints


if __name__ == "__main__": main()