#include <iostream>

using namespace std;

const int N = 5;
const int INF = 100000;
char items[] = "ABCDE";

void show(int a[N][N], int p[N][N])
{
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(a[i][j] == INF)
                cout << "I"; 
            else
                cout << a[i][j];
            cout << items[p[i][j]] << '\t';
        }
        cout << '\n';
    }
    cout << "\n\n--------------------------------------------------\n\n";
}
int main()
{
    int a[N][N] = {
        {0,1,INF,INF,4},
        {1,0,5,1,INF},
        {INF, 5,0,2,INF},
        {INF, 1,2,0,1},
        {4,INF,INF,1,0}
    };
    int p[N][N] = {
        {0,1,2,3,4},
        {0,1,2,3,4},
        {0,1,2,3,4},
        {0,1,2,3,4},
        {0,1,2,3,4}
    };
    show(a,p);
    for(int j = 0; j < N; j++){
        for(int i = 0; i < N; i++){
            for(int k = 0; k < N; k++){
                if((i != j) && (j != k)){
                    if(a[i][k] > a[i][j] + a[j][k]){
                        a[i][k] = a[i][j] + a[j][k];
                        p[i][k] = p[i][j];
                    }
                }
            }
        }
        show(a,p);
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(i != j){
                int temp = i;
                cout << items[i] << "->";
                while(p[temp][j] != j){
                    cout << items[p[temp][j]] << "->";
                    temp = p[temp][j];
                }
                cout << items[p[temp][j]] << " = " << a[i][j] << '\n';
            }
        }
    }

}