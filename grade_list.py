#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: January 2021
# This program gets the average of the numbers in the list


def average_of_list(new_list):
    # This function gets the average of the numbers in the list

    average = 0

    for loop_counter in range(0, len(new_list)):
        average += new_list[loop_counter]
    average = average / len(new_list)
    return average


def main():
    # This function gets any amount of inputed grades from the user and
    # gives them to the average function

    my_list = []
    counter = 2
    average = 0

    print("")
    print("Please enter all the grades of the students."
          " Enter -1 when finished.")
    print("")

    try:
        new_grade = int(input("Grade 1:"))
    except Exception:
        print("This was not a valid grade")
        new_grade = 0  # this is so the != -1 won't end up crashing the program
    else:
        if new_grade <= 100 and new_grade >= -1:
            my_list.append(new_grade)
        else:
            print("This was not a valid grade")

    while new_grade != -1:
        try:
            new_grade = int(input("Grade {0}:".format(counter)))
        except Exception:
            print("This was not an integer")
        else:
            if new_grade <= 100 and new_grade >= -1:
                my_list.append(new_grade)
            else:
                print("This was not a valid grade")
        counter += 1

    if len(my_list) != 1:
        my_list.pop()
        average = average_of_list(my_list)
    print("The average is {0}".format(average))


if __name__ == "__main__":
    main()
