# DataAnalysis.py
# Author: Jared Buehner
# Class: SDEV 300
# Professor: Muhammad Khan
# Date: 06/22/2020

# Imports.
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HOUSING = 'Housing.csv'
POP_CHANGE = 'PopChange.csv'

# Main menu.
def main_menu():

    print('Select the file you want to analyze:\n'\
    '1. Population Data\n2. Housing Data\n3. Exit the program')

    main_menu

    try:
        # Holds user input in memory.
        selection = int(input('\nPlease make a selection: '))
        if selection == 1:
            ingest_csv(POP_CHANGE)
        if selection == 2:
            ingest_csv(HOUSING)
        if selection == 3:
            print('\n*** Thanks for trying the line Analysis program ***\n')
            sys.exit()

    except ValueError:
        print('\nSelection invalid. Please try again.\n')
        main_menu()

# Reads .csv file and passes it to the proper method.
def ingest_csv(file):

    line_frame = pd.read_csv(file)
    if file == POP_CHANGE:
        PopChange(line_frame)
    else:
        Housing(line_frame)

# Generates histogram and saves it as a .svg file.
def generate_histogram(line, title):

    mu = line.mean()
    sigma = line.std()
    x = mu + sigma * np.random.randn(10000)
    plt.hist(x, bins='auto')
    plt.grid(True)
    plt.title(title)
    plt.savefig('{}{}'.format(title, '.svg'))
    plt.show()

class PopChange:

    def __init__(self, line_frame):

        self.line_frame = line_frame
        self.housing_menu()

    def housing_menu(self):

        menu_items = {
            1: '1. Pop Apr 1',
            2: '2. Pop Jul 1',
            3: '3. Change Pop',
            4: '4. Return to Menu'
        }

        for item in menu_items.keys():
            print(menu_items[item])

        try:
            selection = int(input('\nSelect a column you wish to analyze: '))
            if selection == 1:
                self.analyze(self.line_frame['Pop Apr 1'])
            elif selection == 2:
                self.analyze(self.line_frame['Pop Jul 1'])
            elif selection == 3:
                self.analyze(self.line_frame['Change Pop'])
            elif selection == 4:
                main_menu()

        except ValueError:
            print('\nSelection invalid. Please try again.\n')
            self.housing_menu()

    # Finds and assigns line found and passed in as paremeters and prompts for a histogram.
    def analyze(self, line):

        print('The statistics for this column are:\n')

        pop_dict = {
            'Count:': line.count(),
            'Mean:': line.mean(),
            'Std Deviation:': line.std(),
            'Min:': line.min(),
            'Max:': line.max()
        }

        for item in pop_dict.keys():
            print(item, '{:10.2F}'.format(pop_dict[item]))

        try:
            if input('\nWould you like to generate a histogram? (Y/N): ').upper() == 'Y':
                generate_histogram(line, 'PopChangeHistogram')
                print('\nYour histogram has been saved.\n')

        except ValueError:
            print('\nSorry, please try again.\n')

        finally:
            print('\n')
            self.housing_menu()

class Housing:

    def __init__(self, line_frame):
        self.line_frame = line_frame
        self.housing_menu()  # Display selection menu

    # Selection menu for user to retrieve specific information from the .csv file.
    def housing_menu(self):

        print('1. Age\n2. Bedrooms\n3. Built\n4. Rooms\n5. Utility'\
        '\n6. Return to Menu')

        try:
            # Holds user input in memory.
            selection = int(input('\nSelect the column you want to analyze: '))
            if selection == 1:
                self.analyze(self.line_frame['AGE'])
            if selection == 2:
                self.analyze(self.line_frame['BEDRMS'])
            if selection == 3:
                self.analyze(self.line_frame['BUILT'])
            if selection == 4:
                self.analyze(self.line_frame['ROOMS'])
            if selection == 5:
                self.analyze(self.line_frame['UTILITY'])
            if selection == 6:
                main_menu()

        except ValueError:
            print('\nSelection invalid. Please try again.\n')
            self.housing_menu()

    # Creates dictionary from analysis and prompts the user to create a histogram.
    def analyze(self, line):

        housing_dict = {
            'Count:': line.count(),
            'Mean:': line.mean(),
            'Std Deviation:': line.std(),
            'Min:': line.min(),
            'Max:': line.max()
        }

        for item in housing_dict.keys():
            print(item, '{:10.2F}'.format(housing_dict[item]))

        try:
            if input('\nWould you like to generate a histogram? (Y/N): ').upper() == 'Y':
                generate_histogram(line, 'HousingHistogram')
                print('\nYour histogram has been saved to this directory.\n')

        except ValueError:
            print('\nError, please try again.\n')

        finally:
            print('\n')
            self.housing_menu()

if __name__ == '__main__':
    print('\n*** Welcome to the line Analysis application ***\n')
    main_menu()