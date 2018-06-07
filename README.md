# Python Functions
This repository contains my personal Python functions. I will update this document as the included functions are changed.

## Current Functions:
add_time(): Increments inputed hour, minute, and second time (in military format) by desired seconds. All of the preceding functions work to calculate the exact time of day an event ends on based on its start time and the event's duration in seconds. Its inputs are, respectively, the starting hour (from 0 to 23), the starting minute, that starting second, and the amount of seconds that the event lasts. Its outputs are, respectively, the ending hour (from 1 to 12), the ending minute, the ending second, and whether or not it is AM or PM.

sec_to_hrminsec(): Converts time in seconds to time in hours, minutes, and seconds. Used in add_time function.

inc_min(): Used in add_time function.

inc_hour(): Used in add_time function.

gen_prime(): This function generates the first n number of prime numbers.

gen_twinprimes(): This function generates the first n number of twin prime numbers. It makes use of the gen_prime() function in its procedure.

even_or_odd(): This function determines whether input is odd, even, or not a real number. If input is a real number but not an integer, function will indicate this.

add_even_odd(): This function adds all the even entries and all of the odd entries separately and reports both respective sums. Uses the even_or_odd() function.

print_list_separately(): This function takes a list and prints each of its values on a separate line with a space in between. A prefacing text to be printed before the list value may be included if desired; similarly for an outro text.

print_list_fields_var_rows(): This function takes a list of tuples, a list of fields, an integer number of rows, (optionally) an introductory text, and (optionally) an outro text and prints the intro followed by dictionaries for each rows field into each field name followed by an outro.

list_to_dict(): This function takes each entry 'k' of a passed list object and maps it to key 'entry_j' such that the statement 'lst[j] == k' is True.

PoE_attribute_tracker(): This function allows the user to adjust attribute values for their character from an initial blank state. Things it will do: adjust integer increments or decrements to the included attributes, decline (most) unacceptable input attempts, continue to iterate until the user indicates that they are finished. Things it will not do: accept float value adjustments to handle user input with multiple colons.
