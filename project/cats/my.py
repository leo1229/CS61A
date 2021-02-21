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
        start_list,goal_list=list(start),list(goal)
        for i in range(min(len(start_list),len(goal_list))):
            if start_list[i]!=goal_list[i]:
                break
        if i+1==min(len(start_list),len(goal_list)) and len(start_list)>len(goal_list):
            return 1+feline_fixes(start_list[:-1], goal_list, limit-1)
        elif i+1==min(len(start_list),len(goal_list)) and len(start_list)<len(goal_list):
            return 1+feline_fixes(start_list+[goal_list[len(start_list)]], goal_list, limit-1)
        elif i+1==min(len(start_list),len(goal_list)) and len(start_list)==len(goal_list):
            return 1+feline_fixes(start_list[:-1]+[goal_list[-1]], goal_list, limit-1)
        else:
            add_diff = 1+feline_fixes(start_list[:i]+[goal_list[i]]+start_list[i:],goal_list,limit-1)
            remove_diff = 1+feline_fixes(start_list[:i]+start_list[i+1:],goal_list,limit-1)
            substitute_diff = 1+feline_fixes(start_list[:i]+[goal_list[i]]+start_list[i+1:],goal_list,limit-1)
        return min(add_diff,remove_diff,substitute_diff)
