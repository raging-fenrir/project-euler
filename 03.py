from mpi4py import MPI
import numpy as np

comm =  MPI.COMM_WORLD
rank = comm.Get_rank()

number = 600851475143
if number%2==0:
    possibility = number - 1
else:
    possibility = number

not_found = True
#going = True

while not_found:

    #testing_list = np.linspace(possibility-2,2,(possibility-1)/2)
    #testing_list = map(int,testing_list)
    #print testing_list
    #for i in testing_list:
    i = possibility-2

    while i>1:

        if possibility%i == 0:
            print "%i %% %i = %i"%(possibility,i,possibility%i)
            break

        elif i<4:
            print "found? %i"%possibility
            not_found = False
            break

        else:
            
            i-=2



    if possibility < 4:
        print "Not found :("
        exit(1)
    possibility -= 2    
