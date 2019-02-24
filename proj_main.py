import proj_setting
import proj_reader
import proj_preprocess
import proj_tag
import proj_chunk
import proj_tree_traversal
import PyGram
import proj_matrix
import proj_median
import nltk
import time
import proj_log

def init():
    proj_reader.read_proj_file()
    proj_preprocess.proj_preprocessor()
    for sent in proj_setting.sent_token:
        proj_setting.words=nltk.tokenize.word_tokenize(sent)
        proj_tag.proj_tagger()
        proj_chunk.proj_chunker()
        if proj_setting.count<=5:
            proj_setting.result.draw()
            proj_setting.count+=1
            print(proj_setting.result.pprint())
        proj_setting.log+=(proj_setting.result.pprint()+'\n')
        if not proj_setting.result:
            print('Got an empty sentence')
            proj_setting.sent_token.remove(sent)
        tree_root=PyGram.Profile(proj_tree_traversal.traverse(proj_setting.result))
        proj_setting.p.append(tree_root)
        
t=time.process_time()
init()
time_after_init=time.process_time()
print('Init took',time_after_init-t)
proj_matrix.create_matrix()
time_after_create=time.process_time()
print('Create took',time_after_create-time_after_init)
proj_matrix.find_dis()
time_after_find=time.process_time()
print('Find took',time_after_find-time_after_create)
proj_matrix.print_mat()
time_after_print=time.process_time()
print('Print took',time_after_print-time_after_find)
print('\nMedian:')
proj_setting.median=proj_median.matrix_median(proj_setting.mat)
time_after_median=time.process_time()
print('Median took',time_after_median-time_after_print)
proj_median.matrix_mean(proj_setting.median)
proj_median.matrix_sd(proj_setting.median)
time_after_parameters=time.process_time()
print('Params took',time_after_parameters-time_after_median)
proj_median.find_plagiarized_sent()
time_after_calc=time.process_time()
print('Calc took',time_after_calc-time_after_parameters)
proj_log.proj_logger()

    
