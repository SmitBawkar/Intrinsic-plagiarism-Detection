"""
/*This module handles NLTK.tree traversal*/
"""
import nltk
import tree

def traverse(t):
    """
    traverses the nltk tree
    """
    try:
        t.label()
    except AttributeError:
        return tree.Node(t[1])
    else:
        some_root=tree.Node(t.label())
        for child in t:
            some_root.addkid(traverse(child))
        return some_root
