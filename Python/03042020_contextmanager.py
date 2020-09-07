# context manager -> a function that'll handle the opening/closing or protecting/unprocteting o
# of files stuff for me

class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print('enter')
        return self.file

    def __exit__(self, type, value, traceback):
        print('exit \n')
        self.file.close()


with File('text.txt', 'w') as f:
    f.write('Hello')
    print('middle')


#other way of doing this is with a generator. I have to use contextlib.contextmanager for this
from contextlib import contextmanager

@contextmanager
def file(filename, method):
    print('enter')
    file = open(filename, method)
    yield file
    print('exit')
    file.close()

with file('text1.txt', 'w') as f:
    f.write('hey there')
    print('middle')