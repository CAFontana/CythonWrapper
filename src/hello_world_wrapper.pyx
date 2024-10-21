cdef extern from "hello_world.h":
    void hello_world(char* person)

def py_hello_world(char* person):
    hello_world(person)