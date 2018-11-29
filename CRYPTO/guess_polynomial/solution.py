from netcat import Netcat
guess_number = long("100000000000000000000000000000000000000000000000000")

def get_last_number(remaining_sum):
    last_number = ""
    y = 0
    for i in xrange(len(remaining_sum)-1, -1 , -1):
        y = i
	# try to figure out the end out an number        
	if remaining_sum[i-5:i] == "00000":
            break
        last_number = remaining_sum[i] + last_number
    if(len(remaining_sum) > 37):
        last_number = remaining_sum[y] + last_number

    return long(last_number)
loop = 0
while (loop < 10):
    print "LOOP: " + str(loop)
    if(loop == 0):
	# connect to the server thrugh netcat lib
        nc = Netcat('39.96.8.114', 9999)
        nc.read_until('Please input your number to guess the coeff:')

    nc.write(str(guess_number) + '\n')
    data = nc.read_until("It is your time to guess the coeff!")
    data = data.replace("This is the sum: ", "")
    data = data.replace("It is your time to guess the coeff!", "")

    sum = data
    cof = ""
    for i in range( 0, 120):
        if long(sum) == 0 or long(sum) == -1: 
            continue
        last_number = get_last_number(sum)
        cof = str(last_number) + str(" ") + cof
	# eliminate last number by subtract it from the sum then divide by guess number  
	sum = str(long(long(sum) - long(last_number))/long(guess_number))
    print cof
    nc.write( cof + "\n")      
    print nc.read(100)
    loop = loop + 1
