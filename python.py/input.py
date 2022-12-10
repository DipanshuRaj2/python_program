from ctypes import _NamedFuncPointer


if _NamedFuncPointer == '_main_':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)