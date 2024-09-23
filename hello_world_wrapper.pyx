cdef extern from "hello_world.h":
    void hello_world()

def py_hello_world():
    hello_world()