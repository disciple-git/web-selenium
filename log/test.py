import traceback
import sys
import exception

list = [1,2,3,4]
print(list[7])
ex_type, ex_val, ex_stack = sys.exc_info()
print(ex_type )
print(ex_val)
