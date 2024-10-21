from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("hello_world_wrapper",
              sources=["hello_world_wrapper.pyx"],
              libraries=["hello_world"],
              library_dirs=["../lib"],
              include_dirs=["../include"]),
    Extension("person_wrapper",
              sources=["person_wrapper.pyx", "person.c"],
              library_dirs=["../lib"],
              include_dirs=["../include"])
]

setup(
    ext_modules=cythonize(extensions)
)