#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
const int maxn = 1010, maxm = 1010;
const int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
const char pressChar[4] = {'U', 'D', 'L', 'R'};
struct Point {
    int x, y;
    bool operator != (const Point &rhs) const {
        return x != rhs.x || y != rhs.y;
    }
};
Point Food, Head;
int n, m, Row, Col, Len;
int Map[maxn][maxm], Vis[maxn][maxm];
Point Pre[maxn][maxm];
deque<Point> Body;

inline bool inSpace(int x, int y) {
    return x >= 1 && x <= n && y >= 1 && y <= m;
}

int getPress(Point pre, Point nxt) {
    for (int dir = 0; dir < 4; ++dir)
        if (nxt.x == dx[dir] + pre.x && nxt.y == dy[dir] + pre.y)
            return dir;
}

void printBody() {
    for (int i = 0; i < Body.size(); ++i) printf("%d %d\n", Body[i].x, Body[i].y);
    puts("");
}
void Move(int dir) {
    Point nxt = (Point) {Body.back().x + dx[dir], Body.back().y + dy[dir]};
    if (nxt != Food) {
        Map[Body.front().x][Body.front().y] = 0;
        Body.pop_front();
    }
    Body.push_back(nxt);
    Map[nxt.x][nxt.y] = 1;
    Head = nxt;
}

bool couldEatFood() {
    queue<Point> st;
    memset(Vis, 0, sizeof Vis); Vis[Head.x][Head.y] = 1; Pre[Head.x][Head.y] = {-1, -1};
    st.push(Head);

    bool flag = false;
    while (!st.empty()) {
        Point tmp = st.front(); st.pop();
        for (int dir = 0; dir < 4; ++dir) {
            int destX = tmp.x + dx[dir], destY = tmp.y + dy[dir];
            if (inSpace(destX, destY) && !Vis[destX][destY] && Map[destX][destY] != 1) {
                st.push((Point) {destX, destY});
                Vis[destX][destY] = 1;
                Pre[destX][destY] = {tmp.x, tmp.y};
                if (Map[destX][destY] == 2) {
                    flag = true;
                    break;
                }
            }
        }
        if (flag) break;
    }
    if (!flag) {
        puts("E"); fflush(stdout);
        return false;
    }
    Point tmp = Food;
    vector<int> outDir;
    while (Pre[tmp.x][tmp.y] != (Point){-1, -1}) {
        Point pre = Pre[tmp.x][tmp.y];
        outDir.push_back(getPress(pre, tmp));
        tmp = pre;
    }
    for (int i = (int)outDir.size() - 1; i >= 0; --i) {
        printf("%c\n", pressChar[outDir[i]]); fflush(stdout);
        int info; scanf("%d", &info);
        Move(outDir[i]);
        if (info == -1) return false;
    }
    return true;
}

int main() {
    scanf("%d%d", &n, &m);

    scanf("%d%d%d", &Row, &Col, &Len);
    for (int j = Col; j < Col + Len; ++j) {
        Body.push_back((Point) {Row, j});
        Map[Row][j] = 1;
    }
    Head = (Point) {Row, Col + Len - 1};

    scanf("%d%d", &Food.x, &Food.y);
    Map[Food.x][Food.y] = 2;

    while (couldEatFood()) {
        scanf("%d%d", &Food.x, &Food.y);
        Map[Food.x][Food.y] = 2;
    }
    return 0;
}
