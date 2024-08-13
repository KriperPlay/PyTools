# PyTools
![image](https://github.com/user-attachments/assets/f98d4591-809c-4d30-ba4a-8c3c49d89297)

# About

PyTools - python lib with simple tools for logging,testing and information of func

# How to install

# How to use

# A little examples
All examples in dir 'examples'

* Simple unitest
* * ```python
    from pytools import Testing
    
    def plus(a,b):
        return a-b
    
    def minus(a,b):
        return a+b
    
    def mult(a,b):
        return a*b
    
    q = Testing()
    q.assertt(4,plus,2,2)
    q.assertt(20,minus,30,10)
    q.assertt(10,mult,5,2)
    q.print_tests()
    ```
* Source code of func
* * ```python
    from pytools import InfoFunc

    def plus(a,b):
      return a+b

    print(InfoFunc(plus,__file__).code)
    ```
* Logging #1
* * ```python
    from pytools import Logger
    
    def div(a,b):
        return a/b
    
    q = Logger()
    print(q.FullLog(div,2,0))
    ```
* Logging #2
* * ```python
    from pytools import logging

    @logging
    def div(a,b):
        return a/b
    
    div(2,0)
    ```

# End
