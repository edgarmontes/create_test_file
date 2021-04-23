"""
Program Name:   create_test_file.py
Purpose:        Generate a test file from a given set of columns
Input files:    N/A
Output files:   Test file(.txt)
Author:         Edgar Montes
Date created:   04.22.2021
Version:        V3
"""
import time
start_time = time.time()
import random
import string
import re
from randomtimestamp import randomtimestamp


ran_str = lambda string_length: "".join(random.choice(string.ascii_uppercase).strip() for i in range(string_length)) #[ascii_lowercase]|[ascii_letters]
ran_num = lambda number_length: "".join(random.choice(string.digits).strip() for i in range(number_length))

# Generate random values based on the header
def generate_record():
    record = f"""
            {randomtimestamp(start_year=1920).split()[0]}
            ,{ran_str(9)}
            ,{ran_str(9)}
            ,{ran_num(5)} {ran_str(9)} {ran_str(3)}
            ,{""}
            ,{ran_str(5)}
            ,{ran_str(2)}
            ,{ran_num(5)}
            """
    aux = re.sub("\s","",record)
    return aux


def test_file(file_name,num_of_records):
    with open("{}.txt".format(file_name),"w") as f:
        # Define header for the test file
        f.write("DOB(DD-MM-YYYY),Last Name,First Name,Address 1,Address 2,City,State,Zip Code\n")
        c = 0
        while c < num_of_records:
            print(c)
            f.write(generate_record()+"\n")
            c += 1


if __name__ == "__main__":
    # Enter file name and number of records needed for the test file
    test_file("the_file_name",2000)


total_time = time.time()-start_time
print("\nTotal execution time {:.2f} minutes!".format(total_time/60))