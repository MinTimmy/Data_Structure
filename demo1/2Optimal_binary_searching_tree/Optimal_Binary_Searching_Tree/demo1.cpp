#include <iostream>
#include <iomanip>

using namespace std;

#define N 7

void printTable(char items[], int[][N] , int[][N]);
int main()
{
    
    int cost[N][N];
    char items[] = "ABCDEFG?";
    int freq[] = {4,2,1,3,5,2,1};
    // const int N = sizeof(freq) / sizeof(int);

    int best[N][N];

    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++){
            best[i][j] = 7;
            if(i == j)
                cost[i][j] = freq[i];
            else if(i > j)
                cost[i][j] = 0;
            else   
                cost[i][j] = INT32_MAX;
        }
    // for(int i = 0; i < N; i++){
    //     for(int j = 0; j < N; j++)
    //         cout << cost[i][j] << " ";
    //     cout << "\n"; 
    // }
    // cout << cost[0][0]; 
    int temp;
    for(int j = 1; j < N ; j++)
        for(int i = 0; i < N - j; i++){
            for(int k = i; k <= i + j; k++){
                if(k-1 < 0)
                    // temp = 0 + cost[k+1][i+j+1];
                    temp = 0 + cost[k+1][i+j];
                    // temp = cost[1][1];
                else if(k+1 >= N)
                    temp = cost[i][k-1] + 0;
                    // temp = cost[i][k-1] + 0;
                else
                    temp = cost[i][k-1] + cost[k+1][i+j];
                if(temp < cost[i][i+j]){
                    // cout << cost[i][i+j] << "\t" << temp << "\n";
                    cost[i][i+j] = temp;
                    best[i][i+j] = k;
                }
                
            }
            temp = 0;
            for(int k = i; k <= i + j; k++)
                temp += freq[k];
            cost[i][i+j] = cost[i][i+j] + temp;
        }
    printTable( items, cost, best);
    
}
void printTable(char items[], int cost[][N], int best[][N])
{
    for(int i = 0; i < N; i++){
        cout << "  |    " << items[i];
    }

    cout << "\n";
    for(int i = 0; i < N; i++){
        cout << items[i];
        for(int j = 0; j < N; j++){
            // cout << " | " << items[best[i][j]] << cost[i][j];
            // cout << " | " << best[i][j] << cost[i][j];
            cout << " | " << setw(5) << items[best[i][j]]<<  cost[i][j];
            // cout << " | " << setw(5) << best[i][j];
        }
        cout << "\n";
    }
}