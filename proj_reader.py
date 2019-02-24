"""
/*This module locates and reads the file specified by the user*/
"""
import proj_setting
import tkinter.filedialog
import xml.etree.ElementTree as ET

def read_proj_file():
    """
    Opens a tkinter diloag box to locate the file.
    reads the file and stores the sentences in all_sents[]
    """
    filename=tkinter.filedialog.askopenfilename()
    file=open(filename,encoding='utf-8')
    proj_setting.log+=('Opened '+filename+' for reading\n')
    tree=ET.parse(file)
    root=tree.getroot()
    finalbody=''
    for body in root.iter('bodyText'):
        finalbody+=body.text
    proj_setting.all_sents=finalbody
    proj_setting.log+=('Sentences from text\n'+finalbody+'\n')

