#!/usr/bin/env python3
# Author ID: cshin9

def read_file_string(file_name):
    f = open(file_name, 'r')
    read_data = f.read()
    f.close()
    
    return read_data

def read_file_list(file_name):
    new_list = []

    f = open(file_name, 'r')
    list_read_data = list(f)
    f.close()

    for word in list_read_data:
        new_list.append(word.strip())
    
    return new_list

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
