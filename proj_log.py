"""
/*This module creates a log of activies happening in the project
"""
import proj_setting
import os
def proj_logger():
        """
	writes debugging data into log.txt file
	"""
        path=os.getcwd()+"\plagiarism_log.txt"
        file=open(path,'w',encoding='utf-8')
        file.write(proj_setting.log)
        file.close()
        path=os.getcwd()+"\plagiarism.txt"
        file=open(path,'w',encoding='utf-8')
        file.write(proj_setting.plag_sent_log)
        file.close()
    
