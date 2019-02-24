"""
/*This module preprocesses all_sent[] based on rules and eliminates sentences which are outside the scope of the project*/
"""
import proj_setting
import nltk.data
import re

def proj_preprocessor():
    """
    Eliminates sentences that lies outside the scope of the project
    """
    sent_detector=nltk.data.load('tokenizers/punkt/english.pickle')
##    Rule 
##    If there is a '.' before the sentence should actually end, make the parser go ahead without breaking the sentence.
    before_regex=sent_detector.tokenize(proj_setting.all_sents.strip())
    for sent in before_regex:
        proj_setting.total_sent_count+=1
##    Rule 
##    If there is an acknowledgment or citation after any sentence,discard from further consideration,if quotes are present too.
##    Eg: Various scientists have acknowledged doubt in the veracity of the results[4].
##    The above sentence will not be excluded from tagging.
##    Eg:"Curiosity killed the experiment", a scientist opined[4].
##    The above sentence will be excluded from tagging.  
        match3=re.search(r'\[[\d+\,]+\]',sent)
##    Rule 
##    If there are quotes present, it indicates that the content within the quotes are not explicitly of the author's
##    Eg: Few physicists are of the opinion that "Fermions can act like electrons when grouped together at subzero temperatures"
        match2=re.search(r'[\w\s]*\"[\w\s]+\"[\w\s]*',sent)
##    Rule 
##    If there are acronyms present like (U.S.S.R),(F.B.I) in brackets, remove them
##    Eg:The Federal Bureau of Investigation(F.B.I) made numerous arrests in Baltimore today, pending further investigation.
        sent=re.sub(r'\([A-Z\.]+\)','',sent)
##   Rule 
##   For scientific names enclosed in brackets, remove them
##   Eg: The wetland berms and cells were planted with a variety of native plant species such as Carex crinita(fringed sedge).
        while re.search(r'\((.*?)\)',sent):
            sent=re.sub(r'\((.*?)\)','',sent)
        if not match2:
            if match3:
                sent=re.sub(r'\[[\d+\,]+\]','',sent)
            ind=sent.find('et al.')
            if(ind!=-1):
                
                               
           
##   Rule
##   If there is "et al." present in the sentence,remove it.
##   Eg:According to McAllister et al.,certain species of plant are non-native to America.
                ind=sent.find('et al.')
                ind1=sent.find(',',ind)
                sent=sent[ind1+1:]
                sent=sent.strip()
            proj_setting.sent_token.append(sent[0:-1])#Remove '.' after every sentence
    print('Total No of sent ',str((proj_setting.total_sent_count)))       
    print('Total No of sent under consideration ',str(len(proj_setting.sent_token)))
    proj_setting.log+=('Total No of sent '+str((proj_setting.total_sent_count))+'\n\n')
    proj_setting.log+=('Total No of sent under consideration '+str(len(proj_setting.sent_token))+'\n\n')
    print(proj_setting.sent_token)
    proj_setting.log+=('Sentences under consideration are\n')
    for sent in proj_setting.sent_token:
        proj_setting.log+=(sent+'\n')

        
