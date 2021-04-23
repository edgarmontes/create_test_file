"""
Program Name:   create_test_file_c.py
Purpose:        Generate a test file from a given set of variables
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


ran_str = lambda string_length: "".join(random.choice(string.ascii_uppercase).strip() for i in range(string_length)) #[ascii_lowercase]|[ascii_letters]
ran_num = lambda number_length: "".join(random.choice(string.digits).strip() for i in range(number_length))

# Layout for the record
def generate_record():
    record = f"""
            {ran_num(2)}/{ran_num(2)}/{ran_num(4).strip()}
            ,{ran_str(9)}
            ,{ran_str(9)}
            ,{ran_num(5)} {ran_str(9)} {ran_str(3)},{""},{ran_str(5)},{ran_str(2)},{ran_num(5)}
            """
    aux = re.sub("\s","",record)
    return aux


def test_file(file_name,num_of_records):
    with open("{}.txt".format(file_name),"w") as f:
        f.write("DOB,Last Name,First Name,Address 1,Address 2,City,State,Zip Code\n")
        c = 0
        while c < num_of_records:
            print(c)
            f.write(generate_record()+"\n")
            c += 1


if __name__ == "__main__":
    test_file("tf",2000)


total_time = time.time()-start_time
print("\nTotal execution time {:.2f} minutes!".format(total_time/60))