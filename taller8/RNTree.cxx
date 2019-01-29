#include <stdlib.h>
#include <time.h>
#include <fstream>
#include "leerArchivos.h"

int main(int argc, char *argv[])
{
    leerArchivos *lA = new leerArchivos();
    std::set<std::string> w;
    std::vector<std::string> d;
    lA->leerPalabras("W_prince.csv", w);
    lA->leerDicc("W_prince.csv", d);

    std::ofstream fs("Set.res");
    for (int i = 0; i < 500; i++)
    {
        int cant_max = (i+1) * 100;
        double tfinal;
        clock_t begin = clock();
        for (int j = 0; j < cant_max; j++)
        {
            srand(time(NULL));
            int num = rand()%d.size()+1;
            std::string s= d.at(num);
            
            std::set<std::string>::iterator it;
            it = w.find(s);
        }
        tfinal = (double)(clock()-begin)/CLOCKS_PER_SEC;
        fs << cant_max << " " << tfinal << '\n';
    }
    fs.close();
}