#include <cmath>
#include <iostream>
#include <mpi>

int main(int argcounter, char **arg_values)
{
  int number, possibility, i,j;
  int rank, size, counter_start, counter_stop;

  number = 100;
  MPI_Init (&argcounter, &arg_values);
  MPI_Comm_rank (MPI_COMM_WORLD, &rank);
  MPI_Comm_size (MPI_COMM_WORLD, &size);
  
  printf("Finding largest prime factor of %d\n",
         number);
  if (number%2 == 0)
    possibility = number-1;
  else
    possibility = number-2;
  
  for (j=possibility ; j>2 ; j-=2)
    {
      //      if(rank==1)
      //printf("%d\n",j);
      if (number%j == 0)
        {
        
          counter_start = rank*(j-2)/size;
          counter_stop = (rank+1)*(j-2)/size;
          printf("%d: start = %d, stop = %d\n",rank,counter_start,counter_stop);
          //printf("j=%d\n",j);
          for (i=counter_stop ; i>counter_start ; i-=2)
            {
              printf("j=%d, i=%d\n",j,i);
              if (j%i == 0)
                {
                  printf("%d %% %d = %d\n",j,i,j%i);
                  break;
                }
              else if(i<4)
                {
                  printf("%d: found? %d\n",rank,j);
                  j=1;
                  break;
                }
            }
        }
    }
  MPI_Finalize();
  return 0;
}
