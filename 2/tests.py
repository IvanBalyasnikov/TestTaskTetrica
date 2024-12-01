import os
from solution import main


def test_main():
    assert main() == None
    assert os.path.isfile("beasts.csv")