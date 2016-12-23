# http://kevman3d.blogspot.com/2015/05/introduction-to-simple-maya-ui-coding.html


import maya.cmds as cmds

def drawUI(): #Function that will draw the entire window
    #check to see if window exists
    if cmds.window("UI_MainWindow", exists = True):
        cmds.deleteUI("UI_MainWindow")
    #create actual window
    cmds.window("UI_MainWindow", title = "Choose which dude to put animation on", w = 200, h = 700, mnb = False, mxb = False, sizeable = False)
    cmds.columnLayout("UI_MainLayout", w = 150, h =500)

    #file input
#    cmds.button("UI_fileDialogue", label = "...", w = 200, command=getFile())

    #build the list of choices
    # crowdList = 12
    # for n in range(crowdList):
    #     newButt = "Butt_" + str(n)
    #     newButt = cmds.button(newButt, label = "Root" + str(n), w = 100, command=lambda x: selectDude(n))

    butt0 = cmds.button("Button00", label = "Dude 00", w = 100, backgroundColor=(0.66, 0.73, 0.62), command=lambda x:selectDude(0))
    butt1 = cmds.button("Button01", label = "Dude 01", w = 100, backgroundColor=(0.66, 0.73, 0.62), command=lambda x:selectDude(1))
    butt2 = cmds.button("Button02", label = "Dude 02", w = 100, backgroundColor=(0.66, 0.73, 0.62), command=lambda x:selectDude(2))
    butt3 = cmds.button("Button03", label = "Dude 03", w = 100, backgroundColor=(0.66, 0.73, 0.62), command=lambda x:selectDude(3))
    butt4 = cmds.button("Button04", label = "Dude 04", w = 100, backgroundColor=(0.66, 0.73, 0.62), command=lambda x:selectDude(4))
    butt5 = cmds.button("Button05", label = "Dude 05", w = 100, backgroundColor=(0.66, 0.73, 0.62), command=lambda x:selectDude(5))
    butt6 = cmds.button("Button06", label = "Dude 06", w = 100, backgroundColor=(0.66, 0.73, 0.62), command=lambda x:selectDude(6))
    butt7 = cmds.button("Button07", label = "Dude 07", w = 100, backgroundColor=(0.66, 0.73, 0.62), command=lambda x:selectDude(7))
    butt8 = cmds.button("Button08", label = "Dude 08", w = 100, backgroundColor=(0.66, 0.73, 0.62), command=lambda x:selectDude(8))
    butt9 = cmds.button("Button09", label = "Dude 09", w = 100, backgroundColor=(0.66, 0.73, 0.62), command=lambda x:selectDude(9))
    butt10 = cmds.button("Button10", label = "Dude 10", w = 100, backgroundColor=(0.66, 0.73, 0.62), command=lambda x:selectDude(10))
    butt11 = cmds.button("Button11", label = "Dude 11", w = 100, backgroundColor=(0.66, 0.73, 0.62), command=lambda x:selectDude(11))

    buttAtomOut = cmds.button("AtomOut", label = "ATOM Export", w = 100, backgroundColor=(0.99, 0.99, 0.58), command=cmds.ExportAnimOptions)
    buttAtomIn = cmds.button("AtomIn", label = "ATOM Import", w = 100, backgroundColor=(0.68, 0.77, 0.8), command=cmds.ImportAnimOptions)

    cmds.button("UI_Cancel", label = "Cancel", w = 100, backgroundColor=(0.87, 0.65, 0.64), command=lambda x:closeUI())

    cmds.showWindow("UI_MainWindow") #shows window

def unSelect():
    cmds.select(clear=True)

def selectDude(numVar): #selects hierchy for dude chosen
#    chosenVar = "c0_root_jnt"
    chosenVar = "c" + str(numVar) + "_root_jnt"
    unSelect()
    cmds.select(cmds.listRelatives(chosenVar, children=True))
#selectDude()

def getFile(): #gets file path
    basicFilter = "*.atom"
    cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=2)

def closeUI():
    unSelect()
    cmds.deleteUI("UI_MainWindow")

drawUI() #Calling drawUI now at the end of the script
