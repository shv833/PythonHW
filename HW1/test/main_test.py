"""This module is for testing my teammate`s tasks"""
import unittest

from main import task_86a, task_86b, task_330


class Task86aTests(unittest.TestCase):
    """This class is for testing function task_86a"""

    def test_task86a_valid(self):
        """This method is for testing the correct result"""
        self.assertEqual(task_86a(928322), 6)

    def test_task86a_type(self):
        """This method is for testing the TypeError"""
        with self.assertRaises(TypeError):
            task_86a("!22")
        with self.assertRaises(TypeError):
            task_86a([])

    def test_task86a_value(self):
        """This method is for testing the ValueError"""
        with self.assertRaises(ValueError):
            task_86a(0)
        with self.assertRaises(ValueError):
            task_86a(-23)

    def test_task86a_negative(self):
        """This method is for testing the incorrect result"""
        self.assertNotEqual(task_86a(928), 6)


class Task86bTests(unittest.TestCase):
    """This class is for testing function task_86b"""

    def test_task86b_valid(self):
        """This method is for testing the correct result"""
        self.assertEqual(task_86b(928322), 26)

    def test_task86b_type(self):
        """This method is for testing the TypeError"""
        with self.assertRaises(TypeError):
            task_86b("!22")
        with self.assertRaises(TypeError):
            task_86b([])

    def test_task86b_value(self):
        """This method is for testing the ValueError"""
        with self.assertRaises(ValueError):
            task_86b(0)
        with self.assertRaises(ValueError):
            task_86b(-23)

    def test_task86b_negative(self):
        """This method is for testing the incorrect result"""
        self.assertNotEqual(task_86b(928), 6)


class Task330Tests(unittest.TestCase):
    """This class is for testing function task_86b"""

    def test_task330_valid(self):
        """This method is for testing the correct result"""
        self.assertEqual(task_330(9000), [6, 28, 496, 8128])

    def test_task330_type(self):
        """This method is for testing the TypeError"""
        with self.assertRaises(TypeError):
            task_330("!22")
        with self.assertRaises(TypeError):
            task_330([])

    def test_task330_value(self):
        """This method is for testing the ValueError"""
        with self.assertRaises(ValueError):
            task_330(0)
        with self.assertRaises(ValueError):
            task_330(-23)

    def test_task330_negative(self):
        """This method is for testing the incorrect result"""
        self.assertNotEqual(task_330(9000), [6, 28, 496, 8128, 33550336])


if __name__ == '__main__':
    unittest.main()
