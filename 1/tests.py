from solution import example_function


def test_correct():
    try:
        example_function(1, 2.0, "hello")
        assert True 
    except Exception as e:
        assert False

def test_incorrect():
    try:
        example_function(1, "not a float", "hello")
        assert False 
    except Exception as e:
        assert True