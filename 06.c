#include <stdio.h>


int main()
{
  int sum_of_squares, square_of_sum,i;
  sum_of_squares = square_of_sum = 0;

  for (i=1 ; i<101 ; i++)
    {
      sum_of_squares += i*i;
      square_of_sum += i;
    }
  square_of_sum = square_of_sum*square_of_sum;

  printf("Square of sum - sums of square:\n");
  printf("%i - %i = %i\n",square_of_sum,sum_of_squares,
         square_of_sum-sum_of_squares);
  return 0;
}
