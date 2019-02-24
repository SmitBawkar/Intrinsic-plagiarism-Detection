"""
/*This module does the required maths computation on the distance matrix to find the plagiarised sentences*/
"""
import math
import proj_setting

def median(lst):
    """
    computes median of the given list
    """
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst)%2 == 1:
            return lst[((len(lst)+1)//2)-1]
    if len(lst)%2 == 0:
            return float(sum(lst[(len(lst)//2)-1:(len(lst)//2)+1]))/2.0

#print(median([0.1,0.2,0.3,0.4]))
def matrix_median(mat):
    """
    calculates the median of every row of the matrix
    """
    l=[]
    for lst in mat:
        l.append(median(lst))
    print(l)    
    return l

def matrix_sd(lst):
    """
    calculates stand deviation
    """
    sum=0
    for xi in lst:
        sum+=math.pow(xi-proj_setting.mean,2)
    proj_setting.sd=math.sqrt(sum/len(lst))
    print('sd is',proj_setting.sd)
    proj_setting.log+=('sd is '+str(proj_setting.sd)+'\n')

def matrix_mean(lst):
    """
    calculates the mean of the list of median
    """
    sum=0
    for xi in lst:
        sum+=xi
    proj_setting.mean=sum/len(lst)
    print('mean is',proj_setting.mean)
    proj_setting.log+=('mean is '+str(proj_setting.mean)+'\n')

def find_plagiarized_sent():
    """
    calculates threshold value
    marks the plagiarised sentences which lies outside the threshold value
    """
    threshold_upper=proj_setting.mean+(1.8*proj_setting.sd)
    print('threshold upper'+str(threshold_upper)+'\n')
    proj_setting.log+=('Threshold upper '+str(threshold_upper)+'\n')
    threshold_lower=proj_setting.mean-(1.8*proj_setting.sd)
    print('threshold lower'+str(threshold_lower)+'\n')
    proj_setting.log+=('Threshold lower '+str(threshold_lower)+'\n')
    for i in range(len(proj_setting.median)):
        val=proj_setting.median[i]
        if not(threshold_lower<=val and val<=threshold_upper):
            proj_setting.plagiarized_sent.append(proj_setting.sent_token[i])
            #proj_setting.log+=(proj_setting.sent_token[i]+'\n')
    if len(proj_setting.plagiarized_sent)>0:
        for i in range(0,len(proj_setting.plagiarized_sent)):
            sen=proj_setting.plagiarized_sent[i].strip()
            word=sen.split()
            if len(word)>2:
                print(proj_setting.plagiarized_sent[i])
                proj_setting.plag_sent_log+=(proj_setting.plagiarized_sent[i]+'.\n\n')
                proj_setting.plag_count+=1
    print('Plagiarized sent: ',str(proj_setting.plag_count)+'\n')
    proj_setting.plag_sent_log+=('Plagiarized sent: '+str(proj_setting.plag_count)+'.\n\n')
    print('Plagiarism ratio: '+(str(proj_setting.plag_count/len(proj_setting.sent_token))))
    proj_setting.plag_sent_log+=('Plagiarism ratio: '+(str(proj_setting.plag_count/len(proj_setting.sent_token))))
    
        

