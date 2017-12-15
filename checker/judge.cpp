#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
#include <random>
using namespace std;

const int maxn = 1010, maxm = 1010;
const int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
const char pressChar[4] = {'U', 'D', 'L', 'R'};
struct Point {
    int x, y;
    bool operator != (const Point &rhs) const {
        return x != rhs.x || y != rhs.y;
    }
    bool operator == (const Point &rhs) const {
        return x == rhs.x && y == rhs.y;
    }
};

int n, m, Map[maxn][maxm], Row, Col, Len;
Point Head, Food;
deque<Point> Body;
std::random_device rd;
std::mt19937 rng(rd());


int get_random(int Min, int Max) {
    /*const int p = 107, q = 233, M = 297;
    random_tmp = (random_tmp * p + q) % (Max - Min + 1) + Min;
    return random_tmp;*/
    std::uniform_int_distribution<int> uni(Min, Max);
    return uni(rng);
}

bool getFood(Point &ret) {
    vector<Point> Choice;
    for (int row = 1; row <= n; ++row)
        for (int col = 1; col <= m; ++col)
            if (Map[row][col] != 1) Choice.push_back({row, col});
    if (!Choice.size()) return false;
    int cho = get_random(0, Choice.size() - 1);
    ret = Choice[cho];
    return true;
}

inline bool inSpace(int x, int y) {
    return x >= 1 && x <= n && y >= 1 && y <= m;
}

int main(int argc, char* argv[])
{
	FILE *finit, *fpress, *ffood;

	finit = fopen("init", "w+");
	fpress = fopen("press", "w+");
	ffood = fopen("food", "w+");

    n = m = 20;
    printf("%d %d\n", n, m); fflush(stdout);
    Row = get_random(1, n); Col = get_random(1, m); Len = get_random(1, m - Col + 1);
    printf("%d %d %d\n", Row, Col, Len); fflush(stdout);

    Head = (Point){Row, Col + Len - 1};
    for (int j = Col; j < Col + Len; ++j) Body.push_back({Row, j});

    getFood(Food);
    printf("%d %d\n", Food.x, Food.y);  fflush(stdout);
    fprintf(finit, "%d %d\n%d %d %d\n%d %d\n", n, m, Row, Col, Len, Food.x, Food.y);
    while (true) {
        char s[5], press; scanf("%s", s);
        fputc(s[0], fpress);
        if (s[0] == 'E') {
            printf("-1\n"); fflush(stdout);
            break;
        }
        int dir;
        for (int i = 0; i < 4; ++i)
            if (pressChar[i] == s[0]) {
                dir = i;
                break;
            }
        Point nxtP = {dx[dir] + Head.x, dy[dir] + Head.y};
        int type = Map[nxtP.x][nxtP.y];
        if (!inSpace(nxtP.x, nxtP.y) || type == 1) {
                printf("%d\n", -1); fflush(stdout);
                break;
        } else {
            Body.push_back(nxtP);
            Head = nxtP;
            Map[nxtP.x][nxtP.y] = 1;
            if (nxtP == Food) {
                bool ret = getFood(Food);
                if (!ret) {
                    printf("-1\n"); fflush(stdout);
                    // return 0;
                    break;
                } else {
                    printf("1 %d %d\n", Food.x, Food.y); fflush(stdout);
                    fprintf(ffood, "%d %d\n", Food.x, Food.y);
                    Map[Food.x][Food.y] = 2;
                }
            } else {
                printf("0\n"); fflush(stdout);
                Map[Body.front().x][Body.front().y] = 0;
                Body.pop_front();
            }
        }
    }
    fclose(finit);
    fclose(fpress);
    fclose(ffood);
}
