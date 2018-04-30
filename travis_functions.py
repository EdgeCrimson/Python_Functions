#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Name:     Useful Functions
# Purpose:  To serve as a reference for useful functions that I have computed before that I might desire to use later. 
#           
# Author:   Travis Asher
#
# Created:  1/21/2018
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_time(in_hour,in_min,in_sec,time_s):
    '''Increments inputed hour, minute, and second time (in military format) by desired seconds. All of the preceding functions work to 
        calculate the exact time of day an event ends on based on its start time and the event's duration in seconds. Its inputs are, 
        respectively, the starting hour (from 0 to 23), the starting minute, that starting second, and the amount of seconds that the 
        event lasts. Its outputs are, respectively, the ending hour (from 1 to 12), the ending minute, the ending second, and whether 
        or not it is AM or PM.'''
    time = sec_to_hrminsec(time_s)
    if in_sec + time[2] < 60:
        tot_sec = in_sec + time[2]
        tot_hrmin = inc_min(in_min+time[1],in_hour,time[0])
        tot_min = tot_hrmin[1]
        tot_hour = tot_hrmin[0]
    else:
        tot_sec = (in_sec + time[2]) % 60
        tot_hrmin = inc_min(in_min+time[1]+1,in_hour,time[0])
        tot_min = tot_hrmin[1]
        tot_hour = tot_hrmin[0]
    milt_time = (tot_hour,tot_min,tot_sec)
    if milt_time[0]==0:
        adj_hour=12
        period = "AM"
    elif 0<milt_time[0]<12:
        adj_hour=milt_time[0]
        period = "AM"
    elif milt_time[0]==12:
        adj_hour=12
        period= "PM"
    elif milt_time[0]>12:
        adj_hour=milt_time[0]-12
        period = "PM"
    fin_time = (adj_hour,tot_min,tot_sec,period)       
    return fin_time         
    
    
    
def sec_to_hrminsec(time_s):
    '''Used in add_time function.'''
    if time_s<60:
        add_sec = time_s
        add_min = 0
        add_hour = 0
    else:
        add_sec = time_s % 60
        time_m = int(time_s/60)
        if time_m<60:
            add_min = time_m
            add_hour = 0
        else:
            add_min = time_m % 60
            add_hour = int(time_m/60)
    return (add_hour,add_min,add_sec)
         
    
    
def inc_min(mint,in_hour,time_h):
    '''Used in add_time function.'''
    if mint < 60:
        tot_min = mint
        tot_hour = inc_hour(in_hour + time_h)
    else:
        tot_min = mint % 60
        tot_hour = inc_hour(in_hour + time_h + 1)
    return (tot_hour,tot_min)
    
        
        
def inc_hour(hour):
    '''Used in add_time function.'''
    if hour < 25:
        tot_hour = hour
    else:
        if hour % 24 == 0:
            tot_hour = 24
        else:
            tot_hour = hour % 24
    return tot_hour
    

    
def gen_prime(n):
    '''This function generates the first n number of prime numbers.'''
    start1 = 2
    start2 = 3
    collection = [start1,start2]
    test_int = collection[len(collection)-1] + 1
    while len(collection)<n:
        prime_check=0
        for i in range(0,len(collection)-1):
            if test_int % collection[i] == 0:
                prime_check+=1
            else:
                pass
        if prime_check == 0:
            collection = collection + [test_int]
            test_int = collection[len(collection)-1] + 1
        else:
            test_int += 1
    return collection
    
    
    
def gen_twinprimes(n):
    '''This function generates the first n number of twin prime numbers. It makes use of the gen_prime() function in its procedure.'''
    twin_primes = []
    #Our first test run is done on the first n primes using gen_prime(). Since we know that (2,3) is not a twin prime, we are certain 
    # that our first run will not be sufficient to calculate the first n twin primes. 
    test_twins = gen_prime(n)
    for i in range(1,n-2):
        if test_twins[i+1] - test_twins[i] == 2:
            twin_primes = twin_primes + [0]
            spot = len(twin_primes)-1
            twin_primes[spot] = [test_twins[i],test_twins[i+1]]
        else:
            pass
    test_next = n+1
    while len(twin_primes)<10:
        check = gen_prime(test_next)[test_next-2:]        
        if check[1]-check[0] == 2:
            twin_primes = twin_primes + [0]
            spot = len(twin_primes)-1
            twin_primes[spot] = [check[0],check[1]]
        else:
            pass
        test_next += 1
        #The below if statement is for debugging purposes only to prevent overflow. This line well be suppressed unless needed.
        #if test_next > 1000:
        #twin_primes = ["o","v","e","r","f","l","o","w","e","r"]
    return twin_primes
    
    
    
def even_or_odd(x):
    '''This function determines whether input is odd, even, or not a real number. If input is a real number but not an integer, function
        will indicate this.'''
    if type(x) != int and type(x) != float:
        return False
        print("Your input needs to be a real number. C'mon man, be reasonable.")
    else:
        if type(x) == float:
            return False
            print("Your input needs to be an integer to be even or odd.")
        else:
            if x % 2 == 0:
                e_or_o = "e"
                return e_or_o
                print("Integer {} is even.".format(x))
            else:
                e_or_o = "o"
                return e_or_o
                print("Integer {} is odd.".format(x))


def add_even_odd(n):
    '''This function adds all the even entries and all of the odd entries separately and reports both respective sums. Uses the even_or_odd()
        function.'''
    even_sum = 0
    odd_sum = 0
    for i in n:
        if even_or_odd(i) != False:
            if even_or_odd(i) == "e":
                even_sum = even_sum + i
            else:
                odd_sum = odd_sum + i
        else:
            pass
    print("The sum of even values in {} is {}. The sum of odd values in {} is {}.".format(n,even_sum,n,odd_sum))
    
    
    
def print_list_separately(list_input,intro=False,outro=False):
    '''This function takes a list and prints each of its values on a separate line with a space in between. A prefacing text to be 
        printed before the list value may be included if desired; similarly for an outro text.'''
    if intro==False:
        pass
    else:
        print(intro)
        print("\n")
    limit = len(list_input)
    for i in range(0,limit):
        if i == limit-1:
            print(list_input[i],".",sep="")
        else:
            print(list_input[i])
            print("\n")
    if outro==False:
        pass
    else:
        print("\n")
        print(outro)
        
        
        
def print_list_fields_var_rows(data,fields,num_rows,intro=False,outro=False):
    '''This function takes a list of tuples, a list of fields, an integer number of rows, (optionally) an introductory text, and 
        (optionally) an outro text and prints the intro followed by dictionaries for each rows field into each field name followed by an
        outro.'''
    if len(data[0]) != len(fields):
        return("The number of columns in your input data must match the length of your fields input.")
    else:
        pass
    if intro==False:
        pass
    else:
        print(intro)
        print("\n")
    assign = {}
    for row in range(0,num_rows):
        for col in range(0,len(fields)):
            assign[fields[col]] = data[row][col]
        print(assign)
        print("\n")
    if outro==False:
        pass
    else:
        print(outro)

        
def list_to_dict(lst):
    '''This function takes each entry 'k' of a passed list object and maps it to key 'entry_j' such that the
        statement 'lst[j] == k' is True.'''
    if type(lst) != list:
        if type(lst) == tuple:
            pass
        else:
            return "Function 'list_to_dict' only takes input of the tuple or list types."
    key = {}
    dum_list = []
    lst_deg = len(lst)
    for i in range(0,lst_deg):
        dum_list.append("entry_{}".format(i))
    for i in range(0,lst_deg):
        key[dum_list[i]] = lst[i]
    return key
