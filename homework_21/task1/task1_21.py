import logging
import datetime as dt

class FileContextManager:
    counter = 0
    #lists = ['r', 'w', 'a']
    #lists_log = 'log.txt'
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.times = dt.datetime.now()
        self.file = open(filename, mode)

    @classmethod
    def get_init(cls):
        return cls.counter

    def __enter__(self):
        FileContextManager.counter += 1
        print(FileContextManager.counter)
        return self.file


    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        print(f"{dt.datetime.now()}")
        if exc_type is not None:
            logging.exception('exception')
        self.file.close()

with FileContextManager("test.txt", "a") as value:
    value.write("Hello World\n")

#with FileContextManager("test.txt", "a") as value:
#    value.write("Hello World\n")

#with FileContextManager("test.txt", "a") as value:
#    value.write("bye World\n")