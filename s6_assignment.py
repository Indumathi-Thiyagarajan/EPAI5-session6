import inspect
from functools import wraps

def docstring_calculation(fn: 'function', / , number_of_char: 'int' = 50) -> 'function':
    """_summary_

    Args:
        fn (function): takes any function as input
        number_of_char (int, optional): Defaults to 50.

    Raises:
        TypeError: Only integer type arguments are allowed
        TypeError: Only function type positional arguments are allowed

    Returns:
        function: function that checks the length of the docstring of the function given as input
    """
    # checks if the number_of_char is an integer
    if not isinstance(number_of_char, int):
        raise TypeError("Only integer type arguments are allowed")
    
    # checks if positional only arguments are present in the function
    sig = inspect.signature(docstring_calculation)
    params = sig.parameters.values()
    has_POSITION_ONLY = any(param.kind == param.POSITIONAL_ONLY for param in params)
    if fn is None or not callable(fn) or not has_POSITION_ONLY:
        raise TypeError("Only function type positional arguments are allowed")
        
    def checking_docstring(): 
        # because the function we give to test can have n number of arguments
        nonlocal fn
        nonlocal number_of_char
        if fn.__doc__ is not None:
            if len(fn.__doc__) > number_of_char:
                return f"This function has a greater than {number_of_char} docstring"
            else:
                return f"This function has a less than {number_of_char} docstring"
            
    return checking_docstring


def next_fibonacci(n: int, /) -> 'list':
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
    if n <= 0:
        raise ValueError("Only positive integers are allowed")

    def fibseries():
        nonlocal n
        fib_list = [1, 1]  # create a list with first two Fibonacci numbers
        
        if n <= 2:  # if n is less than or equal to 2, return the first two Fibonacci numbers
            return fib_list[:n]
        
        for i in range(2, n):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list
    
    return fibseries


counters = dict()

def counter(fn: 'function', /) -> 'function':
    """_summary_ :
    
    Closure that counts how many times a function was called.
    Global dictionary variable with the count that can keep track of how many times add/mul/div functions were called.

    Args:
        fn (function): Function that can accept any number of arguments and return a value

    Returns:
        function: Global dictionary that keeps track of the number of times the function has been called
    """
    if fn is None or not callable(fn):
        raise TypeError("Callable function is not present")
    
    cnt = counters.get(fn.__name__, 0)  # get the count from the dictionary or initialize to 0
    
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal cnt        
        cnt += 1
        counters[fn.__name__] = cnt  # update the count in the dictionary
        return counters
    
    return inner

def default_counter(fn, /, counter_dict: dict) -> 'function':
    """_summary_ :
    
    Closure that counts how many times a function was called.
    Global dictionary variable with the count that can keep track of how many times add/mul/div functions were called.

    Args:
        fn (function): Function that can accept any number of arguments and return a value

    Returns:
        function: Global dictionary that keeps track of the number of times the function has been called
    """
    if not isinstance(counter_dict, dict):
        raise TypeError("Only dictionary type arguments are allowed")
    
    if fn is None or not callable(fn):
        raise TypeError("Callable function is not present")
    
    fn_name = fn.__name__
    
    if fn_name not in counter_dict:
        raise ValueError("Only default functions are allowed to run")
        
    cnt = counter_dict[fn_name]  # get the count from the dictionary
    
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1  # increment the counter
        counter_dict[fn_name] = cnt  # update the count in the dictionary
        return counter_dict
    
    return inner
