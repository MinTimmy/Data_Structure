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
void selection_sort(int num[])
{
   for(int i = 0; i < len; i++){
       int min = i;
       for(int j = i + 1; j < len; j++){
           if(num[min] > num[j]){
               min = j;
           }
        if(min != i){
            int temp = num[min];
            num[min] = num[i];
            num[i] = temp;
        }
       }
   }
}
int main()
{
    int num[5] = {12,45,89,15,2};
    len = sizeof(num) / sizeof(int);

    selection_sort(num);
    print(num);

    

    //cout << sizeof(num) / sizeof(int);
}