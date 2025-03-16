#include <iostream>
#include <vector>

using namespace std;

// 定义全局变量
int l, r, cnt;
vector<int> a, b;
vector<int> ans;

// 扩展函数
void expand() {
    l--;
    r++;
    // 前面两个加法，表示逆序后 l与 r对上，r与 l对上的数量
    // 后面减法是减去逆序前已对上的数量
    cnt += (a[l] == b[r]) + (a[r] == b[l]) - (a[l] == b[l]) - (a[r] == b[r]);
    ans[cnt]++;
}

int main() {
    int n;
    cin >> n;
    a.resize(n);
    b.resize(n);
    ans.resize(n + 1, 0);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];

    int fit = 0;
    for (int i = 0; i < n; i++) if (a[i] == b[i]) fit++;

    for (int i = 0; i < n; i++) {
        cnt = fit;      // 之所以放到 for + 双指针是因为这些逆序操作之间存在递推关系，不用每次都重新计算
        l = i + 1;
        r = i - 1;
        while (l - 1 >= 0 && r + 1 < n) expand();
    }

    for (int i = 0; i < n; i++) {      
        cnt = fit;
        l = i + 1;              // 处理偶数长度的逆序（上面只处理了奇数长度序列）
        r = i;
        while (l - 1 >= 0 && r + 1 < n) expand();
    }

    for (int x : ans) cout << x << endl;
    return 0;
}