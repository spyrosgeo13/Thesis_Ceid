import poisson_numbers_generation         
import QuickSort2
import numpy as np
# simple menu for the user to chose which distr will he sort
menu_options = {
    1: 'Sort the given Poisson  Distribution of Pseudo-Random Numbers',
    2: 'Sort the given Uniform  Distribution of Pseudo-Random Numbers',
    3: 'Sort the given Binomial  Distribution of Pseudo-Random Numbers',
    4: 'Sort the given Geometric  Distribution of Pseudo_Random Numbers',
    5: 'Exit',
}


def main():
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           s = np.load("poisson.npy")
           QuickSort2.sort_and_count(s)
        elif option == 2:
            s = np.load("Uniform.npy")
            QuickSort2.sort_and_count(s)
        elif option == 3:
            s = np.load("Binomial.npy")
            QuickSort2.sort_and_count(s)
        elif option == 4:
            s = np.load("geometric.npy")
            QuickSort2.sort_and_count(s)
        elif option == 5:
            print('Thank you, you exited successfully')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


main()



