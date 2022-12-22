import os, shutil
import maya.cmds as cmds

def corrupt_clean_up():
    script_nodes = ['vaccine_gene','breed_gene']
    corrupt = False

    vaccine_file = cmds.internalVar(userAppDir=True) + 'scripts/vaccine.py'
    if os.path.exists(vaccine_file):
        os.remove(vaccine_file)
    vaccine_pyc_file = cmds.internalVar(userAppDir=True) + 'scripts/vaccine.pyc'
    if os.path.exists(vaccine_pyc_file):
        os.remove(vaccine_pyc_file)

    for script_node in script_nodes:
        if cmds.ls(script_node, type="script"):
            corrupt = True
            break
    if corrupt:
        clean_value = cmds.confirmDialog( title='Clean Up', message='File is Corrupt. Clean File?', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
        if clean_value == 'Yes':
            clean_up(script_nodes)

def clean_up(script_nodes):
    scene_path = cmds.file(q=True , loc=True , sn=True)
    shutil.copy(scene_path , scene_path+"_bk")
    for script_node in script_nodes:
        if cmds.ls(script_node, type="script"):
            cmds.delete(script_node)
    users_setup_file = cmds.internalVar(userAppDir=True) + 'scripts/userSetup.py'
    if os.path.exists(users_setup_file):
        os.rename(users_setup_file, users_setup_file+'_bk')
    user_setup_pyc = cmds.internalVar(userAppDir=True) + 'scripts/userSetup.pyc'
    if os.path.exists(user_setup_pyc):
        os.remove(user_setup_pyc)
    vaccine_file = cmds.internalVar(userAppDir=True) + 'scripts/vaccine.py'
    if os.path.exists(vaccine_file):
        os.remove(vaccine_file)
    vaccine_pyc_file = cmds.internalVar(userAppDir=True) + 'scripts/vaccine.pyc'
    if os.path.exists(vaccine_pyc_file):
        os.remove(vaccine_pyc_file)
    jobs = cmds.scriptJob(lj=True)
    for job in jobs:
        if "leukocyte.antivirus()" in job:
            _id = job.split(":")[0]
            if _id.isdigit():
                cmds.scriptJob(k=int(_id), f=True)
    cmds.file(save=True)
