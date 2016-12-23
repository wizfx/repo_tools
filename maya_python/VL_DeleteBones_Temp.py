
import maya.cmds as cmds

def unSelect():
    cmds.select(clear=True)

# Select some specific bones
def removeBones():
    unSelect()
    # cmds.removeJoint('*clavicle*')
    cmds.removeJoint('*prop*')

removeBones()
