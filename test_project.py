from mylib.calc import add,sub,div,power,mul

def test_add():
    assert add(1,2) ==3
def test_sub():
    assert sub(1,2) ==-1
def test_mul():
    assert mul(1,2) ==2
def test_power():
    assert power(1,2) ==1
def test_div():
    assert div(1,2) ==0.5       