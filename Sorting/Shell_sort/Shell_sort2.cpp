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
void shell_sort(int num[])
{
   int interval = len / 2;
   while (interval > 0)
   {
       for(int i = interval; i < len; i++){
           int temp = num[i];
           int j = i;
           while (j >=interval && num[j-interval] > temp)
           {
               num[j] = num[j-interval];
               j -= interval;
           }
           num[j] = temp;
       }
       interval /= 2;
   }
   
}
int main()
{
    int num[5] = {12,45,89,15,2};
    len = sizeof(num) / sizeof(int);

    shell_sort(num);
    print(num);
    //cout << sizeof(num) / sizeof(int);
}