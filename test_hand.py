import sys
from pretty_python import pretty, pprint

def main(argv):
    # Start tests
    test_pretty()

    test_pprint()

    pass

def test_pretty():
  
    d = dict(Foo=[1,2,3], Bar={'a':1, 'b':2, 'c':3})
    print(f"d: {pretty(d, verbose=True)}")

def test_pprint():
  
    d = dict(Foo=[1,2,3], Bar={'a':1, 'b':2, 'c':3})
    pprint(d, verbose=True)


if __name__ == '__main__':
    main(sys.argv[1:])