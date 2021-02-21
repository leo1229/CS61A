"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    candidate=[x for x in paragraphs if select(x)]
    if k>=len(candidate):
        return ''
    else:
        return candidate[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def helper(s):
        list_s=[]
        element_in_s=''
        s=s.lower()
        i=0
        for x in s:
            if x<='z' and x>='a':
                element_in_s+=x
            elif x==' ':
                list_s+=[element_in_s]
                element_in_s=''
            if i==len(s)-1:
                list_s+=[element_in_s]
            i+=1
        for y in list_s:
            for z in topic:
                if y==z:
                    return True
        return False
    return helper
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    list_typed=[x for x in split(typed) if x!='']
    list_reference=[x for x in split(reference) if x!='']
    i,right_times=0,0
    for i in range(min(len(list_typed),len(list_reference))):
        if list_typed[i]==list_reference[i]:
            right_times+=1
    if len(list_typed)==0:
        return 0.0
    elif len(list_typed)==0 and len(list_reference)==0:
        return 100.0
    else:
        return right_times/len(list_typed)*100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    total=len(typed)
    time=(total/5)/(elapsed/60)
    return time
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        difference=[]
        for valid_word in valid_words:
            difference+=[diff_function(user_word,valid_word,limit)]
        minimum=min(difference)
        if minimum>limit:
            return user_word
        else:
            return valid_words[difference.index(minimum)]
    # END PROBLEM 5


def sphinx_swap(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    start_list,goal_list=list(start),list(goal)
    def helper(start_list,goal_list,change_times):
        start_length,goal_length=len(start_list),len(goal_list)
        if start_length==0 or goal_length==0:
            return change_times+max(start_length,goal_length)
        s,g=start_list.pop(0),goal_list.pop(0)
        if s!=g:
            change_times+=1
        if change_times>limit:
            return change_times
        return helper(start_list,goal_list,change_times)
    return helper(start_list,goal_list,0)



    # END PROBLEM 6


def feline_fixes(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    if limit<0:
        return 1
    elif start==goal:
        return 0
    else:
        differ_index=None
        start_list,goal_list=list(start),list(goal)
        for i in range(min(len(start_list),len(goal_list))):
            if start_list[i]!=goal_list[i]:
                differ_index=i
                break
        if differ_index==None and len(start_list)>len(goal_list):
            return 1+feline_fixes(start_list[:-1], goal_list, limit-1)
        elif differ_index==None and len(start_list)<len(goal_list):
            return 1+feline_fixes(start_list+[goal_list[len(start_list)]], goal_list, limit-1)
        elif differ_index+1==min(len(start_list),len(goal_list)) and len(start_list)==len(goal_list):
            return 1
        else:
            add_diff = 1+feline_fixes(start_list[:differ_index]+[goal_list[differ_index]]+start_list[differ_index:],goal_list,limit-1)
            remove_diff = 1+feline_fixes(start_list[:differ_index]+start_list[differ_index+1:],goal_list,limit-1)
            substitute_diff = 1+feline_fixes(start_list[:differ_index]+[goal_list[differ_index]]+start_list[differ_index+1:],goal_list,limit-1)
            return min(add_diff,remove_diff,substitute_diff)


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    total=0
    for i in range(len(typed)):
        if typed[i]==prompt[i]:
            total+=1
        else:
            break
    ratio=total/len(prompt)
    send({'id':id,'progress':ratio})
    return ratio


    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    for j in range(len(times_per_player)):
        if len(times_per_player[j])==1:
            times_per_player[j]=[]
        else:
            for i in range(len(times_per_player[j])-1):
                times_per_player[j][i]=times_per_player[j][i+1]-times_per_player[j][i]
            times_per_player[j].remove(times_per_player[j][i+1])
    return game(words,times_per_player)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    result=[]
    for player_num in players:
        result.append([])
    for word_num in words:
        min_time=1000000
        index=0
        for player_num in players:
            if time(game,player_num,word_num)<min_time:
                min_time=time(game,player_num,word_num)
                index=player_num
        result[index].append(word_at(game,word_num))
    return result

    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
