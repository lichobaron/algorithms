#ifndef __leerArchivos__HXX__
#define __leerArchivos__HXX__

#include "leerArchivos.h"

leerArchivos::leerArchivos() {}

void leerArchivos::leerPalabras(std::string s, std::set<std::string> &p)
{
    std::ifstream fs(s);
    std::string line;
    if (!fs.is_open())
    {
        std::cout << "El archivo " + s + " no existe o es ilegible" << std::endl;
    }
    else
    {
        while (!fs.eof())
        {
            getline(fs, line);
            line.erase(line.length()-1);
            p.insert(line);
        }
        fs.close();
    }
}

void leerArchivos::leerPyQ(std::string p, std::string q, std::vector<double> &P, std::vector<double> &Q)
{
    std::ifstream fs1(p);
    std::ifstream fs2(q);
    std::string line1;
    std::string line2;
    if (!fs1.is_open() && !fs2.is_open())
    {
        std::cout << "El archivo " + p + " o "+q+" no existe o es ilegible" << std::endl;
    }
    else
    {
        while (!fs1.eof())
        {
            getline(fs1, line1);
            getline(fs2, line2);
            P.push_back(atof(line1.c_str()));
            Q.push_back(atof(line2.c_str()));
        }
        getline(fs2, line2);
        Q.push_back(atof(line2.c_str()));
        fs1.close();
        fs2.close();
    }
}

void leerArchivos::leerDicc(std::string dic, std::vector<std::string> &D)
{
    std::ifstream fs(dic);
    std::string line;
    if (!fs.is_open() )
    {
        std::cout << "El archivo " +dic+" no existe o es ilegible" << std::endl;
    }
    else
    {
         while (!fs.eof())
        {
            getline(fs, line);
            D.push_back(line);
        }
        fs.close();
    }
}

#endif