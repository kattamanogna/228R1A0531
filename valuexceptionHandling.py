try:
      a=int(input("enter a value"))
      b=int(input("enter b value"))
      c=a/b
      w = a + b
      d = [10, 20, 30]
      print(d[5])

except ZeroDivisionError:
     print("zero division error")
except NameError:
    print(" value not given")#value exception
except ValueError:
    print("value error")
except IndexError:
    print("Array index out of bounds")
except KeyError:
    print("key not found error")
except IOError:
    print("Input and output error")