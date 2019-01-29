#include <iostream>
#include <vector>
#include <limits>
#include <random>
#include <string>
#include <tuple>

using namespace std;

string makeCoor(int j, int i);
bool validPlay(int i, int j, int n);
int otherPlayer(int me);
int cellC(int x, int y, int n);
int impCell(int x, int y, int n);
vector<vector<int>> makeBoard( const char *c);
vector<vector<int>> getPlays(vector<vector<int>> board, int n, int me);
//Interfaz para python
const char* simulatePlay(const char *cadena, int me);

/*
Función makeCoor: hace una coordenada en el formato <letra,numero>
    1. Entradas:
        - j: indice del tablero
        - i: indice del tablero
    2. Salidas
        - Coordenada formato <letra,numero>
*/
string makeCoor(int j, int i){
    string f(1, char('a')+i);
    string s = to_string(j+1);
    return f+s;
}

/*
Función validPlay: verifica que una coordenada este en el rango del tablero
    1. Entradas:
        - j: indice del tablero
        - i: indice del tablero
        - n: tamaño del tablero
    2. Salidas
        - True: si se encuentra en el rango
        - False: si no se encuentra en el rango
*/
bool validPlay(int i, int j, int n){
    return 0 <= i && 0 <= j && i < n && j < n;
}

/*
Función otherPlayer: dado un jugador retorna su adversario
    1. Entradas:
        - me: jugador actual
    2. Salidas
        - 0: si el jugador actual es 1
        - 1: si el jugador actual es 0
*/
int otherPlayer(int me){
    if(me == 0){
        return 1;
    }
    return 0;
}

/*
Función cellC: retorna el valor de una posición C
    1. Entradas:
        - j: indice del tablero
        - i: indice del tablero
        - n: tamaño del tablero
    2. Salidas
        - (-100): si es una posición C
        - 0: si no es una posición C
*/
int cellC(int x, int y, int n){
    if ((x==1 && y==0) || (x==0 && y==1) || (x==1 && y==1) || (x==0 && y==n-2) || (x==1 && y==n-1) || (x==1 && y==n-2) ||
       (x==n-2 && y==0) || (x==n-1 && y==1) || (x==n-2 && y==1) || (x==1 && y==0) || (x==n-1 && y==n-2) || (x==n-2 && y==n-2) ||
       (x==n-2 && y==n-1)){
        return -100;    
    }
    return 0;
}

/*
Función isCellC: verifica si es una posición es C
    1. Entradas:
        - j: indice del tablero
        - i: indice del tablero
        - n: tamaño del tablero
    2. Salidas
        - True: si es una posición C
        - False: si no es una posición C
*/
bool isCellC(int x, int y, int n){
    if ((x==1 && y==0) || (x==0 && y==1) || (x==1 && y==1) || (x==0 && y==n-2) || (x==1 && y==n-1) || (x==1 && y==n-2) ||
       (x==n-2 && y==0) || (x==n-1 && y==1) || (x==n-2 && y==1) || (x==1 && y==0) || (x==n-1 && y==n-2) || (x==n-2 && y==n-2) ||
       (x==n-2 && y==n-1)){
        return true;    
    }
    return false;
}

/*
Función impCell: aumenta el valor de una posición de la esquina o lateral
    1. Entradas:
        - j: indice del tablero
        - i: indice del tablero
        - n: tamaño del tablero
    2. Salidas
        - 100: si es una posición de la esquina
        - 10: si es una posición lateral
        - 0: si no es ninguna de las anteriores
*/
int impCell(int x, int y, int n){
    if ( (x==0 && y == 0) || (x==0 && y == n-1) || (x==n-1 && y == 0) || (x==n-1 && y == n-1) ){
        return 100;
    }
    else if( (x==0 || x==n-1 || y==0 || y==n-1) && !isCellC(x,y,n)){
        return 10;
    }
    return 0;
}

/*
Función makeBoard: construye el tablero de juego
    1. Entradas:
        - c: cadena serializada del tablero
    2. Salidas
        - board: Tablero de juego
*/
vector<vector<int>> makeBoard( const char *c)
{
    std::string s = std::string(c);
    std::vector<std::vector<int>> board;
    int tam =(int) std::sqrt(s.size());
    int avance = 0;
    const char * s2 = s.c_str();   
    for (int i=0; i < tam ; i++)
    {
        std::vector<int> row;
        for (int j=0; j < tam ; j++)
        {
            int n = static_cast<int>(s2[avance] - char('0'));
            row.push_back(n);
            avance ++;
        }
        board.push_back(row);
    }
    return board;
}

/*
Función getPlays: aumenta el valor de una posición de la esquina o lateral
    1. Entradas:
        - board: Tablero de juego
        - n: tamaño del tablero
        - me: jugador actual
    2. Salidas
        - plays: Secuencia de las posibles jugadas con su respectivo valor
*/
vector<vector<int>> getPlays(vector<vector<int>> board, int n, int me){
    //Posibles direcciones
    int dir[8][2] = {
                        { 0,  1 }, {  1,  1 }, {  1, 0 }, {  1, -1 },
                        { 0, -1 }, { -1, -1 }, { -1, 0 }, { -1,  1 }
                    };
    int x = 0, y = 0;
    vector<vector<int>> plays;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            //Busca jugada si la posición está vacia
            if(board[i][j] == 2){
                bool onevalid = false;
                int f = 0;
                //Se mueve en las 8 direcciones
                for(int ix = 0; ix<8; ix++){
                    x=i, y=j;
                    x+=dir[ix][0];
                    y+=dir[ix][1];
                    if(validPlay(x,y,n) && board[x][y] == otherPlayer(me)){ 
                        bool real = false;
                        int faux = 0;
                        //Juega mientras este en el tablero
                        while (validPlay(x,y,n)){
                            //Si encuentra una pos vacia, se anula la jugada
                            if (board[x][y] == 2){
                                real = false;
                                break;
                            }
                            //Si encuentra una pos propia, se valida la jugada
                            if (board[x][y] == me){
                                real = true;
                                break;
                            }
                            x+=dir[ix][0];
                            y+=dir[ix][1];
                            faux++;
                        }
                        //Si la jugada es valida, se aumenta su valor
                        if (real){
                            f+=faux;
                            onevalid = true;
                        }
                    }
                }
                //Si algún movimiento fue valido, se guarda la posibles posicion para jugar
                if (onevalid){
                    plays.push_back({i,j,f+cellC(i,j,n)+impCell(i,j,n)});                   
                }
            }
        }
    }
    return plays;
}

/*
Función simulatePlay: simula la mejor jugada, dado un tablero
    1. Entradas:
        - cadena: Tablero de juego serializado
        - me: jugador actual
    2. Salidas
        - Coor: posición de juego en formato <letra-número>
        - NP: si no existe una posición de juego jugable
*/
const char* simulatePlay(const char *cadena, int me){
    vector<vector<int>> board = makeBoard(cadena);
    int n = board.size();
    //Se obtienen las posibles jugadas del jugador actual
    vector<vector<int>> plays = getPlays(board,n,me);
    vector<int> totals;
    for(int i = 0; i < plays.size(); i++){
        //Se establece el valor positivo de la jugada <las fichas ganadas>
        int total = plays[i][2];
        //Se simula la jugada
        board[plays[i][0]][plays[i][1]] = me;
        //Se obtienen las juagadas del adversario dada la jugada anterior
        vector<vector<int>> other_plays = getPlays(board,n,otherPlayer(me));
        for(int j = 0; j < other_plays.size(); j++){
            //Se resta el valor de las jugadas del adversario
            total -= other_plays[j][2];
        }
        totals.push_back(total);
        //Se establece el valor original de la posición
        board[plays[i][0]][plays[i][1]] = 2;
    }
    int max = numeric_limits<int>::min();
    vector<int> options;
    //Se busca la jugada con mas ganancia
    for(int i = 0; i < totals.size(); i++){
        if(totals[i] > max){
            max = totals[i];
        }
    }
    cout<<"Soy el player "<<me<<endl;
    //Verifica si existe alguna jugada posible
    if (totals.size() > 0){
        //Busca los maximos en las jugadas posibles
        for(int i = 0; i < totals.size(); i++){
            cout<< makeCoor(plays[i][0],plays[i][1])<<" -> t: "<<totals[i]<<endl;
            //Si alguna jugada también es maxima, se añade a las opciones
            if(totals[i] == max){
                options.push_back(i);
            }
        }
        std::random_device r;
        std::default_random_engine e1(r());
        std::uniform_int_distribution<int> uniform_dist(0, options.size()-1);
        int mean = uniform_dist(e1);
        //Escoge aleatoriamente una jugada de las jugadas máximas
        return makeCoor(plays[options[mean]][0],plays[options[mean]][1]).c_str();
    }
    //Muestra que no existe una posible jugada
    cout<<"No hay donde jugar!"<<endl;
    string error = "NP";
    return error.c_str();
}



