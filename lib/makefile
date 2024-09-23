hellomake: hello_world.o 
	gcc -c hello_world.c
	ar rcs libhello_world.a hello_world.o
	gcc -o my_program my_program.c -L. -lhello_world