 /* ProPlayer.i */
 %module ProPlayer
 %{
    /* Put header files here or function declarations like below */
    extern const char* simulatePlay(const char * board,int me);
 %}
extern const char* simulatePlay(const char *board,int me);