#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

#define N 6

string answer;
void printTable(char [], int [][N], int [][N]);
void printAnswer(char [], int [][N], int [][N]);
int main()
{
    int r[] = {4,2,3,1,2,2,3};
    char item[] = "ABCDEF";
    int cost[N][N] = {0};
    int best[N][N];

    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++){
            if( i > j)
                cost[i][j] = -1;
            else if(i < j)
                cost[i][j] = INT32_MAX;
            best[i][j] = -1;
        }

    for(int j = 1; j <= N - 1; j++)
        for(int i = 1; i <= N - j; i++)
            for(int k = i + 1; k <= i + j; k++){
                int t = cost[i-1][k-1-1] + cost[k-1][i+j-1] + r[i-1] * r[k-1] * r[i+j+1-1];
                if(t < cost[i-1][i+j-1]){
                    cost[i-1][i+j-1] = t;
                    best[i-1][i+j-1] = k-1;
                    cout << i - 1 << ' ' << i + j - 1 << ' ' << item[best[i-1][i + j -1]] << '\n';
                }
            }
    printTable(item, cost, best);
    answer = item;
    // answer = "ABCDE";
}
void printTable(char item[], int cost[][N], int best[][N])
{
    cout << " ";
    for(int i = 0; i < N ; i++){
        cout << " | " << "   " << item[i] << " ";
    }

    cout << "\n";

    for(int i = 0; i < N; i++){
        cout << "--------------------------------------------------------------\n" << item[i];
        for(int j = 0; j < N; j++){
            if(i > j){
                cout << " | " << setw(5) << "?";
            }
            else if(i == j){
                cout << " | " << setw(5) << "0";
            }
            else{
                cout << " | " << setw(4) << cost[i][j] << item[best[i][j]];
            }
        }
        cout << "\n";
    }
}
void printAnswer(char items[], int cost[][N], int best[][N], int right, int left)
{
    int i = right;
    
    
}
     