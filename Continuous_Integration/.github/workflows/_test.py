import pytest

#function to test square
def square(n):
    return n ** 2

#function to test cube
def cube(n):
    return n**3

def fifht_power(n):
    return n**5

#testing square function
def test_square():
    assert square(2) == 4, "Test failed: Square of 2 should be 4"
    assert square(3) == 27, "Test failer: Square of 3 should be 9"
    
#testing the cube function
def test_cube():
    assert cube(2) == 8, "test failed: Cube of 2 should be 8"
    assert cube(3) == 9, "test failed: Cube of 3 should be 27"
    
#testing the fifth power function
def test_fifth_power():
    assert fifht_power(2) == 32, "test failed: fifth power of 2 should be 32"
    assert fifht_power(3) == 243, "test failed: fifth power of 3 should be 243"
    
#test for invalid input()
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")