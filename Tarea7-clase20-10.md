# *Tarea 7  de la clase correspondiente al día 20 de Octubre de 2022*

**Universidad Autónoma de Nuevo León**

**Facultad de Físico Matemáticas**

**Maestría en Ciencia de Datos**

**Hecha por Ma. Luisa Argáez Salcido**

**Correo Universitario: maria.argaezs@uanl.edu.mx**

**Matricula 2173261**


## **Instrucciones**
1. Usar funciones de agregación para calcular:
   
    a) [1 punto] conteo de frecuencias o media <br />
    b) [1 punto] mínimo o máximo<br />
    c) [4 puntos] mediana o algún cuantil cuyo resultado sea distinto a la mediana<br />
    d) [4 puntos] moda<br />
    e) [2 puntos] reporta hallazgos, dificultades, implementación de soluciones encontradas en línea, etc.<br />
2. Haz al menos un ejemplo de cada una de las consultados de estadísticos.
3. Escribe un reporte en Markdown o PDF y súbelo a tu repositorio
4. Sube el link de tu tarea a Nexus


## **Respuestas** 
El punto 1. y 2. estan relacionados y se desarrollan a continuación.
~~~
###########################  a) 1.-  Conteo de frecuencias 
SELECT COUNT(DISTINCT categoria) FROM arbol; #65 
SELECT COUNT(DISTINCT descripcion) FROM arbol; #549
SELECT COUNT(DISTINCT codigo) FROM arbol; #532

########################### b) 2.- Media
SELECT AVG(PRECIO) FROM precio; #55792.72553 

########################### c) 3.- 1er cuantil cuyo resultado es distinto a la mediana
SET @row_number=0;
CREATE TABLE test1 
SELECT 
( @row_number :=@row_number +1) As num ,
precio_promedio 
FROM
  producto
ORDER BY precio_promedio ASC  ;

SET @number = round((SELECT count(*) FROM test1 ) * .25);
select * from test1 where num = (round(0.25* @number));
 
select count(*) from test1 ; #41883 
select @number; #0.25 = 10471, 0.75 = 31412

########################### d) 4.- Moda
select * from tienda;
select count(distinct estado) from tienda; #1112
SELECT estado, COUNT(*) AS magnitude 
FROM tienda 
GROUP BY estado 
ORDER BY magnitude DESC
LIMIT 1;
~~~

e) 5.- Reportar hallazgos, dificultades, implementación de soluciones encontradas en línea, etc.<br /><br />
Entre los hallazgos y dificultades que encontre fue que muchas de las soluciones propuestas en páginas web como stackoverflow no las entendí y por ende, cuando las implementaba no me salían correctamente, por lo que empece a plantearlo como lo haría a mi manera de una forma tal vez menos eficiente pero más entendible para mi parecer. 

3. Este punto se ve reflejado en el presente documento.