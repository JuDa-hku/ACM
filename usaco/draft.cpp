/*
ID: judanju1
PROG: test
LANG: C++    
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main() {
    ofstream fout ("test.out");
    ifstream fin ("test.in");
    int a, b;
    fin >> a >> b;
    fout << a+b << endl;
    return 0;
}
