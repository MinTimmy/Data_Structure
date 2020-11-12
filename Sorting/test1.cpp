#include<iostream>
#include <cmath>
#include<string.h>
using namespace std;

void test(char n[][3])
{
    //cout << n[0][0];
    n[0][0] = '1';
    //n[0][1] = "9";
}
int main()
{
    char m[][3] = {"01","02"};
    //m[0][0] = '9';
    test(m);
    cout << pow(2,2);
    //test(data);
}