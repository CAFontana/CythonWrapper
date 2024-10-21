#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "person.h"

Person* create_person(const char* name, int age) {
    Person* p = (Person*)malloc(sizeof(Person));
    strncpy(p->name, name, 49);
    p->name[49] = '\0';
    p->age = age;
    return p;
}

int age(Person* p) {
    return &p->age;
}

void free_person(Person* p) {
    free(p);
}