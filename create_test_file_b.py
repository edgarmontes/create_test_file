"""
Program Name:   create_test_file_c.py
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


def ran_str(string_length):
    return "".join(random.choice(string.ascii_uppercase) for i in range(string_length)) #[ascii_lowercase]|[ascii_letters]

def ran_num(number_length):
    return "".join(random.choice(string.digits) for i in range(number_length))

def build_file(num_of_records):
    c = 0
    file_layout = {}
    while c < num_of_records:
        file_layout[ran_num(6)] = {
            "DOB":ran_num(2)+"/"+ran_num(2)+"/"+ran_num(4),
            "First Name":ran_str(9),
            "Last Name":ran_str(9),
            "Address":ran_num(5)+" "+ran_str(5)+" "+ran_str(3)+" "+ran_str(5)+" "+ran_str(2)+" "+ran_num(7)
        }
        c += 1
    return file_layout

def test_file(file_name,num_of_records):
    #build_file(num_of_records)#Commented out to take different approach
    with open("{}.txt".format(file_name),"w") as f:
        f.write("DOB,Last Name,First Name,Address\n")
        c = 0
        while c < num_of_records:
            print(c)
            f.write(ran_num(2)+"/"+ran_num(2)+"/"+ran_num(4)+","+ran_str(9)+","+ran_str(9)+","+ran_num(5)+" "+ran_str(5)+" "+ran_str(3)+" "+ran_str(5)+" "+ran_str(2)+" "+ran_num(5)+"\n")
            c += 1


if __name__ == "__main__":
    test_file("tf",20000)



total_time = time.time()-start_time
print("\nTotal execution time {:.2f} minutes!".format(total_time/60))