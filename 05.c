#include <iostream>


int main()
{
    int divisors[20];
    int i,j,k;
    
    for (i=0 ; i < 21 ;i++)
      divisors[i] = i;
    
    for (i=100 ; i<100000000000 ; i++)
      {
        if (k>16)
          {
            std::cout << i-1 << " "
              << k << std::endl;
          }
        k = 0;
        for (j=2 ; j<21 ; j++)
          {
            if (i%j==0)
              k += 1;
            else
              k -= 1;
          }
        if (k==19)
          {
            std::cout << i << std::endl;
            break;
          }
      }
    return 0;
}
