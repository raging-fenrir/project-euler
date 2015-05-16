from mpi4py import MPI
import numpy as np

comm =  MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = None
i = None
#number = 336423426
number = 600851475143

if rank ==0:
    prime_file=open('primes.txt','a')
    prime_file.write("Primefactors for %i\n"%number)
    prime_file.close()

def check_primage(i):
    prime = True
    counter_start = rank*i/size
    counter_stop = (rank+1)*i/size-1
    if counter_start == 0:
        counter_start = 1

    print "%i: start = %i and stop = %i"%(rank,counter_start,counter_stop)

    for j in xrange(counter_start, counter_stop+1, 2):

        if i%j == 0:
            if j < 2:
                continue
            else:
                print "%i %% %i = %i"%(i,j,j%i)
                prime = False
                break
        
    data = comm.gather(prime,root=0)
    
    if rank==0:
        print "Number of trues: %i/%i"%(np.sum(data),size)
        if np.sum(data)==size:
            prime_file = open('primes.txt','a')
            prime_file.write(str(i)+'\n')
            prime_file.close()

i = 300425753573
i = comm.bcast(i,root=0)

counter = 1

while i > 2:
    if rank == 0:
        if len(str(i)) > 6:
            if counter%(10**(len(str(i))-5)) == 0:
                myfile = open('current.txt','w')
                write_string = str(i)+'\n'
                myfile.write(write_string)
                myfile.close()

        if (number%i == 0):
            print "%i: Found divisible number %i"%(rank,i)
            i = comm.bcast(i,root=0)
            check_primage(i)
        
        i -=2
        if i < 2:
            i = comm.bcast(i,root=0)
        counter += 1
       
    if rank > 0:
        i = comm.bcast(i,root=0)        
        if i > 2:
            print "%i: checking i = %i" %(rank,i)
            check_primage(i)
        else:
            continue

if rank == 0:
    if number%2==0:
        prime_file = open('primes.txt','a')
        prime_file.write("2\n")
        prime_file.close()
