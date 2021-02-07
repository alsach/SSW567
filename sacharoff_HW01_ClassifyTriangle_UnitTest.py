# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:37:22 2021
SSW 567 Homeowrk 01
@author: Alisha Sacharoff
Code notes are not present below becuase the author prefer to write very detailed notes 
and finds that including the notes with the code makes the code messy and more difficult to follow.

Each program the author writes has a code description document that should be saves in the same location this code was saved in.
The file name is Sacharoff_HW01.xlsx

The code description document includes:
    Tab 1: Assignment Overview 
    Tab 2: a copy of the code below with detailed notes
    Tab 3: decision table for each function that traces to each test case and a description
    Tab 4: Test Case Summary detailing
        - test ID
        - inputs
        - resired output
        - acheived output
        - results of automated test
        - screen shots of test
    Tab 5: Unit Test Summary
    Tab 6: Summary of Experience


"""
import unittest

def is_trianlge (a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False
    
def triangle_type (a,b,c):
    if a==b and b==c:
        return True and print ('You have an Equilateral Triangle.')
    elif a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
        return True and print ('You have a Right Triangle')
    elif a==b or b==c or a==c:
        return True and print ('You have an Isosceles Triangle.')
    else:
        return True and print ('You have a Scalene Triangle')

length_a = float(input('Enter length of 1st side: '))
length_b = float(input('Enter length of 2nd side: '))
length_c = float(input('Enter length of last side: '))

if is_trianlge(length_a, length_b, length_c):
    triangle_type(length_a, length_b, length_c)

else:
    is_triangle = 'Triangle is not possible from given sides'
    print('Triangle is not possible from given sides')
    
class calctest(unittest.TestCase):
    def test_triangle_type_scalene(self):
        self.assertEqual(triangle_type(10,13,8), True and print ('You have a Scalene Triangle'))
        
    def test_triangle_type_isosceles(self):
        self.assertEqual(triangle_type(3,3,5), True and print ('You have an Isosceles Triangle.'))
    
    def test_triangle_type_right(self):
        self.assertEqual(triangle_type(3,4,5), True and print ('You have a Right Triangle'))
        
    def test_triangle_type_equilateral(self):
        self.assertEqual(triangle_type(8,8,8), True and print ('You have an Equilateral Triangle.'))
        
    def Test_is_trianlge_negative_sides(self):
        self.assertEqual(is_trianlge(-10,13,8), 'Triangle is not possible from given sides')
        
    def test_is_trianlge_letter(self):
        self.assertFalse(is_trianlge('a',13,8), 'Triangle is not possible from given sides')
        
    def test_is_trianlge_invalid(self):
        self.assertFalse(is_trianlge(1,2,60), 'Triangle is not possible from given sides')

if __name__ == '__main__':
   unittest.main()

    