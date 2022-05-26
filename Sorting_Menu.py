import poisson_numbers_generation         
import QuickSort2
# simple menu for the user to chose which distr will he sort
menu_options = {
    1: 'Uniform Distribution of Pseudo-Random Numbers',
    2: 'Poisson Distribution of Pseudo-Random Numbers',
    3: 'Binomial Distribution of Pseudo-Random Numbers',
    4: 'geometric Distribution of Pseudo_Random Numbers',
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
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    poisson_numbers_generation.load_poisson_distribution_and_sort_it()
    

def option2():
    print()

   
def option3():
    print()

    

def option4():  
    print()




