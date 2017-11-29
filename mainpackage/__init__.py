
#from main import main_func # uncomment this line to fail()
try:
   from main import main_func
    from aa import a
    from bb import b
    from cc import c
    from dd import d
except ImportError:
    pass 
