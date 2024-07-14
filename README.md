In this session6 I have learnt, what a closure function is, global and nonlocal scope, how to write test sessions for python script. 


# docstring_calculation:
REQUIREMENT : Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable (+ 4 tests) - 200

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

------------------------------------------------------------------------------------

# next_fibonacci
REQUIREMENT: Write a closure that gives you the next Fibonacci number (+ 2 tests) - 100

Generates the next 'n' Fibonacci numbers.
    
    Args:
        n (int): The number of Fibonacci numbers to generate.
        
    Returns:
        list: A list containing the next 'n' Fibonacci numbers.
        
    Raises:
        TypeError: If the input 'n' is not an integer.
        ValueError: If the input 'n' is not a positive integer.

-------------------------------------------------------------------------------------

# counter

REQUIREMENT: We wrote a closure that counts how many times a function was called. Write a new one that can keep track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts (+ 6 tests) - 250

"""_summary_ :
    
    closure that counts how many times a function was called.
    global dictionary variable with the count that can keep track of how many times add/mul/div functions were called 

    Args:
        fn (function): function that can accept any number of arguments and return a value

    Returns:
        function: global dictionary that keeps track of the number of times the function has been called
    """
-------------------------------------------------------------------------------------

# default_counter

REQUIREMENT:Modify above such that now we can pass in different dictionary variables to update different dictionaries (+ 6 tests) - 250

    Summary
    closure that counts how many times a function was called.
    global dictionary variable with the count that can keep track of how many times add/mul/div functions were called 

    Args:
        fn (function): function that can accept any number of arguments and return a value

    Returns:
        function: global dictionary that keeps track of the number of times the function has been called


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# TESTING:
We test each function for following criteria:
### README:
    1) check if readme file is present and inside readme file, we are checking if all the functions are explained, if number of words in readme is greater than 500, checking if readme file has more than 10 hashes.
   
### CODE SCRIPT:

    2) we are testing if our code script has proper indendation

### FUNCTION WISE TESTING:

    3) we are testing if each function is a closure, has doc_string, takes int when required, prints out TypeError when non-integer are inputed.
    4) each function is tested for boundary condition where it fails and sees if error messages are properly set up. 
    5) we have a ### counter and ### default_counter function. #counter function creates a dynamic global dictionary based on the function user is running
    6) # default_counter function takes dictionary as default value and updates the dictionary as it runs over the default functions present in the default value. 