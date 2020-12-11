#include<iostream>
#include<random>
#include<time.h>

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

void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
//again
void bubble_sort(int num[])
{
    bool s = true;

    while (s)
    {
        s = false;
        for(int i = 0; i < SIZE - 1; i++){
            if(num[i] > num[i+1]){
                swap(num[i], num[i+1]);
                s = true;
            }
        }
    }
    
}

void counting_sort(int num[])
{
    int count[MAX] = {0};
    int output[SIZE] = {0};

    for(int i = 0; i < SIZE; i++){
        count[num[i]]++;
    }
    for(int i = 0; i < MAX - 1; i++){
        count[i+1]+=count[i];
    }
    for(int i = 0; i < SIZE; i++){
        output[count[num[i]]-1] = num[i];
        count[num[i]]--;
    }
    for(int i = 0; i < SIZE; i++){
        num[i] = output[i];
    }
}

// again
void insertion_sort(int num[])
{
   for(int i = 1; i < SIZE; i++){
       int temp = num[i];
        int  j = i -1;
        while (j >= 0 && num[j] < temp)
        {
            num[j+1] = num[j];
            j--;
        }
        num[j+1] = temp;      
   }
}

int partition(int num[], int low, int high)
{
    int pivot = num[high];
    int i = low - 1;
    for(int j = low; j < SIZE - 1; j++){
        if(num[j] > pivot){
            i++;
            swap(num[i], num[j]);
        }
    }
    swap(num[i+1], num[high]);
    return i+1;
}
//again
void quick_sort(int num[], int low, int high)
{
   if(low < high){
       int pi = partition(num, low, high);
       quick_sort(num,low,pi - 1);
       quick_sort(num, pi+1, high);
   }
}

void selection_sort(int num[])
{
    for(int i = 0; i < SIZE; i++){
        for(int j = i + 1; j < SIZE; j++){
            if(num[i] > num[j]){
                swap(num[i], num[j]);
            }
        }
    }
}
//again
void shell_sort(int num[])
{
    int interval = SIZE / 2;

    while (interval > 0)
    {
        for(int i = interval; i < SIZE; i++){
            int temp = num[i];
            int j = i;
            while (j - interval >= 0 && num[j-interval] < temp)
            {
                num[j] = num[j-interval];
                j -= interval;
            }
            num[j] = temp;
        }
        interval /= 2;
    }
    
}

void radix_counting_sort(int num[], int place)
{
   int count[10] = {0};
   int output[SIZE] = {0};

   for(int i = 0; i < SIZE; i++){
       int index = num[i] / place;
       count[index%10]++;
   }
   for(int i = 0; i < 10-1; i++){
       count[i+1] += count[i];
   }
   int i = SIZE - 1;
   for(i; i >= 0; i--){
       int index = num[i] / place;
       output[count[index%10]-1] = num[i];
       count[index%10]--;
   }
   for(int i = 0; i < SIZE; i++){
       num[i] = output[i];
   }
}
void radix_sort(int num[])
{
    int place = 1;
    while ( (100 - 1) / place > 0){
        radix_counting_sort(num, place);
        place *= 10;
    }
    
}
int main()
{
    srand(time(NULL));

    int num[MAX] = {0};
    for(int i = 0; i < SIZE; i++){
        num[i] = rand() % 100 + 1; 
    }

    //bubble_sort(num);
    //counting_sort(num);
    //insertion_sort(num);
    quick_sort(num, 0, SIZE-1);
    //selection_sort(num);
    //shell_sort(num);
    //radix_sort(num);
    print(num);
   
}