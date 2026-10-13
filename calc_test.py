from hello import add, subtract, multiply, divide

def test_add():
    assert add(15, 30) == 45

def test_subtract():
    assert subtract(15, 30) == -15

def test_multiply():
    assert multiply(15, 30) == 450

def test_divide():
    assert divide(15, 30) == 0.5
