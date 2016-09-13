#!/usr/bin/env python
# coding=utf-8

import unittest
import animal_q

input = """e4e87cb2-8e9a-4749-abb6-26c59344dfee
2016/09/02 22:30:46
cat1 10 9

351055db-33e6-4f9b-bfe1-16f1ac446ac1
2016/09/02 22:30:52
cat1 10 9 2 -1
cat2 2 3

dcfa0c7a-5855-4ed2-bc8c-4accae8bd155
2016/09/02 22:31:02
cat1 12 8 3 4"""

output = """cat1 15 12
cat2 2 3"""

id = "dcfa0c7a-5855-4ed2-bc8c-4accae8bd155"

class DemoTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testparse(self):
        self.assertEqual(animal_q.parse_file(input,id), output)

if __name__ == '__main__' :
    unittest.main()

