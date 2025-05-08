import sys
from missing_number import NumberSet

if __name__ == '__main__':
    try:
        num = int(sys.argv[1])
        ns = NumberSet()
        ns.extract(num)
        print(f'Número extraído: {ns.find_missing()}')
    except Exception as e:
        print(f'Error: {e}')
