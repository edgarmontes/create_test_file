"""
Program Name:   create_test_file.py
Purpose:        Generate a test file from a given set of variables
Input files:    N/A
Output files:   Test file(.txt)
Author:         Edgar Montes
Date created:   03.28.2021
Version:        V3
"""
import time
start_time = time.time()
import random
import string


def random_string(string_length):
    letters = string.ascii_uppercase#[ascii_lowercase]|[ascii_letters]
    generated_string = "".join(random.choice(letters) for i in range(string_length))
    return generated_string

def random_number(number_length):
    numbers = string.digits
    generated_number = "".join(random.choice(numbers) for i in range(number_length))
    return generated_number

def build_file(num_of_records):
    c = 0
    file_layout = {}
    while c < num_of_records:
        file_layout[random_number(6)] = {
            "Client Name":random_string(9),
            "S":random_string(9),
            "Pharmacy":random_string(9),
            "Units":int(random_number(6))
        }
        c += 1
    return file_layout

def test_file(file_name,num_of_records):
    #build_file(num_of_records)#Commented out to take different approach
    with open("{}.txt".format(file_name),"w") as f:
        f.write("ID,Client Name,S,Pharmacy,Units\n")
        c = 0
        while c < num_of_records:
            print(c)
            f.write(random_number(6)+","+random_string(9)+","+random_string(9)+","+random_string(9)+","+random_number(6)+"\n")
            c += 1


if __name__ == "__main__":
    test_file("tf",20000)



total_time = time.time()-start_time
print("\nTotal execution time {:.2f} minutes!".format(total_time/60))