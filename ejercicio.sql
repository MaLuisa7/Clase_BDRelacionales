-- CREATE DATABASE ML_dataset;
USE ML_dataset;

-- Se necesitan 3 BD:
-- 1.- BD dónde se insertará el Histórico / matriz de entrenamiento / experiencia cuantificable
-- 2.- BD con características (Donde se registran)
-- 3.- BD dónde se guardarán las características con el valor estimado

/*1.- Crear tabla tabla1 donde se guardara el histórico*/
CREATE TABLE iris(
	sepal_length float,
    sepal_width float,
    petal_length float,
    petal_width float,
    clase varchar(10)
);

/* Desde la consola inserto los datos para que sea más ágil */ 
-- mysql --local-infile=1 -u root -p 
-- USE ml_dataset; 
-- mysql> LOAD DATA LOCAL INFILE "C:/Users/Maria Luisa/OneDrive/Documentos/MasterDataScience/BDRelacionales/pia/iris.txt"
--    -> INTO TABLE iris
--    -> FIELDS TERMINATED BY ','
--    -> LINES TERMINATED BY '\n'
--   -> (sepal_length, sepal_width, petal_length, petal_width, clase);

SELECT * FROM iris; #SON 151 , POR QUE TOMO EL ULTIMO ESPACIO EN BLANCO

# SELECCIONO AQUELLOS CAMPOS QUE NO SON NULOS 
CREATE TABLE iris1(
SELECT   *  FROM   iris
WHERE  sepal_width IS NOT NULL );

SELECT COUNT(*) FROM iris1;
 
/*2.- Crear tabla se registran las características */
 CREATE TABLE features(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	sepal_length float,
    sepal_width float,
    petal_length float,
    petal_width float
);
-- Insertaré dato
 INSERT INTO features (sepal_length,sepal_width,petal_length,petal_width) VALUES (6.2, 3.4, 5.4, 2.3);
 SELECT * FROM features;
 
 /* 3.- Crear tabla output donde se guardaran las características y la predicción*/
 CREATE TABLE output(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	sepal_length float,
    sepal_width float,
    petal_length float,
    petal_width float,
    prediction float
);
select * FROM output;
