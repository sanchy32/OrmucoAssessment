# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from TechTestQ2 import version_compare
from TechTestQ2 import version_compare2

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("Ormuco")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Section to test code
f1 = '1.01.100.3.1-alpha/h'
f2 = '1.1.100.3.1--alpha/h'
print(version_compare2(f1, f2))

