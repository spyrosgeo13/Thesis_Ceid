import Uniform_numbers_generation
import poisson_numbers_generation 
import Binomial_numbers_generation
import geometric_numbers_distribution

menu_options = {
    1: 'Create Uniform Distribution of Pseudo-Random Numbers',
    2: 'Create Poisson Distribution of Pseudo-Random Numbers',
    3: 'Create Binomial Distribution of Pseudo-Random Numbers',
    4: 'Create geometric Distribution of Pseudo_Random Numbers',
    5: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    
    Uniform_numbers_generation.create_uniform_distribution_numbers_array()

def option2():
    poisson_numbers_generation.create_poisson_distribution_numbers_array()
   
def option3():

    Binomial_numbers_generation.create_binomial_distribution_numbers_array()

def option4():
    
    geometric_numbers_d1istribution.create_geometric_distribution_numbers_array()

    
    
    
if __name__=='__main__':
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
