#!/usr/bin/env python

def break_words(stuff):
    """this function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)
    #this creates a cloned list and doesn't modify the orginial list
    
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word
    
def print_last_word(words):
    """prints the last word after poping it off"""
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then print the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)