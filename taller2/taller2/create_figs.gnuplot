set terminal png

p(x)=a2*x*x + a1*x + a0
l(x)=a0*x*(log(x)/log(2))

set output "Solucion1.png"
set title "Solucion1 timing"
set xlabel "Size (n)"
set ylabel "Time (s)"
fit p(x) "Solucion1.res" using 1:2 via a2, a1, a0
plot "Solucion1.res" using 1:2 with lines notitle, p(x)

set output "Solucion2.png"
set title "Solucion2 timing"
set xlabel "Size (n)"
set ylabel "Time (s)"
fit l(x) "Solucion2.res" using 1:2 via a0
plot "Solucion2.res" using 1:2 with lines notitle, l(x)

## eof - create_figs.gnuplot
