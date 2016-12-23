import maya.cmds as cmds

startFrame = cmds.playbackOptions(query=True, minTime=True)
endFrame = cmds.playbackOptions(query=True, maxTime=True)
selectedObject = cmds.ls(sl=1)

def drawUI(): #Function that will draw the entire window



    #check to see if window exists
    if cmds.window("UI_MainWindow", exists = True):
        cmds.deleteUI("UI_MainWindow")

    #create actual window
    cmds.window("UI_MainWindow", title = "Choose which dude to put animation on", w = 200, h = 700, mnb = False, mxb = False, sizeable = False)
    cmds.columnLayout("UI_MainLayout", w = 150, h =500, columnAlign="center")


    if not len(selectedObject) == 1:
        print(selectedObject)
        cmds.deleteUI("UI_MainWindow")
        cmds.warning('Select ONE object')
    else:
        print(selectedObject[0])

        cmds.text(label=" ")

        #object selected
        cmds.text(label="object selected is:", backgroundColor=(0.66, 0.73, 0.62))
        cmds.text(label=selectedObject[0], backgroundColor=(0.99, 0.99, 0.58), font="boldLabelFont")

        cmds.text(label=" ")

        #bake range
        cmds.text(label="Baking Frame Range from:", backgroundColor=(0.66, 0.73, 0.62))
        cmds.text(label=str(startFrame) + " to " + str(endFrame), backgroundColor=(0.99, 0.99, 0.58), font="boldLabelFont")

        cmds.text(label=" ")

        #bake the selected
        cmds.button("UI_Bake", label = "Bake Selected", w = 100, backgroundColor=(0.87, 0.65, 0.64), command=lambda x:bakeObject())

        cmds.text(label=" ")

        cmds.button("UI_Cancel", label = "Cancel", w = 100, backgroundColor=(0.63, 0.67, 0.81), command=lambda x:cmds.deleteUI("UI_MainWindow"))

        cmds.showWindow("UI_MainWindow") #shows window

def bakeObject():
    newLocatorName = "loc_deleteMe"
    cmds.currentTime(startFrame)

    # objectXform = cmds.xform(selectedObject[0], q=True, m=True)
    objectXform = cmds.getAttr(selectedObject[0] + ".worldMatrix")
    if cmds.objExists(newLocatorName):
        cmds.delete(newLocatorName)
    newLocator = cmds.spaceLocator(name=newLocatorName)
    cmds.xform(newLocator, matrix=objectXform)

    for i in range(int(startFrame)+1, int(endFrame)):
        cmds.currentTime(i) #go to current frame
        cmds.xform(selectedObject, ws=True, matrix=objectXform) #move object to keyframe to pos
        cmds.setKeyframe(selectedObject, newLocatorName + '.matrix') #set keys on object

    cmds.delete(newLocatorName)
    cmds.select(selectedObject)
    cmds.deleteUI("UI_MainWindow") #close the script window

#be sure to delete the locator (if needed)
drawUI() #Calling drawUI now at the end of the script
