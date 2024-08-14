

# █▀█ █▄█ ▀█▀ █▀█ █▀█ █░░ █▀   █▄▄ █▄█   █▀█ █▀█ █▀▀ █▀▀
# █▀▀ ░█░ ░█░ █▄█ █▄█ █▄▄ ▄█   █▄█ ░█░   ▀▀█ █▄█ █▀░ █▀░

from datetime import datetime
import traceback as tr
import json

error_descriptions = {
    "ValueError": "Occurs when a function receives an argument of the right type but an inappropriate value.",
    "TypeError": "Occurs when an operation or function is applied to an object of inappropriate type.",
    "IndexError": "Occurs when an index is out of range for a sequence.",
    "KeyError": "Occurs when a key is not found in a dictionary.",
    "AttributeError": "Occurs when an attribute or method is not found for an object.",
    "NameError": "Occurs when a variable or function is not defined.",
    "ZeroDivisionError": "Occurs when there is an attempt to divide by zero.",
    "FileNotFoundError": "Occurs when the program tries to open a file that does not exist.",
    "ImportError": "Occurs when a module cannot be imported.",
    "SyntaxError": "Occurs when there is a syntax error in the code that prevents it from being parsed.",
    "RuntimeError": "Occurs when an error is detected during execution that does not fall into other categories."
}

def func_code(func, file) -> str:
    line_no = 0
    first_line = func.__code__.co_firstlineno
    code = ""
    with open(file) as f:
        lines = f.readlines()
        for line in lines[first_line:]:
            line_no += 1
            if "    " not in line:
                last_line = line_no
                break
        for line in lines[first_line - 1: first_line + last_line - 1]:
            code = code + line
    return code 


def logging(func: callable) -> callable:
    """Decorator for logging functions"""
    def wrapped(*args,**kwargs):
        current_time = datetime.now().strftime("%H:%M:%S")

        try:
            return func(*args,**kwargs)
        except Exception as e:
            error = tr.TracebackException(exc_type =type(e),exc_traceback = e.__traceback__ , exc_value =e).stack[-1]
            log = f"Error: {e}\nTime: {current_time}\nLineNum: {error.lineno}\nLine: {error.line}"
            print(log)
    return wrapped

def logging_to_file(file: str) -> callable:
    def decorator(func: callable) -> callable:
        def wrapped(*args,**kwargs):
            current_time = datetime.now().strftime("%H:%M:%S")

            try:
                return func(*args,**kwargs)
            except Exception as e:
                error = tr.TracebackException(exc_type =type(e),exc_traceback = e.__traceback__ , exc_value =e).stack[-1]
                log = f"Error: {e}\nTime: {current_time}\nLineNum: {error.lineno}\nLine: {error.line}\n"
                file1 = open(file, 'a')
                file1.write(log)
        return wrapped
    return decorator

def logging_full(func: callable) -> callable:
    def wrapped(*args, **kwargs):
        current_time = datetime.now().strftime("%H:%M:%S")
        try:
            func(*args, **kwargs)
        except Exception as e:
            error = tr.TracebackException(exc_type =type(e),exc_traceback = e.__traceback__ , exc_value =e).stack[-1]
            for error1,desc in error_descriptions.items():
                if error1 == e.__class__.__name__:
                    log2 = error1
                    desc2 = desc
            log = f"Name: {log2}\nError: {e}\nTime: {current_time}\nLineNum: {error.lineno}\nLine: {error.line}\nDescription: {desc2}"
            print(log)  
    return wrapped

class Testing:
    def __init__(self) -> None:
        self.iter = 0
        self.test_dict = {}

    def assertt(self,result,func: callable,*args,**kwargs):
        if func(*args,**kwargs) == result:
            self.iter += 1
            self.test_dict[f"Test {self.iter} passed"] = f"{func.__name__}{func.__code__.co_varnames[:func.__code__.co_argcount]}"
        else:
            self.iter += 1
            self.test_dict[f"Test {self.iter} fail"] = f"{func.__name__}{func.__code__.co_varnames[:func.__code__.co_argcount]}"
        
    def print_tests(self):
        for test,func_name in self.test_dict.items():
            if "passed" in test:
                print("\033[32m{}".format(f"{func_name} = {test}"))
            else:
                print("\033[31m{}".format(f"{func_name} = {test}"))
        print("\033[0m")

    def simple_tests(self):
        for test,func_name in self.test_dict.items():
            print(test)

class Logger:
    def __init__(self) -> None:
        self.current_time = datetime.now().strftime("%H:%M:%S")
        self.log2 = None
        self.desc2 = None
    def TimeLog(self,func,Lines:str,*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            error = tr.TracebackException(exc_type =type(e),exc_traceback = e.__traceback__ , exc_value =e).stack[-1]
            if Lines == "Line":
                log = f"Error: {e}\nTime: {self.current_time}\nLine: {error.line}"
            if Lines == "Lineno":
                log = f"Error: {e}\nTime: {self.current_time}\nLineNum: {error.lineno}"
            if Lines == "Line&No":
                log = f"Error: {e}\nTime: {self.current_time}\nLineNum: {error.lineno}\nLine: {error.line}"
            return log
    
    def TimeLogWrite(self,func,Lines:str,file:str,*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            file0 = open(file,'a')
            file0.write(self.TimeLog(func,Lines), end = '\n')
            file0.close()
    
    def FullLog(self,func,*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            error = tr.TracebackException(exc_type =type(e),exc_traceback = e.__traceback__ , exc_value =e).stack[-1]
            log = f"Name: {self.log2}\nError: {e}\nTime: {self.current_time}\nLineNum: {error.lineno}\nLine: {error.line}\nDescription: {self.desc2}"
            for error1,desc in error_descriptions.items():
                if error1 == e.__class__.__name__:
                    self.log2 = error1
                    self.desc2 = desc
            log = f"Name: {self.log2}\nError: {e}\nTime: {self.current_time}\nLineNum: {error.lineno}\nLine: {error.line}\nDescription: {self.desc2}"
            return log  
    
    def DictLog(self,func,*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            error = tr.TracebackException(exc_type =type(e),exc_traceback = e.__traceback__ , exc_value =e).stack[-1]
            log = {"name": str(e.__class__.__name__), "error": str(e), "time": self.current_time, "lineno": error.lineno, "line": error.line}
            return log
        else:
            log = {"name": None, "error": None, "time": None, "lineno": None, "line": None}
            return log

    #Beta function    
    def JsonLog(self,func,file,*args,**kwargs):
        log = self.DictLog(func,*args,**kwargs)
        if log != None:
            with open(file, 'w') as json_file:
                json.dump(log,json_file, indent=4)
                json_file.write('\n')
        else:
            pass

class InfoFunc:
    def __init__(self,func,file) -> None:
        self.func0 = func
        self.doc = self.func0.__doc__
        self.args = self.func0.__defaults__
        self.callable = callable(self.func0)
        self.param_names = self.func0.__code__.co_varnames[:self.func0.__code__.co_argcount]
        self.func_name = self.func0.__name__
        self.annot = self.func0.__annotations__
        self.code = self.func_code(func,file)
    
    def func_code(self,func, file):
        line_no = 0
        first_line = func.__code__.co_firstlineno
        code = ""
        with open(file) as f:
            lines = f.readlines()
            for line in lines[first_line:]:
                line_no += 1
                if "    " not in line:
                    last_line = line_no
                    break
            for line in lines[first_line - 1: first_line + last_line - 1]:
                code = code + line
        return code 

