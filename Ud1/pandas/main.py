# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd

data = {'Nombre': ['Ana', 'Luis', 'Juan'],
        'Edad': [23, 21, 22],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}

df = pd.DataFrame(data)

print(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
