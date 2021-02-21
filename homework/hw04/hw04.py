this_file = __file__

# Mobiles

def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]

def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]

def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]

def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]

def is_arm(s):
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'

def length(s):
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]

def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]

def planet(size):
    """Construct a planet of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return ['planet',size]

def size(w):
    """Select the size of a planet."""
    assert is_planet(w), 'must call size on a planet'
    "*** YOUR CODE HERE ***"
    return w[1]

def is_planet(w):
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'

def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                              arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return (t, u, v)

def total_weight(m):
    """Return the total weight of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a planet"
        return total_weight(end(left(m))) + total_weight(end(right(m)))

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(arm(3, t), arm(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(arm(1, v), arm(1, w)))
    False
    >>> balanced(mobile(arm(1, w), arm(1, v)))
    False
    """
    "*** YOUR CODE HERE ***"
    L,R=left(m),right(m)
    length_left,length_right=length(L),length(R)
    end_left,end_right=end(L),end(R)
    torque_left,torque_right=0,0
    if is_planet(end_left):
        torque_left=length_left*size(end_left)
    else:
        if balanced(end_left):
            torque_left=length_left*total_weight(end_left)
        else:
            return False
    if is_planet(end_right):
        torque_right=length_right*size(end_right)
    else:
        if balanced(end_right):
            torque_right=length_right*total_weight(end_right)
        else:
            return False
    if torque_left==torque_right:
        return True
    else:
        return False

def totals_tree(m):
    """Return a tree representing the mobile with its total weight at the root.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    """
    "*** YOUR CODE HERE ***"
    weight=total_weight(m)
    L,R=left(m),right(m)
    end_left,end_right=end(L),end(R)
    weight_left,weight_right=total_weight(end_left),total_weight(end_right)
    if is_planet(end_left):
        branch_left=weight_left
    else:
        branch_left=totals_tree(end_left)
    if is_planet(end_right):
        branch_right=weight_right
    else:
        branch_right=totals_tree(end_right)
    if is_tree(branch_left) and is_tree(branch_right):
        return tree(weight,[branch_left,branch_right])
    elif is_tree(branch_left) and not is_tree(branch_right):
        return tree(weight,[branch_left,tree(branch_right)])
    elif not is_tree(branch_left) and is_tree(branch_right):
        return tree(weight,[tree(branch_left),branch_right])
    else:
        return tree(weight,[tree(branch_left),tree(branch_right)])

def replace_leaf(t, old, replacement):
    """Returns a new tree where every leaf value equal to old has
    been replaced with replacement.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('freya')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        freya
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    "*** YOUR CODE HERE ***"
    copy=copy_tree(t)
    def helper(T,old,replacement):
        if is_leaf(T):
            if label(T)==old:
                T[0]=replacement
        else:
            for x in branches(T):
                helper(x, old, replacement)
    helper(copy,old,replacement)
    return copy

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    incorrect_password=[]
    def withdraw_protection(amount,input_password):
        nonlocal balance,incorrect_password
        if len(incorrect_password)<3:
            if input_password==password:
                if amount>balance:
                    return 'Insufficient funds'
                else:
                    balance=balance-amount
                    return balance
            else:
                incorrect_password=incorrect_password+[input_password]
                return 'Incorrect password'
        else:
            result="Your account is locked. Attempts: "+str(incorrect_password)
            return result
    return withdraw_protection

def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    a=withdraw(0,old_pass)
    if type(a)==str:
        return a
    else:
        def helper(amount,password):
            if password==new_pass:
                return withdraw(amount,old_pass)
            else:
                return withdraw(amount,password)
        return helper





## Tree Methods ##
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

###################
# Extra Questions #
###################

def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

def str_interval(x):
    """Return a string representation of interval x.
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    p5,p6=min(p1,p2,p3,p4),max(p1,p2,p3,p4)
    return interval(p5,p6)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    "*** YOUR CODE HERE ***"
    p1 = lower_bound(x) - lower_bound(y)
    p2 = lower_bound(x) - upper_bound(y)
    p3 = upper_bound(x) - lower_bound(y)
    p4 = upper_bound(x) - upper_bound(y)
    p5,p6=min(p1,p2,p3,p4),max(p1,p2,p3,p4)
    return interval(p5,p6)


def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    assert lower_bound(y)*upper_bound(y)>0, 'divisor spans zero'
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def multiple_references_explanation():
    return """The multiple reference problem..."""

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    ideal_min_point=-b/(2*a)
    f=lambda x: a*x*x+b*x+c
    if a>0:
        if ideal_min_point>=lower_bound(x) and ideal_min_point<=upper_bound(x):
            p1=f(ideal_min_point)
            p2=max(f(lower_bound(x)),f(upper_bound(x)))
            return interval(p1,p2)
        elif ideal_min_point<lower_bound(x):
            p1=f(lower_bound(x))
            p2=f(upper_bound(x))
            return interval(p1,p2)
        elif ideal_min_point>upper_bound(x):
            p1=f(upper_bound(x))
            p2=f(lower_bound(x))
            return interval(p1,p2)
    elif a<0:
        if ideal_min_point>=lower_bound(x) and ideal_min_point<=upper_bound(x):
            p1=f(ideal_min_point)
            p2=min(f(lower_bound(x)),f(upper_bound(x)))
            return interval(p2,p1)
        elif ideal_min_point<lower_bound(x):
            p1=f(lower_bound(x))
            p2=f(upper_bound(x))
            return interval(p2,p1)
        elif ideal_min_point>upper_bound(x):
            p1=f(upper_bound(x))
            p2=f(lower_bound(x))
            return interval(p2,p1)
