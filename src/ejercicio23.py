a=float(raw_input('Valor de a: '))
b=float(raw_input('Valor de b: '))
if(a!=0):
  x=-b/a
  print 'La solucion es: ',x
if((a==0) and (b!=0)):
  print 'No hay solucion'
if((a==0) and (b==0)):
  print 'La ecuacion tiene infinitas soluciones'
