#include <iostream>

using namespace std;

int len = 0;
#define MAX 100
void print(int num[])
{
    for(int i = 0; i < len; i++){
        cout << num[i] << ' ';
    }
}
void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int num[], int low, int high)
{
    int pivot = num[high];
    int i = low - 1;

    for(int j = low; j <= high - 1; j++){
        if(num[j] < pivot){
            i++;
            swap(&num[i], &num[j]);
        }
    }

    swap(&num[i+1], &num[high]);
    return (i+1);

}

void quick_sort(int num[], int low, int high)
{
   if(low < high){
       int pi = partition(num, low, high);
       quick_sort(num, low, pi - 1);
       quick_sort(num, pi + 1, high);
   }

   
}
int main()
{
    int num[5] = {12,45,89,15,2};
    len = sizeof(num) / sizeof(int);

    quick_sort(num, 0, len-1);
    print(num);
    //cout << sizeof(num) / sizeof(int);
}