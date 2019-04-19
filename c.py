#coding=utf-8

import sys
import ctypes

def cstr_encode(args_string):
    '''Encode by utf-8 in PY3.'''
    if sys.version_info >= (3, 0):
        args_string = args_string.encode('utf-8')
    return args_string

mod = ctypes.cdll.LoadLibrary("./goso.so")

callbackfunc = ctypes.CFUNCTYPE(None,ctypes.c_char_p)

BoxHelloCallBack = mod.BoxHelloCallBack 
BoxHelloCallBack.argtypes = [ctypes.c_void_p,ctypes.c_char_p]

def callbackReal(message):
    print "this is call back from C language! %s " % (str(message))

## 包装成为c语言里调用的函数指针，用来从so中回调
cb_to_c = callbackfunc(callbackReal)

## 调用so 里的函数,除了传递参数以外 , 还传递了函数回调,
BoxHelloCallBack(cb_to_c,cstr_encode(" \n hello message from python !"))
