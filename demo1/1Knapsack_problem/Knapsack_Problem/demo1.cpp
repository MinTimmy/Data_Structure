#include <iostream>
#include <iomanip>

using namespace std;

#define N 5
#define M 17

void printTable(char[], int [], int[]);
void printAnswer(char[], int [], int[], int[]);
int main()
{
    char item[] = "ABCDE";
    int size[] = {3,4,7,8,9};
    int value[] = {4,5,10,11,13};
    int cost[M] = {0};
    int best[17] = {-1};
    for(int i = 0;i < M; i++){
        best[i] = -1;
    }
    for(int j = 1; j <= N; j++){
        for(int i = 1; i <= M; i++){
            if(i - size[j-1] >= 0){
                if(cost[i-1] < cost[(i-size[j-1]-1) < 0 ? 0 : (i-size[j-1]-1)] + value[j-1]){
                    cost[i-1] = cost[(i-size[j-1]-1) < 0 ? 0 : (i-size[j-1]-1)] + value[j-1];
                    best[i-1] = j-1;
                }
            }
        }
        printTable(item, cost, best);
    }

    printAnswer(item, cost, best,size);

}
void printTable(char item[], int cost[], int best[])
{
    for(int i = 0; i < M; i++){
        cout << setw(3) << cost[i] << "  ";
    }
    cout << '\n';
    for(int i = 0; i < M; i++){
        if(best[i] == -1)
            cout << setw(3) << "?" << "  ";
        else
            cout << setw(3) << item[best[i]] << "  ";
    }
    cout << '\n' << "-----------------------------------------------------------------------------------------------------------------------------" << "\n";
 
}
void printAnswer(char item[], int cost[], int best[], int size[])
{
    for(int i = M - 1; i >= 0 && cost[i] != 0; i--){
        int pivot = i;
        cout << cost[pivot] << " = " << item[best[pivot]];
        pivot -= size[best[pivot]];
        while(pivot >= 0){
            if(best[pivot] == -1 )
                break;
            cout << " + " << item[best[pivot]];
            pivot -= size[best[pivot]];
        }
        cout << '\n';
    }
}