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
void insertion_sort(int num[])
{
    int key;
    for(int i = 1; i < len; i++){
        key = num[i];
        int j = i - 1;
        while( j >= 0 && key < num[j]){
            num[j+1] = num[j];
            j--;
        }
        num[j+1] = key;
    }
}
int main()
{
    int num[5] = {12,45,89,15,2};
    len = sizeof(num) / sizeof(int);

    insertion_sort(num);
    print(num);

    

    //cout << sizeof(num) / sizeof(int);
}