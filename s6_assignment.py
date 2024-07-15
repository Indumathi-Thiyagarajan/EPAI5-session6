import inspect
from functools import wraps


def docstring_calculation(fn: 'function', /, number_of_char: 'int' = 50) -> 'function':
    """Summary

    Args:
        fn (function): takes any function as input
        number_of_char (int, optional): Defaults to 50.

    Raises:
        TypeError: Only integer type arguments are allowed
        TypeError: Only function type positional arguments are allowed

    Returns:
        function: function that checks the length of the docstring of the function given as input
    """
    if not isinstance(number_of_char, int):
        raise TypeError("Only integer type arguments are allowed")
    
    sig = inspect.signature(docstring_calculation)
    params = sig.parameters.values()
    has_position_only = any(param.kind == param.POSITIONAL_ONLY for param in params)
    if fn is None or not callable(fn) or not has_position_only:
        raise TypeError("Only function type positional arguments are allowed")
        
    def checking_docstring(): 
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
    if not isinstance(n, int):
        raise TypeError("Only integer type arguments are allowed")
    if n <= 0:
        raise ValueError("Only positive integers are allowed")

    def fibseries():
        nonlocal n
        fib_list = [1, 1]
        if n <= 2:
            return fib_list[:n]
        for i in range(2, n):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list
    
    return fibseries


counters = dict()


def counter(fn: 'function', /) -> 'function':
    """Summary

    Closure that counts how many times a function was called.
    Global dictionary variable with the count that can keep track of how many times 
    add/mul/div functions were called.

    Args:
        fn (function): Function that can accept any number of arguments and return a value

    Returns:
        function: Global dictionary that keeps track of the number of times the function has been called
    """
    if fn is None or not callable(fn):
        raise TypeError("Callable function is not present")
    
    cnt = counters.get(fn.__name__, 0)
    
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal cnt        
        cnt += 1
        counters[fn.__name__] = cnt
        return counters
    
    return inner


def default_counter(fn, /, counter_dict: dict) -> 'function':
    """Summary

    Closure that counts how many times a function was called.
    Global dictionary variable with the count that can keep track of how many times 
    add/mul/div functions were called.

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
        
    cnt = counter_dict[fn_name]
    
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal cnt
        nonlocal fn, fn_name
        cnt += 1
        counter_dict[fn_name] = cnt
        return fn(*args, **kwargs)
    
    return inner
