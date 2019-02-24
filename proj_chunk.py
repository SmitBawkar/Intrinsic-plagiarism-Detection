"""
/*This module chunks POS words in to noun phrases */
"""
import proj_setting
import nltk.chunk

def proj_chunker():
        """
        chunks POS tagged before_chunk[] into noun phrase chunks
        """
        proj_setting.tagged_words=nltk.chunk.ne_chunk(proj_setting.before_chunk)
        grammar = "NP: {<DT>?<JJ>*<NN>}"
        cp = nltk.RegexpParser(grammar)
        proj_setting.result = cp.parse(proj_setting.tagged_words)
