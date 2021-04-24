"""
Program Name:   create_test_file.py
Purpose:        Generate a test file from a given set of columns
Input files:    N/A
Output files:   Test file(.txt)
Author:         Edgar Montes
Date created:   04.22.2021
Version:        V1
"""
import time
start_time = time.time()
import random
import string
import re
from randomtimestamp import randomtimestamp


ran_str = lambda string_length: "".join(random.choice(string.ascii_uppercase).strip() for i in range(string_length)) #[ascii_lowercase]|[ascii_letters]
ran_num = lambda number_length: "".join(random.choice(string.digits).strip() for i in range(number_length))

# Define file name, number of records and delimiter
of = "the_file_name.txt"
nor = 10000
dlm = "|"

# Build test file
def generate_test_file(output_file,num_of_records):
    with open(output_file,"w") as f: 
        c = 0
        while c < num_of_records:
            print(c)
            # Define file layout
            file_layout = {
                "DOB(DD-MM-YYYY)":randomtimestamp(start_year=1920).split()[0],
                "First Name":ran_str(9),
                "Last Name":ran_str(9),
                "Address 1":" ".join([ran_num(5),ran_str(9),ran_str(3)]),
                "Address 2":"",
                "City":ran_str(5),
                "State":ran_str(2),
                "Zip Code":ran_num(5),
            }
            if c == 0:
                f.write(dlm.join([k for k in file_layout.keys()])+"\n")
            else:
                f.write(dlm.join([v for v in file_layout.values()])+"\n")
            c += 1


if __name__ == "__main__":
    generate_test_file(of,nor)



total_time = time.time()-start_time
print("\nTotal execution time {:.2f} minutes!".format(total_time/60))