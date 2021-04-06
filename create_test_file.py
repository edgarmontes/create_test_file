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


def test_file(file_name,num_of_records):
    with open("{}.txt".format(file_name),"w") as f:
        header = "ID,Client Name,S,Pharmacy,Units\n"
        f.write(header)
        c = 0
        d = "," # Define file delimiter
        while c < num_of_records:
            print(c)
            f.write(random_number(6)+d+random_string(9)+d+random_string(9)+d+random_string(9)+d+random_number(6)+"\n")
            c += 1


if __name__ == "__main__":
    test_file("tf",20000)



total_time = time.time()-start_time
print("\nTotal execution time {:.2f} minutes!".format(total_time/60))
