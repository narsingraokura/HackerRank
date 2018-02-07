'''
Created on Feb 7, 2018

@author: kuran
'''
import unittest
from Introduction import intro

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testSimple(self):
        t1 = intro()
        feed = ""
        expected = "Hello, World!"
        output =  t1.helloWorld()        
        self.assertEqual(expected, output, "Failed for positives. expected %s for input %s, but received %s" % (expected, feed, output))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSimple']
    unittest.main()