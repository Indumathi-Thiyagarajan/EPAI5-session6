import pytest
import s6_assignment
import os
import inspect
import re
import math

from s6_assignment import docstring_calculation, next_fibonacci, counter, default_counter

def add(a, b):
    """This function takes two arguments and return their sum"""
    return a+b

def mul(a, b):
    """This function takes two arguments and return their product"""
    return a*b

def div(a, b):
    """This function takes two arguments and return their division"""
    return a/b
    
def test_session6_counter_functionality():
    """Test counter function for functionality """
    @counter
    def add(a, b):
        return a + b
    assert add(1, 2) == {'add': 1}, "Counter function not working as expected"
    
    @counter
    def mul(a, b):
        return a * b
    assert mul(3, 4) == {'add': 1, 'mul': 1}, "Counter function not working as expected"
    assert mul(5, 6) == {'add': 1, 'mul': 2}, "Counter function not working as expected"
    
    @counter
    def div(a, b):
        return a / b
    assert div(10, 2) == {'add': 1, 'mul': 2, 'div': 1}, "Counter function not working as expected"
    assert div(20, 4) == {'add': 1, 'mul': 2, 'div': 2}, "Counter function not working as expected"
    
def test_session6_default_counter_functionality():
    """Test default_counter function for functionality """
    
    counter_dict = {'add': 0, 'mul': 0, 'div': 0}

    @default_counter(counter_dict)
    def add(a, b):
        return a + b
    assert x(1,2) == {'add': 1, 'mul': 0, 'div': 0}, "Default Counter function not working as expected"
    
    @default_counter(counter_dict)
    def mul(a, b):
        return a * b
    assert mul(3, 4) == {'add': 1, 'mul': 1, 'div': 0}, "Default Counter function not working as expected"
    assert mul(5, 6) == {'add': 1, 'mul': 2, 'div': 0}, "Default Counter function not working as expected"
    
    @default_counter(counter_dict)
    def div(a, b):
        return a / b
    assert div(10, 2) == {'add': 1, 'mul': 2, 'div': 1}, "Default Counter function not working as expected"
    assert div(20, 4) == {'add': 1, 'mul': 2, 'div': 2}, "Default Counter function not working as expected"
    
README_CONTENT_CHECK_FOR = [
    'docstring_calculation',
    'next_fibonacci',
    'counter',
    'default_counter',
]



def test_session5_readme_exists():
    """ 
    Test function to see if the readme file exists
    """
    README_FILE_EXISTS = True
    if not os.path.isfile("README.md"):
        README_FILE_EXISTS = False
    
    assert README_FILE_EXISTS == True, "README.md file missing!"

def test_session5_readme_500_words():
    """ 
    Test function to see if the readme file has more than or equal to 500 words 
    """

    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    print(len(readme_words))
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_session5_readme_proper_description():
    """ 
    test function to see if all the functions are explained in the readme file
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"
    
def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10
    
def test_function_name_had_cap_letter():
    functions = inspect.getmembers(s6_assignment, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_session6_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(s6_assignment)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_session5_function_name_had_cap_letter():
    functions = inspect.getmembers(s6_assignment, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
        

####################################### ASSIGNMENT VARIABLE ##################################################################################################
   
def test_session6_docstring_fn_arg():
    """Test docstring_calculation function for mandatory positional arguments"""
    with pytest.raises(TypeError, match=r".*Only function type positional arguments are allowed'*"):
        s6_assignment.docstring_calculation(1, number_of_char=10)
    with pytest.raises(TypeError, match=r".*Only function type positional arguments are allowed'*"):
        s6_assignment.docstring_calculation([1,2,3],number_of_char=10)
    with pytest.raises(TypeError, match=r".*Only function type positional arguments are allowed'*"):
        s6_assignment.docstring_calculation("string",number_of_char=10)

def test_session6_docstring_number_of_Char_values():
    """Test docstring_calculation function for incorrect positional argumentst values for number of characters (check for string AND imaginary input) """
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed*"):
        s6_assignment.docstring_calculation(add,number_of_char='sac')
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed*"):
        s6_assignment.docstring_calculation(add,number_of_char=1+2j)
        
def test_session6_counters_global_var_counter():
    """Test counters function for global variable """
    
    code_object = counter(mul).__code__.co_names
    if 'counters' not in code_object:
        raise AssertionError("Global variable not present")
       
def test_session6_default_counter_dict():
    """ Test default_counter function for default dictionary values """
    with pytest.raises(TypeError, match=r".*Only dictionary type arguments are allowed'*"):
        s6_assignment.default_counter("add", counter_dict=1)
    with pytest.raises(TypeError, match=r".*Only dictionary type arguments are allowed'*"):
        s6_assignment.default_counter("add", counter_dict=[1,2,3])
       
def test_session6_counter_fn_callable():
    """Test counter function is callable"""
    with pytest.raises(TypeError, match=r".*Callable function is not present'*"):
        s6_assignment.counter(1)
    with pytest.raises(TypeError, match=r".*Callable function is not present'*"):
        s6_assignment.counter("print")
    with pytest.raises(TypeError, match=r".*Callable function is not present'*"):
        s6_assignment.counter("add")       

# def test_session6_default_counter_fn_arg():
#     """Test counter function for mandatory positional arguments"""
#     with pytest.raises(TypeError, match=r".*Only positional arguments are allowed for function'*"):
#         s6_assignment.default_counter(fn=add,counter_dict={'add': 20, 'mul': 3, 'div': 5})
#     with pytest.raises(TypeError, match=r".*Only positional arguments are allowed for function'*"):
#         s6_assignment.default_counter(fn=div,counter_dict={'add': 20, 'mul': 3, 'div': 5})
#     with pytest.raises(TypeError, match=r".*Only positional arguments are allowed for function'*"):
#         s6_assignment.default_counter(fn=mul,counter_dict={'add': 20, 'mul': 3, 'div': 5})
        
################################# TEST FOR FUNCTIONALITY ########################################
def test_session6_defult_counter_fn_callable():
    """Test counter function is callable"""
    with pytest.raises(TypeError, match=r".*Callable function is not present'*"):
        s6_assignment.default_counter(1, counter_dict={'add': 20, 'mul': 3, 'div': 5})
    with pytest.raises(TypeError, match=r".*Callable function is not present'*"):
        s6_assignment.default_counter("print", counter_dict={'add': 20, 'mul': 3, 'div': 5})
    with pytest.raises(TypeError, match=r".*Callable function is not present'*"):
        s6_assignment.default_counter("add", counter_dict={'add': 20, 'mul': 3, 'div': 5})
        
def test_next_fib_num_is_valid():
    """
    Test to check the numbers generated by next_fib_num is valid
    """
    from functools import reduce
    import random
    
    # check the number generate by next fib number is a valid fibonacci number
    fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [1, 1])
    fib_list = fib(20)
    result = s6_assignment.next_fibonacci(20)
    assert result() == fib_list, "Numbers generate are not in fibonacci series"
    
def test_session6_fib_series():
    """Test fib_series function for incorrect positional argumentst values for n (check for string AND imaginary input) """
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed*"):
        s6_assignment.next_fibonacci('sac')
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed*"):
        s6_assignment.next_fibonacci(1+2j)
        
def test_session6_fib_series_negative():
    """Test fib_series function for negative values of n """
    with pytest.raises(ValueError, match=r".*Only positive integers are allowed*"):
        s6_assignment.next_fibonacci(-1)
    with pytest.raises(ValueError, match=r".*Only positive integers are allowed*"):
        s6_assignment.next_fibonacci(-1224)
        

        


################################### TEST FOR CLOSURE ########################################

    
def test_closure_docstring_calculation():
    f1 = s6_assignment.docstring_calculation(add, 10)
    assert bool(f1.__closure__)==True, 'Closure is missing'        

def test_closure_counter():
   assert hasattr(s6_assignment.counter, '__closure__'), 'Closure is missing'
   
def test_closure_default_counter():
    dicts = {'add': 0, 'mul': 0, 'div': 0}
    f1 = s6_assignment.default_counter(add, dicts)
    assert bool(f1.__closure__)==True, 'Closure is missing'

def test_closure_next_fibonacci():
    f1 = s6_assignment.next_fibonacci(10)
    assert bool(f1.__closure__)==True, 'Closure is missing'
    

################################### TEST FOR DOC STRING ####################################

def test_docstring_docstring_calculation():
    assert len(s6_assignment.docstring_calculation.__doc__)>0, 'docstring is missing' 

def test_docstring_counter():
    assert len(s6_assignment.counter.__doc__)>0, 'docstring is missing'
    
def test_docstring_default_counter():
    assert len(s6_assignment.default_counter.__doc__)>0, 'docstring is missing'

def test_docstring_next_fibonacci():
    assert len(s6_assignment.next_fibonacci.__doc__)>0, 'docstring is missing'
    
