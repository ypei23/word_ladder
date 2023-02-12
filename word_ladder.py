#!/bin/python3



def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    with open('words5.dict', 'r') as file:
        words = file.readlines()
    words_list = [word.strip() for word in words]
    from collections import deque
    stack = []
    stack.append(start_word)
    queue = deque([])
    queue.append(stack[0])
    i = 0
    while queue:
        word_awaiting = queue.pop()
        while i < len(words_list):   
            if _adjacent(word_awaiting, words_list[i]):
                if words_list[i] not in stack:
                    stack.append(words_list[i])
                    queue.append(words_list[i])       
                if words_list[i] == end_word:
                    return stack
            else:
                i += 1
        return None
    return stack

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 0: 
        return False
    for i in range(len(ladder)-1):
        if _adjacent(ladder[i], ladder[i+1]) == False:
            return False 
    return True
            
def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    counter = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            counter += 1
    return counter == 1
