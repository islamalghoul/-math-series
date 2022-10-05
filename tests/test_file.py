import pytest    
from math_series.math_series import Fibonacci_Series,Lucas_Numbers,sum_series

# these tests for Fibonacci_Series
def test_three_Fibonacci_Series():
    actual = Fibonacci_Series(3)
    expected = 2
    assert actual==expected

def test_four_Fibonacci_Series():
    actual = Fibonacci_Series(4)
    expected = 3
    assert actual==expected

def test_five_Fibonacci_Series():
    actual = Fibonacci_Series(5)
    expected = 5
    assert actual==expected



def test_six_Fibonacci_Series():
    actual = Fibonacci_Series(6)
    expected = 8
    assert actual==expected


# these tests for Lucas_Numbers
def test_three_Lucas_Numbers():
    actual=Lucas_Numbers(3)
    expected =4
    assert actual==expected
def test_four_Lucas_Numbers():
    actual=Lucas_Numbers(4)
    expected =7
    assert actual==expected
def test_five_Lucas_Numbers():
    actual=Lucas_Numbers(5)
    expected =11
    assert actual==expected
    



# these tests for sum_series
def test_four_sum_series():
   
    actual=sum_series(4,10,10)
    expected =50
    assert actual==expected
   # 2=20 3=30 4=50
  

def test_five_sum_series():
    actual=sum_series(5,10,10)
    expected =80
    assert actual==expected
     # 2=20 3=30 4=50 5=80   
def test_six_sum_series():
    actual=sum_series(6,15,5)
    expected =115
    assert actual==expected 
    # 2=20 3=25 4=45 5=70 6=115
  