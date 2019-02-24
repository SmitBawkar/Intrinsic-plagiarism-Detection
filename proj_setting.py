"""
/*This module stores all the major variables used in the entire project*/
##total_sent_count: Total count of sentences in the document
##all_sents       : list of all the sentences in the document
##sent_token      : list of all the preprocessed sentences to be tokenized
##words		  : list of tokenized words
##before_chunk    : POS(Parts of Speech) tagged words
##result          : NP(Noun Phrase) chunked POS tagged words
##p               : Tree Profile
##mat             : Matrix to store tree Edit distances
##median          : List containing median of each row
##mean            : Mean of the median list
##sd              : Standard deviation
##plagiarized_sent: list of sentences which lies outside threshold value
##log             : String to be written in the log file
##plag_sent_log   : List of all plagiarized sentences
"""


total_sent_count=0 
all_sents='all_sents'
sent_token=[] 
words='words'
before_chunk='before_chunk'
result='result'
p=[]
mat=[]
mean=''
sd=''
median=[]
plagiarized_sent=[]
log=''
plag_sent_log=''
count=0
plag_count=0



    
        
        
        
        
