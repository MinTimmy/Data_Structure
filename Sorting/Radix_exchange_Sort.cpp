#include<iostream>
#include<string>
#include <bitset>
#include <cmath>

using namespace std;
#define C_BITS 7  // 000 000 the number of bits for data
#define M 3 // every 3 bits to compare
#define MAX 7+1 // the max of 3 bits
void output(char a[][C_BITS], int amount)
{
    for(int i = 0; i < amount; i++){
        cout << i << ": "<< a[i] << "\n";
    }
}

int bits(char a[C_BITS], int start, int amount)
{
    int temp = 0;
    int count = 0;
    for(int i = C_BITS - start - 2; i > (C_BITS - start - amount - 2); i--)
    {
        temp = temp + pow(2, count) * (int(a[i]) - 48);
        count++; 
    }
    
    return temp;
}

void swap(char a[][C_BITS], int b, int c)
{
    char temp[C_BITS];
    for(int i = 0; i < C_BITS; i++){
        temp[i] = a[b][i];
        a[b][i] = a[c][i];
        a[c][i] = temp[i];
    }
}
void radix_exchange(char a[][C_BITS],int left, int right, int bit)
{
    int i, j ;
    if ( (right > left) && (bit >= 0) ){
        i = left; j = right;
        while  (j != i){
            int k = (bits(a[i], i, 1));
            int kk = (bits(a[j], j, 1));
            //while ((bits(a[i], bit, 1) == 0) && (i < j))i++ ;
            //while ((bits(a[j], bit, 1) == 1) && (i < j))j-- ;
            swap (a, i, j) ;
        }
        if(bits(a[right], bit, 1)) j++;
        radix_exchange ( a, left, j-1, bit-1);
        radix_exchange ( a, j, right, bit-1);
    }

    
}
void straight_radix(char a[][C_BITS], int amount)
{
    int count[MAX];
    char temp[100][100];

    for(int pass = 0; pass < C_BITS / M; pass++) {
        for(int i = 0; i < MAX; i++){
            count[i] = 0;
        }
        for(int i = 0; i < amount; i++){
            count[bits(a[i], pass * M, M)] ++;
        }
         for(int i = 1; i < MAX; i++){
             count[i] = count[i-1] + count[i];
         }

        for(int i = 0; i < amount; i++){
            for(int j = 0; j < C_BITS; j++){
                int t = bits(a[i], pass * M, M);
                temp[count[t] - 1][j] = a[i][j];
            }
            count[bits(a[i], pass * M, M)] --;
        }

         for(int i = 0; i < amount; i++){
            for(int j = 0; j < C_BITS; j++){
                a[i][j] = temp[i][j];
            }  
         }

        output(a, amount);
    }

    
 }


int main()
{
    char data[][C_BITS] = { "001101","110101","101010","111000","000111"};
    int amount = sizeof(data) / sizeof(data[0]); // the amount of data
    radix_exchange(data, 0, 5, 6);

    //output(data, amount);
    //straight_radix(data, amount);

        
}