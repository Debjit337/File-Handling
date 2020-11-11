# create file to store list of all creating files

# create new file with adding file name in file
def create_file():
    # get file name by user
    filename = input('\nCreate new filename: ')
    
    # add file name in list_of_files
    myfile = open('C:/Users/Debjit Mukherjee/Documents/python/files/list_of_files.txt', 'a')
    myfile.write(filename+'\n')

    # time to also create a file with provided name
    myfile = open('C:/Users/Debjit Mukherjee/Documents/python/files/'+ filename +'.txt', 'w')

create_file()

# show available files name as option to user
def show_all_files():
    myfile = open('C:/Users/Debjit Mukherjee/Documents/python/files/list_of_files.txt', 'r')

    # get all available data of file in list
    file_names_in_list = myfile.readlines()
    # print('\n', file_names_in_list)
    final_list = []
    print('\n')
    i = 1
    for r in file_names_in_list:
        print(i, r.strip())
        # append data with strip method to remov \n
        final_list.append(r.strip())
        i += 1
    
    option = input('\nEnter your options: ')
    print('\nOption: ', option)
    print('\nFinal list: ', final_list)

show_all_files()

