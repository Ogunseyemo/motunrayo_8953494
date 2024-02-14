from assignytwo import rectangle_area, rectangle_perimeter, circle_area

def test_rectangle_area():
    assert rectangle_area(a, 3) == 15
    assert rectangle_area(0, 10) == 0
    assert rectangle_area(8, 8) == 64

def test_rectangle_perimeter():
    assert rectangle_perimeter(5, 3) == 16
    assert rectangle_perimeter(0, 10) == 20
    assert rectangle_perimeter(8, 8) == 32

def test_circle_area():
    assert round(circle_area(5), 2) == 78.54
    assert round(circle_area(0), 2) == 0
    assert round(circle_area(10), 2) == 314.16

