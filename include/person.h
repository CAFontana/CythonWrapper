#ifndef PERSON_H
#define PERSON_H

typedef struct {
    char name[50];
    int age;
} Person;

Person* create_person(const char* name, int age);
int age(Person* p);
void free_person(Person* p);

#endif