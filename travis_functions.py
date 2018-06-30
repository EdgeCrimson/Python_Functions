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




def PoE_attribute_tracker(state = True):
    '''This function allows the user to adjust attribute values for their character from an initial blank state. Things it will do:
    adjust integer increments or decrements to the included attributes, decline (most) unacceptable input attempts, continue to
    iterate until the user indicates that they are finished. Things it will not do: accept float value adjustments to attributes,
    handle user input with multiple colons.'''
    attributes = ['int','str','mel_spd','mel_dam','acc','acc_pc','mana_cost_pc','atk_spd','dex','arm_pc',
                  'enrg_shield_pc','life_gen_pc','cst_spd','mov_spd','spl_dam_pc','mel_dam_pc','life_pc',
                  'evd_pc','arm_pc','stun_thrsh','Jewel_Socket','life','evd','mana_pc','mana','mana_gen_pc',
                  'bow_dam_pc','psn_pc','bow_ailm_dam_pc','proj_spd','proj_dam_pc','bow_atk_spd','crit_pc',
                  'lhtn_res_pc','cold_res_pc','fire_res_pc']
    attributes.sort()
    dum_list = [0]*len(attributes)
    att_list = {}
    for x in attributes:
        att_list['{}'.format(x)] = dum_list[attributes.index(x)]
    while state == True:
        get_resp = True
        while get_resp == True:
            print("\nAttributes are: {}".format(attributes))
            response = input("Which attribute do you wish to adjust and by what amount? Make selection in the \
                                 form '{attribute}={value}'.\n")
            if type(response) != str:
                print("Input must be a string.\n")
            elif response.rfind('=') == -1:
                print("Your input does not match the required form.\n")
            else:
                int_pass = True
                try:
                    int(response[response.rfind('=')+1:])
                except ValueError:
                    int_pass = False
                if int_pass == True:
                    get_resp = False
                else:
                    print("The value after the colon in your input must be a string of a number.\n")
        att = response[:response.rfind('=')]
        val = int(response[response.rfind('=')+1:])
        att_list[att] += val
        print("\n{}".format(att_list))
        request_cont = True
        while request_cont == True:
            cont = input("Would you like to keep going? Select either 'yes' or 'no'.\n")
            if cont not in ["yes","no","y","n"]:
                print("Your input must be either 'yes' or 'no'.\n")
            else:
                request_cont = False
        if cont in ["no","n"]:
            state = False
        
        
        

def MarkovState_Calculator(trans,start,chain_num,dec_place=5):
    '''This function performs a Markov chain process on an initial state vector 'start' with transition matrix
    'trans' for a total number of 'chain_num' Markov chains. It takes as input four variables: 'trans' as a 
    numpy matrix, 'start' as a tuple, 'chain_num' as a nonzero positive integer, and an optional 'dec_place'
    as a nonzero positive integer that defaults to a value of 5. Once called, the function will prompt the
    user to indicate one of three possible output options to be provided as input: 'Final' to output only the
    final vector which results from 'chain_num' Markov chains, 'All' to output a list of each of the state
    vectors that result from each Markov chain (in order), or 'Other' to output a certain number of the last
    state vectors that result from their Markov chain applications. If 'Other' is selected, the user is once
    again prompted for input, this time to specify an 'input' number of state vectors from the tail of the
    Markov chain procedure to be included as a list in the output. This 'input' number of tail values must be
    both nonzero positive as well as less than 'chain_num' number of total Markov chains to be performed. For
    the sake of computation, if the desired number of Markov chains is greater than one million, the function
    will terminate unless the user specifies to override this precaution via input.'''
        
    #Our function begins by determining if the passed input values are acceptable values to use to perform the
    # intended calculations for output. We begin with checks on 'trans':
    if type(trans) != np.matrix:
        return("The input 'trans' must be of the type 'np.matrix' from the numpy module.")
    elif len(trans) != len(trans.transpose()):
        return("The rank of matrix 'trans' must be equal to the rank of its tranpose 'trans.transpose()'.")
    R = len(trans)
    
    #Next, we perform checks on 'start':
    if type(start) not in [tuple,list]:
        return("The input 'start' must be either of type 'tuple' or 'list'.")
    elif type(start) in [tuple,list]:
        if len(start) != R:
            return("The length of input 'start' must match the dimension of matrix 'trans'.")
        type_start = [type(item) for item in start]
        if not set(type_start).issubset(set([int,float])):
            return("Each entry of 'start' must be either of the 'float' or 'int' type.")
            
    #Our next check is on 'chain_num':
    if type(chain_num) != int:
        return("The input 'chain_num' must be a positive nonzero integer.")
    elif chain_num < 1:
        return("The input 'chain_num' cannot be 0 or a negative integer.")
    elif chain_num > 1000000:
        override_check = input("The specified number of 'chain_num' Markov chains will be computationally"
                               " expensive and may crash the program. Do you still wish to proceed? Respond"
                               " with either 'Yes' to proceed or anything else to ovveride:\n")
        if override_check not in ['Yes','yes']:
            return
    
    #If all other inputs are acceptable, our last check is performed on 'dec_place':
    if type(dec_place) != int:
        return("The input 'dec_place' must be a positive integer.")
    elif dec_place < 0:
        return("The input 'dec_place' cannot be a negative integer without losing all meaning.")
        
    #If all of the above checks are passed, the function will proceed to Markov chain procedure, beginning by
    # prompting the user for input.
    init_proceed = False
    while init_proceed == False:
        output_type = input("Would you like to receive the resultant vector of {} chains of your Markov"
                            " process, would you like to receive a list containing the resultant vector of"
                            " every step of this Markov process, or would you like to receive a certain"
                            " number of the last iterations of this Markov process? Respond 'Final' for the"
                            " first option, 'All' for' the second option, or 'Other' for the third option:\n"
                            .format(chain_num))
        if output_type in ['Final','final']:
            init_proceed = True
            nxt = start * trans
            for n in range(1,chain_num):
                nxt = nxt * trans
            #The following rounds each entry in nxt and appends it to the empty matrix 'rounded'
            rounded = []
            for n in range(len(trans)):
                rounded_n = round(nxt.item(n),dec_place)
                rounded.append(rounded_n)
            return(rounded)
        if output_type in ['All','all']:
            init_proceed = True
            nxt = start * trans
            first = []
            for m in range(len(trans)):
                rounded_m = round(nxt.item(m),dec_place)
                first.append(rounded_m)
            rounded_all = [first]
            for n in range(1,chain_num):
                nxt = nxt * trans
                rounded = []
                for m in range(len(trans)):
                    rounded_m = round(nxt.item(m),dec_place)
                    rounded.append(rounded_m)
                rounded_all.append(rounded)
            return(rounded_all)
        if output_type in ['Other','other']:
            init_proceed = True
            proceed = False
            while proceed == False:
                tail_num = input("The output of this function will be a list of the last specified number N"
                                 " applications of the Markov process. What number of last entries would you"
                                 " like to receive? Respond with a nonzero positive integer less than the"
                                 " number of Markov chains:\n")
                int_check = True
                try:
                    int(tail_num)
                except ValueError:
                    int_check = False
                if int_check == True:
                    if all((int(tail_num)>0,int(tail_num)<chain_num)):
                        proceed = True
                        nxt = start * trans
                        rounded_all = []
                        for n in range(1,chain_num-int(tail_num)):
                            nxt = nxt * trans
                        for n in range(chain_num-int(tail_num),chain_num):
                            rounded = []
                            nxt = nxt * trans
                            for m in range(len(trans)):
                                rounded_m = round(nxt.item(m),dec_place)
                                rounded.append(rounded_m)
                            rounded_all.append(rounded)
                        return(rounded_all)
                    elif int(tail_num) < 0:
                        print("'{}' is an invalid integer. Please enter a positive nonzero integer:\n"
                              .format(int(tail_num)))
                    else:
                        print("'{}' is an invalid integer. Please enter an integer less than the number of"
                              " Markov chains in the process:\n".format(int(tail_num)))
                else:
                    print("Your response is not an integer.\n")
        else:
            print("Your input must be either 'Final', 'All', or 'Other'.")
            
