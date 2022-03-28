import Calculate

import pytest
@pytest.mark.area
def test_area_square():
    side = 4
    res = Calculate.area_square(side)
    assert res == side * side

@pytest.mark.area
def test_area_rectangle():
    l = 2
    b = 3
    res = Calculate.area_rectangle(l,b)
    assert res == l * b

@pytest.mark.perimeter
def test_perimeter_rectangle():
    a = 3
    b = 2
    res = Calculate.perimeter_rectangle(a,b)
    assert res == 2 * (a+b)
