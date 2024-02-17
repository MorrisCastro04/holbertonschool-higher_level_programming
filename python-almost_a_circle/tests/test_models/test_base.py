#!/usr/bin/python3
"""Unittest class base"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square

class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """Set up for test cases"""
        Base._Base__nb_objects = 0

    def test_init_without_id(self):
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

    def test_init_with_id(self):
        b1 = Base(5)
        self.assertEqual(b1.id, 5)

    def test_to_json_string(self):
        r1 = Rectangle(4, 7)
        dictionary = r1.to_dictionary()
        json_str = Base.to_json_string([dictionary])
        self.assertEqual(json_str, '[{"x": 0, "width": 4, "id": 1, "height": 7, "y": 0}]')

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 7)
        Rectangle.save_to_file([r1])
        with open('Rectangle.json', 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"x": 2, "width": 10, "id": 7, "height": 7, "y": 8}]')

    def test_from_json_string(self):
        json_str = '[{"x": 2, "y": 8, "id": 1, "width": 10, "height": 7}]'
        obj_list = Base.from_json_string(json_str)
        self.assertEqual(len(obj_list), 1)

    def test_create(self):
        r1 = Rectangle(3, 5, 1, 1)
        dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**dictionary)
        self.assertEqual(r1 == r2, False)
        self.assertEqual(r1 is r2, False)
        self.assertNotEqual(r1, r2)

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r1])
        list_rect = Rectangle.load_from_file()
        self.assertEqual(len(list_rect), 1)
        self.assertEqual(list_rect[0].id, 5)

if __name__ == '__main__':
    unittest.main()