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
void counting_sort(int num[])
{
    int count[MAX] = {0};
    int output[len] = {0};

    for(int i = 0; i < len; i++){
        count[num[i]]++;
    }
    for(int i = 0; i < MAX - 1; i++){
        count[i+1] += count[i];
    }
    for(int i = 0; i < len; i++){
        output[count[num[i]]-1] = num[i];
        count[num[i]]--;
    }
    print(output);
}
int main()
{
    int num[5] = {12,45,89,15,2};
    len = sizeof(num) / sizeof(int);

    counting_sort(num);
    //print(num);

    

    //cout << sizeof(num) / sizeof(int);
}