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

def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')
    for word in list_of_lines:
        f.write(word + "\n")
    f.close()    

def copy_file_add_line_numbers(file_name_read, file_name_write):
    list_words = read_file_list(file_name_read)
    
    counter = 1

    f = open(file_name_write, 'w')
    for word in list_words:
        f.write(str(counter) + ":" + word + "\n")
        counter += 1

    f.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
