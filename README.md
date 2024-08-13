# PyTools
![image](https://github.com/user-attachments/assets/f98d4591-809c-4d30-ba4a-8c3c49d89297)

# About

PyTools - python lib with simple tools for logging,testing and information of func

# How to install

# How to use

* Logging
* * Class Logging:
  * * TimeLog(self,func,Lines,*args,**kwargs) - func(func),Lines(choice option: "Line" - just Line where error; "Lineno" - just line number where error; "Line&no" - line and line number where error)
    * FullLog(self,func) - just full log of error
    * TimeLogWrite(self,func,Lines:str,file:str,*args, **kwargs) - same TimeLog, but writing in file 'file'
    * DictLog(self,func,*args, **kwargs) - same TimeLog, but return dictionary
    * JsonLog(self,func,file,*args,**kwargs) - same DictLog, but writing in json file 'file'
* * Class InfoFunc:
  * * InfoFunc(func,file) - example: InfoFunc(plus,__file__)
    * InfoFunc(func,file).doc - doc of func
    * InfoFunc(func,file).callable - is the function callable?
    * InfoFunc(func,file).code - source code func
    * InfoFunc(func,file).func_name - name of func
    * InfoFunc(func,file).annot - annotations of func
    * InfoFunc(func,file).args - default args of func
    * InfoFunc(func,file).param_names - names of all args of func
* * Class Testing:
  * * assertt(self,result,func: callable,*args,**kwargs) - ('result' - necessary result of func) simple unittest
    * print_test(self) - printing tests with colors and which test for which function
    * simple_tests(self) - just printing tests
* * Decorators:
  * * @logging_full - same Logger().FullLog(), but decorator and printing straightaway
    * @logging - same Logger.TimeLog(), but decorator and printing straightaway
    * @logging_to_file(file) - same Logger.TimeLogWrite(), but decorator

# A little examples

* Simple unittest
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
* Info of func
* * ```python
    from pytools import InfoFunc

    def a():
    """Testfunc"""
        return 0

    print(InfoFunc(a,__file__).doc)
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
* Logging #3
* * ```python
    from pytools import logging_to_file

    @logging_to_file("file.txt")
    def a():
        print( 2/0 )

    a()
    ```

# End
