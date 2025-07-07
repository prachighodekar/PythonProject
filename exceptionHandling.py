a = 5
b = 0
try:
    c =a/b                 #code which can give exception
except ZeroDivisionError:  #handles exception
    print("ZeroDivisionError")
except Exception as e:
    print(e)
finally:
    print("Finally")    #execute irrespective of exception