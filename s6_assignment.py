import inspect

def docstring_calculation(fn:'function', / ,number_of_char:'int') -> 'function':
    """_summary_

    Args:
        fn (function): takes any function as input
        number_of_char (int, optional): Defaults to 50.

    Raises:
        TypeError: Only integer type arguments are allowed
        TypeError: Only function type positional arguments are allowed"

    Returns:
        function: function that checks the length of the docstring of the function given as input
    """
    # checks if the number_of_char is present or not
    if number_of_char is None:
        number_of_char = 50
    
    # checks if the number_of_char is an integer
    if not isinstance(number_of_char, int):
        raise TypeError ("Only integer type arguments are allowed")
    
    # checks if positional only arguments are present in the function
    sig = inspect.signature(docstring_calculation)
    params = sig.parameters.values()
    has_POSITION_ONLY = any([True for param in params if param.kind == param.POSITIONAL_ONLY])
    if fn is None or not callable(fn) or not has_POSITION_ONLY:
        raise TypeError("Only function type positional arguments are allowed")
        
    def checking_docstring(): 
        # because the function we give to test can have n number of arguments
        nonlocal fn
        nonlocal number_of_char
        # print("function doc string", fn.__doc__)
        if fn.__doc__ is not None:
            if len(fn.__doc__) > number_of_char:
                return f"This function has a greater than {number_of_char} docstring"
            else:
                return f"This function has a less than {number_of_char} docstring"
            
    return checking_docstring


def next_fibonacci(n:int,/) -> 'list':
    """
    Generates the next 'n' Fibonacci numbers.
    
    Args:
        n (int): The number of Fibonacci numbers to generate.
        
    Returns:
        list: A list containing the next 'n' Fibonacci numbers.
        
    Raises:
        TypeError: If the input 'n' is not an integer.
        ValueError: If the input 'n' is not a positive integer.
    """
    # Check if the input 'n' is an integer
    if not isinstance(n, int):
        raise TypeError("Only integer type arguments are allowed")
    # Check if the input 'n' is a positive integer
    if not n > 0:
        raise ValueError("Only positive integers are allowed")

    def fibseries():
        nonlocal n
        fib_list = [1, 1] # create a list with first two fibonacci numbers
        
        if n <= 2: # if n is less than or equal to 2, return the first two fibonacci numbers
            return 1
        
        else:
            for i in range(2, n):
                fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list
    
    return fibseries
    

counters = dict()
def counter(fn:'function',/) -> 'function':
    """_summary_ :
    
    closure that counts how many times a function was called.
    global dictionary variable with the count that can keep track of how many times add/mul/div functions were called 

    Args:
        fn (function): function that can accept any number of arguments and return a value

    Returns:
        function: global dictionary that keeps track of the number of times the function has been called
    """
    from functools import wraps
    import inspect
        
    cnt = 0  # initially fn has been run zero times
    
    if fn is None or not callable(fn):
        raise TypeError("Callable function is not present")
    
    # check if the function name is present in the dictionary
    if fn.__name__ not in counters:
        counters[fn.__name__] = cnt # add the function name to the dictionary
    else:
        cnt = counters[fn.__name__] # if function name is present, get the counter value from the dictionary
        
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal cnt        
        # increment the counter
        cnt = cnt + 1
        counters[fn.__name__] = cnt  # counters is global
        # print(f"Function {fn.__name__} has been called {cnt} times")
        # print(f"Total number of times all functions have been called {sum(counters.values())}")
        # print(f"All the functions that have been called are {counters.keys()}")
        # print(f"All the functions that have called and their respective number of times are {counters}")
        return counters
    return inner

def default_counter(fn,/,counter_dict: dict) -> 'function':
    """_summary_ :
    
    closure that counts how many times a function was called.
    global dictionary variable with the count that can keep track of how many times add/mul/div functions were called 

    Args:
        fn (function): function that can accept any number of arguments and return a value

    Returns:
        function: global dictionary that keeps track of the number of times the function has been called
    """
    from functools import wraps
    import inspect
    
    # checks if counter_dict is dictionary or not
    if not isinstance(counter_dict, dict):
        raise TypeError("Only dictionary type arguments are allowed")
    
    # checks if the function is callable or not
    if fn is None or not callable(fn):
        raise TypeError("Callable function is not present")
    
    # sig = inspect.signature(counter)
    # params = sig.parameters.values()
    # has_POSITION_ONLY = any([True for param in params if param.kind == param.POSITIONAL_ONLY])
    # if not has_POSITION_ONLY:
    #     raise TypeError("Only positional arguments are allowed for function")
    
    # checks for function name from input fuction
    fn_name = fn.__name__
    
    # checks if the function is a default function or not
    for func in counter_dict:
        if fn_name not in counter_dict:
            raise ValueError("Only default functions are allowed to run")
        
    # Gets corresponding counter value from the dictionary
    # take values from dictionary and then start counter on top of that value
    cnt = counter_dict[fn_name] 
        
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal counter_dict
        nonlocal cnt
        cnt = cnt + 1 # increment the counter
        counter_dict[fn.__name__] = cnt  # add the counter value to the dictionary corresponding to the function name
        # print(f"Function {fn.__name__} has been called {cnt} times")
        # print(f"Total number of times all functions have been called {sum(counters.values())}")
        # print(f"All the functions that have been called are {counters.keys()}")
        # print(f"All the functions that have called and their respective number of times are {counters}")
        return counter_dict
    
    return inner