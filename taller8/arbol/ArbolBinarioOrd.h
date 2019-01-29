#ifndef __ArbolBinarioOrd__HH__
#define __ArbolBinarioOrd__HH__

using namespace std;
#include "NodoBinario.h"
#include "MyMatrix.h"
template<class T>
class ArbolBinarioOrd
{
protected:
    NodoBinario<T> *raiz;

public:
    ArbolBinarioOrd(TMatrix &Costos, vector<string> &words, int tam);
    NodoBinario<T>* obtenerRaiz();
    ~ArbolBinarioOrd()= default;
    NodoBinario<T>* buscar(NodoBinario<T> *nodo, T& val);
};
#include "ArbolBinarioOrd.hxx"
#endif
