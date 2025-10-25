# Many style violations: wildcard import, unused import, wrong naming, missing spaces, long line
from math import *
import os,sys

def badFunction():  # function name not snake_case
    x=1+2  # missing spaces around operators
    long_line = "This is a very long string intended to exceed the typical 79 character line length limit used by many linters and style guides."  # noqa: E501
    unused_var = 42
    print("Hello, wwww!")  
    return x
