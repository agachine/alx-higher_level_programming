#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    a = 10
    b = 5
    print('{:d} + {:d} = {:d}'.format(a, b, add(a=a, b=b)))
    print('{:d} - {:d} = {:d}'.format(a, b, sub(a=a, b=b)))
    print('{:d} * {:d} = {:d}'.format(a, b, mul(a=a, b=b)))
    print('{:d} / {:d} = {:d}'.format(a, b, div(a=a, b=b)))
