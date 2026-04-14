import sys
import os
import site

def is_venv():
    return sys.prefix != sys.base_prefix

def in_venv():
    print(f"Matrix Status: Welcome to the construct")
    print(f"Current python: {sys.executable}")
    print(f"Virtual environment: {os.path.basename(sys.prefix)}")
    print(f"Path to venv: {sys.prefix}")
    print("""\nSUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.\n""")
    print(f"Package installation path:\n{site.getsitepackages()[0]}")

def no_venv():
    print("Matrix Status: You're still plugged in")
    print(f"Current python: {sys.executable}")
    print(f"Virtual environement: Not found")
    print("""\nWARNING: You're in the global environment!
The machines can see everything you install.\n
To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate # On Windows
Then run this program again.""")


def main():
    try:
        if is_venv():
            in_venv()
        else:
            no_venv()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

