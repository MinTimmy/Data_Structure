#include<iostream>
#include <algorithm>
#include <random>
#include <time.h>
#include <cmath>
using namespace std;

#define SIZE 10
#define MAX 100
#define JUMP 1
void print(int num[])
{
    for(int i = 0; i < SIZE; i++){
        cout << num[i] << ' ';
    }
}

void counting_sort(int num[], int place)
{
    int jump = pow(10, JUMP);
    int count[jump] = {0};
    int output[SIZE] = {0};
  
    for(int i = 0; i <  SIZE; i++){
        int index = num[i] / place;
        count[index % jump]++;
    }
  
    for(int i = 0; i < jump - 1; i++){
        count[i+1] += count[i];
    }

    int i = SIZE - 1;
    while (i >= 0)
    {
        int index = num[i] / place;
        output[count[index % jump]-1] = num[i];
        count[index % jump]--;
        i--;
    }
    

    for(int i = 0; i < SIZE; i++){
        num[i] = output[i];
    }
    
}
void radix_sort(int num[])
{
    int place = 1;
    while ( 99 / place > 0 )
    {
        counting_sort(num, place);
        int t = pow(10, JUMP);
        place *= t;
    }
}

int main()
{
    srand(time(NULL));
    int num[SIZE] = {0};
    for(int i = 0; i < SIZE; i++){
        num[i] = rand() % 100 + 1;
    }
    //print(num);

    radix_sort(num);

    print(num);
}