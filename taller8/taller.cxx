#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include <time.h>
#include <fstream>
#include "leerArchivos.h"
#include "./arbol/ArbolBinarioOrd.h"

using namespace std;

void Print_Matrix(TMatrix &M)
{
    for (int i = 0; i < M.size(); i++)
    {
        for (int j = 0; j < M[i].size(); j++)
        {
            if (M[i][j] == inf)
            {
                printf(" %.3f ", -1.0);
            }
            else
            {
                printf(" %.3f ", M[i][j]);
            }
        }
        cout << endl;
    }
}

ArbolBinarioOrd<string> *Build_OptBinTree(vector<double> &P, vector<double> &Q, vector<string> &words)
{
    TMatrix W(P.size() + 1, TRow(P.size(), 0));
    TMatrix M(P.size() + 1, TRow(P.size() + 1, 0));
    TMatrix R(P.size(), TRow(P.size(), 0));
    for (int i = 0; i < P.size(); i++)
    {
        W[i][i] = Q[i] + P[i] + Q[i + 1];
        M[i][i] = Q[i];
        for (int j = i + 1; j < P.size(); j++)
        {
            W[i][j] = W[i][j - 1] + P[j] + Q[j + 1];
            M[i][j] = inf;
        }
    }
    for (int i = 0; i < Q.size(); i++)
    {
        M[i][Q.size() - 1] = inf;
    }
    M[Q.size() - 1][Q.size() - 1] = Q[Q.size() - 1];

    for (int l = 1; l <= P.size(); l++)
    {
        for (int i = 0; i < P.size() - l + 1; i++)
        {
            int j = i + l;
            for (int r = i; r < j; r++)
            {
                double v = M[i][r] + M[r + 1][j] + W[i][j - 1];
                if (v < M[i][j])
                {
                    M[i][j] = v;
                    R[i][j - 1] = r + 1;
                }
            }
        }
    }
    /*
    Print_Matrix(W);
    cout<<endl;
    Print_Matrix(M);
    cout<<endl;
    Print_Matrix(R);
    */
    //M y W no son necesarios enla creacion del arbol
    M.clear();
    W.clear();
    ArbolBinarioOrd<string> *arbol = new ArbolBinarioOrd<string>(R, words, P.size());
    return arbol;
}

int main()
{
    vector<string> words;
    vector<double> P;
    vector<double> Q;
    leerArchivos lector = leerArchivos();
    lector.leerPyQ("P_prince.csv", "Q_prince.csv", P, Q);
    lector.leerDicc("W_prince.csv", words);
    ArbolBinarioOrd<string> *arbol = Build_OptBinTree(P, Q, words);

    std::ofstream fs("OT.res");
    for (int i = 0; i < 500; i++)
    {
        int cant_max = (i + 1) * 100;
        double tfinal;
        clock_t begin = clock();
        for (int j = 0; j < cant_max; j++)
        {
            srand(time(NULL));
            int num = rand() % words.size() + 1;
            std::string s = words.at(num);
            NodoBinario<string> *busqueda = arbol->buscar(arbol->obtenerRaiz(), s);
        }
        tfinal = (double)(clock() - begin) / CLOCKS_PER_SEC;
        fs << cant_max << " " << tfinal << '\n';
    }
    fs.close();
}
