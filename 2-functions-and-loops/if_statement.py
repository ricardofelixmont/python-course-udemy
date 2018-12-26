# On those examples we can realize that we can use boolean logic like in math.
is_programer = False
is_awesome = False

if is_programer: # It's the same of 'if is_programer is True:'
    print('You\'re the best')
if is_awesome:   # It's the same of 'if is_awesome is True:'
    print('You\'re awesome')

if is_programer or is_awesome: 
    print('Be awesome')
if not(is_programer or is_awesome): # It's the same of 'if not(is_programer == True or is_awesome == True):'
    print('Be awesome 2')

if not(is_programer == True or is_awesome == True):
    print('Be awesome 3')


# COMO FUNCIONA O IF STATEMENT?
# In if statement whats happens is that the <condition> is inside a bool() function. 
# Essentially something like this:
if is_programer is False:
    print('Block')
# is the same of:
if bool(is_programer is False) is True:
    print('Block')

# Another example
# if 5: is the same of if bool(5) is True:
# if 'Hello world': is the same of if bool('Hello world') is True:

# That ensures we're comparing apples to apples and not apples to oranges.

# if statements most return us True, but there are few cases where it returns us False:
# for example:
# bool(0)
# bool(0.0)
# bool(' ') empty string
# bool(None)
# bool([])  empty list  
# There're some other cases, but these ones are the most commoms.   
