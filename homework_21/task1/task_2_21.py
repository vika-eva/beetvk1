import unittest
import task1_21

with open('test2.txt', 'a') as f:
    for i in range(4):
        f.write("hello python\n")

class TestTask2(unittest.TestCase):
    def test_open(self):
        with task1_21.FileContextManager('test2.txt', 'r') as f:
            self.assertTrue(f.readable())

    def test_close(self):
        with task1_21.FileContextManager('test2.txt', 'r') as f:
            print('close')
        self.assertTrue(f.closed)

    def test_read(self):
        with task1_21.FileContextManager('test2.txt', 'r') as f:
            test_str = f.readline()
        self.assertEqual('hello python\n', test_str)

    def test_write(self):
        with task1_21.FileContextManager('test2.txt', 'w') as f:
            test_text = 'hello python\n'
            f.write(test_text)
        with open('test2.txt') as f1:
            f1_read = f1.readlines()
        self.assertTrue(f1_read)

