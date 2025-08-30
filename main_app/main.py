

import os
import sys


def main():
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'side_app'))

    sidemodule1 = __import__('sidemodule1')
    sidemodule2 = __import__('sidemodule2')

    # pyarmor: __assert_armored__(sidemodule1)
    # pyarmor: __assert_armored__(sidemodule2)

    sidemodule1.run1()
    sidemodule2.run2()

    


if __name__ == "__main__":
    main()