"""
/*This module does the parts of Speech(POS) tagging*/
"""
import proj_setting
import nltk

def proj_tagger():
    """
    tags words[] with appropriate POS tags using NLTK dictionay
    """
    proj_setting.before_chunk=nltk.pos_tag(proj_setting.words)
   
    
