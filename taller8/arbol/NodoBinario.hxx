#ifndef __NodoBinario__HXX__
#define __NodoBinario__HXX__
#include "NodoBinario.h"

template <class T>
NodoBinario<T>::NodoBinario(T& val)
{
    this->dato= val;
    this->hijoDer= nullptr;
    this->hijoIzq= nullptr;
}

template <class T>
T& NodoBinario<T>::obtenerDato()
{
    return this->dato;
}

template <class T>
void NodoBinario<T>::fijarDato(T& val)
{
    this->dato= val;
}

template <class T>
NodoBinario<T>* NodoBinario<T>::obtenerHijoIzq()
{
    return this->hijoIzq;
}

template <class T>
NodoBinario<T>* NodoBinario<T>::obtenerHijoDer()
{
    return this->hijoDer;
}

template <class T>
void NodoBinario<T>::fijarHijoIzq(NodoBinario<T> *izq)
{
    this->hijoIzq= izq;
}

template <class T>
void NodoBinario<T>::fijarHijoDer(NodoBinario<T> *der)
{
    this->hijoDer= der;
}


#endif
