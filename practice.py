filename = input('\nCreate new filename: ')
myfile = open('C:/Users/Debjit Mukherjee/Documents/python/files/'+ filename +'.txt','a')

print('\nCheck myfile outptut: ', myfile)
myfile.close()

import os

# direct remove file
#os.remove('C:/Users/Debjit Mukherjee/Documents/python/files/New.txt')

delete_file_name = input('\nEnter file name for delete: ')

# remove but before check FileNotFoundError
checkfile = os.path.exists('C:/Users/Debjit Mukherjee/Documents/python/files/'+ delete_file_name + '.txt')

if checkfile == True:
    os.remove('C:/Users/Debjit Mukherjee/Documents/python/files/'+ delete_file_name +'.txt')
else:
    print('\n',delete_file_name + ' file not exists. Try with other file name.')

'''
------------------ END Delete File -------------------
'''    
'''
------------------ CREATE NEW FOLDER -------------------
'''

folder_name = input('\nCreate new folder name: ')
os.mkdir('C:/Users/Debjit Mukherjee/Documents/python/files/' + folder_name)

'''
------------------ END CREATE NEW FOLDER -------------------
'''
'''
------------------ DELETE FOLDER -------------------
'''

folder_name = input('\nDelete folder name: ')
os.rmdir('C:/Users/Debjit Mukherjee/Documents/python/files/' + folder_name)
