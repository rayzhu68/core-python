
    
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):
    assert item not in collection, "Did not expect but {1} is in {0}".format(collection, item)

def test_between_inclusive(a, b, c):
    assert (a<=b) and (b<=c), "{1} is not between {0} and {2}".format(a, b, c)
    
test_not_in([12, 3, 4, 6], 4)
    
print("Just passed all tests!")