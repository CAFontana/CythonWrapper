from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("hello_world_wrapper",
              sources=["hello_world_wrapper.pyx"],
              libraries=["hello_world"],
              library_dirs=["../lib"],
              include_dirs=["../lib"])
]

setup(
    ext_modules=cythonize(extensions)
)