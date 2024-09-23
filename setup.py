from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("hello_world_wrapper",
              sources=["hello_world_wrapper.pyx"],
              libraries=["hello_world"],
              library_dirs=["."],
              include_dirs=["."])
]

setup(
    ext_modules=cythonize(extensions)
)