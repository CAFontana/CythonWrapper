import sys
import os

# Add the current directory to Python's module search path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Current working directory: {os.getcwd()}")
print(f"Contents of current directory: {os.listdir('.')}")
print(f"Python path: {sys.path}")

try:
    import hello_world_wrapper
    import person_wrapper
    print("hello_world_wrapper imported successfully")

    person = person_wrapper.PyPerson(b"John Doe", 30)
    hello_world_wrapper.py_hello_world(person.print_info())
except ImportError as e:
    print(f"Failed to import hello_world_wrapper: {e}")
    sys.exit(1)