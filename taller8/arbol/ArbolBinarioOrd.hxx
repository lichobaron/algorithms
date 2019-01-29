#ifndef __ArbolBinarioOrd__HXX__
#define __ArbolBinarioOrd__HXX__

#include "ArbolBinarioOrd.h"
#include <queue>

using namespace std;

template <class T>
ArbolBinarioOrd<T>::ArbolBinarioOrd(TMatrix &Costos, vector<string> &words, int tam)
{
  queue<vector<int>> colaTriplets;
  int r = Costos[0][tam-1];
  vector<int> r1= {r,0,tam-1};
  queue<NodoBinario<string> *> colaNodos;
  NodoBinario<string> *froot = new NodoBinario<string>(words[r-1]);
  colaNodos.push(froot);
  this->raiz= froot;
  colaTriplets.push(r1);
  int n=0;
  while(n<tam){
    //cout<<"-----------------------"<<endl;
    vector<int> triplet = colaTriplets.front();
    //cout<<triplet[0]<<"-"<<triplet[1]<<"-"<<triplet[2]<<endl;
    //cout<<words[triplet[0]-1]<<endl;
    NodoBinario<string> *root = colaNodos.front();
    int iIzq = triplet[1];
    int jIzq = triplet[0]-2;
    if(jIzq >= 0 && jIzq < triplet[0]-1){
      int rIzq = Costos[iIzq][jIzq];
      if(rIzq<triplet[0] && rIzq != 0){
        triplet = {rIzq, iIzq, jIzq};
        colaTriplets.push(triplet);
        NodoBinario<string> *hijoIzq = new NodoBinario<string>(words[triplet[0]-1]);
        root->fijarHijoIzq(hijoIzq);
        colaNodos.push(hijoIzq);
        //cout<<triplet[0]<<endl;
      }
    }
    triplet = colaTriplets.front();
    int iDer = triplet[0];
    int jDer = triplet[2];
    if(iDer < tam && iDer >= triplet[0]){
      int rDer = Costos[iDer][jDer];
      if(rDer>triplet[0] && rDer != 0){
        triplet = {rDer, iDer, jDer};
        colaTriplets.push(triplet);
        NodoBinario<string> *hijoDer = new NodoBinario<string>(words[triplet[0]-1]);
        root->fijarHijoDer(hijoDer);
        colaNodos.push(hijoDer);
        //cout<<triplet[0]<<endl;
      } 
    }
    colaTriplets.pop();
    colaNodos.pop();
    n++;
  }
}  

template <class T>
NodoBinario<T>* ArbolBinarioOrd<T>::obtenerRaiz(){
  return this->raiz;
}

template <class T>
NodoBinario<T>* ArbolBinarioOrd<T>::buscar(NodoBinario<T> *nodo, T& val){
  if(nodo->obtenerDato()==val){
    return nodo;
  }
  if(val<nodo->obtenerDato()){
    return buscar(nodo->obtenerHijoIzq(), val);
  }
  if(val>nodo->obtenerDato()){
    return buscar(nodo->obtenerHijoDer(), val);
  }
  return nullptr;
}

#endif
