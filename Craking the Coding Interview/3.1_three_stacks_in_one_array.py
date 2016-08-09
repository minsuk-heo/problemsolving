import unittest

"""
array has three stacks inside

"""

class stacks_in_array():
    def __init__(self, stack_size):
        #create three stacks in the array and give input stack size on each stack
        self.array = [None] * stack_size * 3
        self.stack_size = stack_size

        self.stack1_bottom = 0
        self.stack1_top = self.stack1_bottom + self.stack_size

        self.stack2_bottom = self.stack1_top
        self.stack2_top = self.stack2_bottom + self.stack_size

        self.stack3_bottom = self.stack2_top
        self.stack3_top = self.stack3_bottom + self.stack_size

        self.stack1_idx = 0
        self.stack2_idx = self.stack1_idx + self.stack_size
        self.stack3_idx = self.stack2_idx + self.stack_size

    def push_stack1(self, val):
        if self.stack1_idx == self.stack1_top:
            print("stack1 is full")
            return False
        else:
            self.array[self.stack1_idx] = val
            self.stack1_idx = self.stack1_idx + 1
            return True

    def push_stack2(self, val):
        if self.stack2_idx == self.stack2_top:
            print("stack2 is full")
            return False
        else:
            self.array[self.stack2_idx] =  val
            self.stack2_idx = self.stack2_idx + 1
            return True

    def push_stack3(self, val):
        if self.stack3_idx == self.stack3_top:
            print("stack3 is full")
            return False
        else:
            self.array[self.stack3_idx] =  val
            self.stack3_idx = self.stack3_idx + 1
            return True

    def pop_stack1(self):
        if self.stack1_idx > self.stack1_bottom:
            self.stack1_idx = self.stack1_idx - 1
            self.array[self.stack1_idx] = None
            return True
        else:
            print("stack1 is empty")
            return False

    def pop_stack2(self):
        if self.stack2_idx > self.stack2_bottom:
            self.stack2_idx = self.stack2_idx - 1
            self.array[self.stack2_idx] = None
            return True
        else:
            print("stack1 is empty")
            return False

    def pop_stack3(self):
        if self.stack3_idx > self.stack3_bottom:
            self.stack3_idx = self.stack3_idx - 1
            self.array[self.stack3_idx] = None
            return True
        else:
            print("stack3 is empty")
            return False


    def printArray(self):
        return str(self.array)

class stacktest(unittest.TestCase):
    def test(self):
        test_array = stacks_in_array(3)
        self.assertEqual("[None, None, None, None, None, None, None, None, None]", test_array.printArray())
        test_array.push_stack1(1)
        test_array.push_stack2(1)
        test_array.push_stack3(1)
        self.assertEqual("[1, None, None, 1, None, None, 1, None, None]", test_array.printArray())
        test_array.push_stack1(2)
        test_array.push_stack2(2)
        test_array.push_stack3(2)
        self.assertEqual("[1, 2, None, 1, 2, None, 1, 2, None]", test_array.printArray())
        test_array.push_stack1(3)
        test_array.push_stack2(3)
        test_array.push_stack3(3)
        self.assertEqual("[1, 2, 3, 1, 2, 3, 1, 2, 3]", test_array.printArray())

        self.assertFalse(test_array.push_stack1(3))
        self.assertFalse(test_array.push_stack2(3))
        self.assertFalse(test_array.push_stack3(3))

        test_array.pop_stack1()
        test_array.pop_stack2()
        test_array.pop_stack3()
        self.assertEqual("[1, 2, None, 1, 2, None, 1, 2, None]", test_array.printArray())

        test_array.pop_stack1()
        test_array.pop_stack2()
        test_array.pop_stack3()
        self.assertEqual("[1, None, None, 1, None, None, 1, None, None]", test_array.printArray())

        test_array.pop_stack1()
        test_array.pop_stack2()
        test_array.pop_stack3()
        self.assertEqual("[None, None, None, None, None, None, None, None, None]", test_array.printArray())

        self.assertFalse(test_array.pop_stack1())
        self.assertFalse(test_array.pop_stack2())
        self.assertFalse(test_array.pop_stack3())



