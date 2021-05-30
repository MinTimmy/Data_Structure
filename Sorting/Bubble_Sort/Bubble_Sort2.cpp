#include <iostream>

using namespace std;

int len = 0;
void print(int num[])
{
    for(int i = 0; i < len; i++){
        cout << num[i] << ' ';
    }
}
void bubble_sort(int num[])
{
    bool swap = true;
    while (swap)
    {
        swap = false;
        for(int i = 0; i < len - 1; i++){
            if(num[i] < num[i + 1]){
                int temp = num[i];
                num[i] = num[i+1];
                num[i+1] = temp;
                swap = true;
            }
        }
    }
}
int main()
{
    int num[5] = {12,45,89,15,2};
    len = sizeof(num) / sizeof(int);

    bubble_sort(num);
    print(num);

    

    //cout << sizeof(num) / sizeof(int);
}