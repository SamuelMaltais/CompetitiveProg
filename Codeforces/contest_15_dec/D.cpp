#include <iostream>
#include <vector>
#include <sstream>
#include <map>
using namespace std;

std::string join(const std::vector<int> &elements, const std::string &delimiter = " ")
{
    ostringstream oss;
    for (size_t i = 0; i < elements.size(); ++i)
    {
        if (i > 0)
        {
            oss << delimiter;
        }
        oss << elements[i];
    }
    return oss.str();
}

int main(int argc, char const *argv[])
{
    int n;

    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        int a;
        cin >> a;
        vector<int> v;
        vector<int> solution;
        int o;

        for (int i = 0; i < a; i++)
        {
            cin >> o;
            v.push_back(o);
        }
        map<int, int> m;
        m[v[0]] = 1;
        int curr_max = 1;
        solution.push_back(v[0]);

        for (int k = 1; k < v.size(); k++)
        {
            int elem = v[k];
            if (m[elem] == curr_max)
            {
                for (int j = 1; j < a + 1; j++)
                {
                    int ok = j;
                    if (m[ok] != curr_max)
                    {
                        m[ok] = m[ok] + 1;
                        solution.push_back(ok);
                        break;
                    }
                }
            }
            else
            {
                m[elem] = m[elem] + 1;
                solution.push_back(elem);
                if (m[elem] > curr_max)
                    curr_max = m[elem];
            }
        }
        cout << join(solution) << endl;
    }

    return 0;
}
