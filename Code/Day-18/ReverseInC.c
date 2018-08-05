#include <stdio.h>
#include <stdlib.h>
 
#define CHAR_BITS  8  
 
#define INT_BITS  ( sizeof(int) * CHAR_BITS)
//function print in binary format
void PrintInBinary(unsigned n)
{
 short int iPos;
 
 for (iPos = (INT_BITS -1) ; iPos >= 0 ; iPos--)
 {
   (n & (1 << iPos))? printf("1"): printf("0"); 
 }
}
 
//bit reversal function
unsigned int ReverseTheBits(unsigned int num)
{
    unsigned int count = (INT_BITS -1); 
    unsigned int tmp = num;          
    num >>= 1;
    while(num)
    {
       tmp <<= 1;    
       tmp |= num & 1; 
       num >>= 1; 
       count--;
    }
    tmp <<= count; 
    return tmp;
}
int main()
{
    unsigned int data = 0;
    unsigned int Ret = 0;
    printf("Enter the number : ");
    scanf("%u",&data);
    printf("\n\nEntered Data is " );
    PrintInBinary(data);
    Ret = ReverseTheBits(data);
    printf("\n\nReverse Data is " );
    PrintInBinary(Ret);
return 0;
}
