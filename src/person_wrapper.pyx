cdef extern from "person.h":
    ctypedef struct Person:
        char name[50]
        int age
    
    Person* create_person(const char* name, int age)
    int age(Person* p)
    void free_person(Person* p)

cdef class PyPerson:
    cdef Person* c_person

    def __cinit__(self, bytes name, int age):
        self.c_person = create_person(name, age)

    def __dealloc__(self):
        if self.c_person is not NULL:
            free_person(self.c_person)

    def py_age(self):
        age(self.c_person)