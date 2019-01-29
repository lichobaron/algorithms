#ifndef __leerArchivos__HH__
#define __leerArchivos__HH__

#include <fstream>
#include <iostream>
#include <set>
#include <vector>
#include <string.h>

class leerArchivos{
    protected:
        
    public:
    leerArchivos();
    void leerPalabras(std::string s, std::set<std::string> &p);
    void leerPyQ(std::string p, std::string q, std::vector<double> &P, std::vector<double> &Q);
    void leerDicc(std::string dic, std::vector<std::string> &D);
};


#include "leerArchivos.hxx"
#endif