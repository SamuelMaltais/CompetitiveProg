#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const long long MOD = 998244353;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n, m, d;
        cin >> n >> m >> d;

        vector<string> grid(n);
        for (int i = 0; i < n; ++i)
            cin >> grid[i];

        int vertical_reach = floor(sqrt(d * d - 1));

        vector<vector<long long>> ways(n, vector<long long>(m, 0));

        for (int i = 0; i < m; ++i)
            if (grid[0][i] == 'X')
                ways[0][i] = 1;

        int row = 0;
        vector<long long> oldRow = ways[row];

        for (int i = 0; i < m; ++i)
        {
            if (grid[row][i] == 'X')
            {
                long long curr_ways = oldRow[i];
                for (int j = max(0, i - d); j <= min(m - 1, i + d); ++j)
                {
                    if (i != j)
                        curr_ways = (curr_ways + oldRow[j]) % MOD;
                }
                ways[row][i] = curr_ways;
            }
        }

        for (int row = 1; row < n; ++row)
        {
            for (int i = 0; i < m; ++i)
            {
                if (grid[row][i] == 'X')
                {
                    long long curr_ways = 0;
                    for (int j = max(0, i - vertical_reach); j <= min(m - 1, i + vertical_reach); ++j)
                    {
                        curr_ways = (curr_ways + ways[row - 1][j]) % MOD;
                    }
                    ways[row][i] = curr_ways;
                }
            }

            oldRow = ways[row];
            for (int i = 0; i < m; ++i)
            {
                if (grid[row][i] == 'X')
                {
                    long long curr_ways = oldRow[i];
                    for (int j = max(0, i - d); j <= min(m - 1, i + d); ++j)
                    {
                        if (i != j)
                            curr_ways = (curr_ways + oldRow[j]) % MOD;
                    }
                    ways[row][i] = curr_ways;
                }
            }
        }

        long long total_ways = 0;
        for (int i = 0; i < m; ++i)
            total_ways = (total_ways + ways[n - 1][i]) % MOD;

        cout << total_ways << endl;
    }

    return 0;
}
