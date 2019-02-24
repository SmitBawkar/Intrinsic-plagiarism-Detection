"""
/*This module handles the Distance matrix computation */
"""
import proj_setting
import PyGram
from tabulate import tabulate

def create_matrix():
    """
    Creates a nxn matrix where n= number of sentences
    """
    for i in range(0,len(proj_setting.p)):
        proj_setting.mat.append([0]*(len(proj_setting.p)))
    print("Created Matrix")    

def find_dis():
    """
    Calls the edit distance function to calculate the pq gram distance
    """
    for i in range(0,len(proj_setting.p)):
        for j in range(i+1,len(proj_setting.p)):
            temp=proj_setting.p[i].edit_distance(proj_setting.p[j])
            proj_setting.mat[i][j]=temp
            proj_setting.mat[j][i]=temp
    print("Finding Distance")        

def print_mat():
    
    """
    writes the matrix to the log file
    """
    proj_setting.log+=tabulate(proj_setting.mat,tablefmt="grid") 
##    for i in range(0,len(proj_setting.p)):
##        for j in range(0,len(proj_setting.p)):
##           #print(proj_setting.mat[i][j],end="\t")
##           proj_setting.log+=(str(proj_setting.mat[i][j])+'\t')
##        #print()
    proj_setting.log+='\n'
    print("Matrix Computed")    
