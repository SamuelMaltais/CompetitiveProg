#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{

    int n, w, max;

    cin >> n;

    for (size_t i = 0; i < n; i++)
    {
        cin >> w, max;
        string s;

        int c = 0;
        for (size_t i = 0; i < w; i++)
        {
            cin >> s;
            max -= s.length();
            if (max >= 0)
            {
                c++;
            }
        }
        cout << c << endl;
    }

    return 0;
}
