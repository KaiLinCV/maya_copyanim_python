# This script will copy keyframes from a source controller heirarchy and paste it onto the target controller heirarchy
# Please note that the controller names will have to be identical for it to work
# Created mainly to automate the process of copying animation from one character to the next
# Script by Kai-Lin Chuang
import maya.cmds as cmds

##### Functions #####

# Removes any namespace if there are any. This will ensure that both target and source controllers are matched.
# Example: 'Char01:root_Ctrl' -> 'root_Ctrl'
def strip_namespace(name):
    return name.split(':')[-1]

# Finds all controllers in the given root hierarchy. Uses the strip_namespace() function to ignore namespaces.
def get_controllers(root):
    all_descendants = cmds.listRelatives(root, allDescendents=True, type='transform') or []
    all_ctrls = [root] + all_descendants
    controllers = [ctrl for ctrl in all_ctrls if 'ctrl' in ctrl.lower()]
    return controllers

# Creates a dictionary {} to map source controllers to target controllers base on matching names
def map_controllers(source_ctrls, target_ctrls):
    mapping = {}
    for src in source_ctrls:
        src_name = strip_namespace(src.split('|')[-1])
        for tgt in target_ctrls:
            tgt_name = strip_namespace(tgt.split('|')[-1])
            if src_name == tgt_name:
                mapping[src] = tgt

    return mapping

# Transfer animation keyframes from the source to the target
# Copies keyframes from all animatable attributes and pastes the copied data. 
# If attributes have no keyframes, then it will be skipped. 
def transfer_keys(source, target):
    attrs = cmds.listAnimatable(source)
    if not attrs:
        return

    for attr in attrs:
        if cmds.objExists(attr):
            short_attr = attr.split('.')[-1]
            target_attr = f"{target}.{short_attr}"
            if cmds.objExists(target_attr):
                cmds.cutKey(target_attr, clear=True)
                cmds.copyKey(source, attribute=short_attr)
                try:
                    cmds.pasteKey(target, attribute=short_attr)
                except RuntimeError:
                    # Handles "Nothing to paste from" without stopping the script
                    continue    

# Main function to coordinate all of the above functions to use.
# Displays a confirmation message when the script is finished.
def copy_animation(source_root, target_root):
    source_ctrls = get_controllers(source_root)
    target_ctrls = get_controllers(target_root)

    mapping = map_controllers(source_ctrls, target_ctrls)
    if not mapping:
        cmds.warning("No matching controllers found.")
        return

    for src, tgt in mapping.items():
        transfer_keys(src, tgt)

    cmds.inViewMessage(amg="Animation transfer complete", pos='midCenter', fade=True)
    
##### UI #####
# Creates and displays the user interface in Maya
def show_copy_anim_ui():
    if cmds.window("copyAnimUI", exists=True):
        cmds.deleteUI("copyAnimUI")

    window = cmds.window("copyAnimUI", title="Copy Animation Tool", widthHeight=(350, 80), sizeable=True)
    cmds.columnLayout(adjustableColumn=True, rowSpacing=10, columnAlign='center', columnAttach=('both', 20))

    cmds.text(label="Select Source and Target Root Nodes in the Viewport", align='center')

    cmds.button(label="Copy Animation", height=40, bgc=(0.3, 0.6, 0.3), 
                command=lambda *_: on_copy_button())

    cmds.setParent("..")
    cmds.showWindow(window)

# Execution for the "Copy Animation" button, triggers the animation copy process
def on_copy_button():
    selection = cmds.ls(selection=True)
    if len(selection) != 2:
        cmds.warning("! Please select exactly 2 character root nodes: source, then target.")
        return

    source_root, target_root = selection
    copy_animation(source_root, target_root)

show_copy_anim_ui()
