#include <iostream>
using namespace std;

int main()
{
    string line;
    cin >> line;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int start, end, count;
        count = 0;
        cin >> start >> end;
        bool flag = false;

        while (line[start] == line[end])
        {
            start++;
            end++;
            count++;
        }
        cout << count << endl;
    }

    return 0;
}