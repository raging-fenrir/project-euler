#!/usr/bin/env python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

t_start = MPI.Wtime()

primes = []
#number = int(2e6)
number = 50

if rank==0:
    primes.append(2)
    

start = rank*number/size+1
stop = (rank+1)*number/size

if rank==0:
    start +=2

if start%2==0:
    start +=1
if stop%2==0:
    stop -=1
    
print("%i: start = %i, stop = %i"%(rank,start,stop))

for i in xrange(start, stop+1,2):
    found=True
    for j in xrange(3,i,2):
        if i%j==0:
            found=False
            break
        
    if found:
        primes.append(i)
totals = np.sum(primes)

#print(rank," primes: ",primes,"sum: ", totals)
print("%i: sum = %i"%(rank, totals))
total_sum = comm.reduce(totals,op=MPI.SUM,root=0)

if rank==0:
    print("Total sum = %i"%total_sum)
    t_diff = MPI.Wtime() - t_start
    print("time used %f"%t_diff)
