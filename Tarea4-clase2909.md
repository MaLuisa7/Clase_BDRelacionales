# *Tarea 4  de la clase correspondiente al día 29 de Septiembre de 2022*

**Universidad Autónoma de Nuevo León**

**Facultad de Físico Matemáticas**

**Maestría en Ciencia de Datos**

**Hecha por Ma. Luisa Argáez Salcido**

**Correo Universitario: maria.argaezs@uanl.edu.mx**

**Matricula 2173261**


## **Instrucciones**
1. [4 puntos] Crea tu base de datos y tablas correspondientes a partir de tus tareas de los modelos e-r y relacional
2. [4 puntos] Incluye al menos 20 registros en tu base de datos
3. Sube tu archivo de creación de base de datos a tu repositorio con un nombre claro
4. [2 puntos] Tu archivo se ejecuta completamente y sin ningún error en su SGBD correspondiente durante la siguiente sesión en vivo

## **Respuestas**

1. 
```

-- crear tabla employee

CREATE TABLE employees(
    emp_no INT  PRIMARY KEY ,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender Enum('M','F') NOT NULL,
    birth_date DATE NOT NULL,
    hire_date DATE NOT NULL
);

-- crear tabla departments
CREATE TABLE departments(
    dept_no VARCHAR(4) PRIMARY KEY NOT NULL,
    dept_name VARCHAR(50) UNIQUE KEY NOT NULL
);

-- crear tabla TITLE
CREATE TABLE titles(
    emp_no INT  NOT NULL REFERENCES employees (emp_no) ,
  	title VARCHAR(50)  NOT NULL,
    from_date DATE NOT NULL,
    to_date DATE ,
  	PRIMARY KEY (emp_no,title, from_date)       
);


CREATE TABLE dept_manager(
    emp_no INT REFERENCES employees (emp_no),
    dept_no VARCHAR(4) REFERENCES departments(dept_no),
    from_date DATE NOT NULL,
    to_date DATE NOT NULL  ,
  	PRIMARY KEY(emp_no, dept_no)
  );
  
  CREATE TABLE dept_emp(
    emp_no INT NOT NULL REFERENCES employees (emp_no) ,
    dept_no VARCHAR(4) NOT NULL REFERENCES departments (dept_no),
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
    PRIMARY KEY(emp_no, dept_no)
  );
  
  CREATE TABLE salaries(
    emp_no INT  not NULL REFERENCES employees (emp_no),
    salary INT not NULL,
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
    PRIMARY KEY (emp_no, from_date)
  );
  
```

2. 
```
INSERT into employees (emp_no,first_name,last_name,gender,birth_date,hire_date) values
(1,'maria','argaez', 'F', '1995-08-07', '2021-09-12'),
(2,'luisa','salcido', 'F', '1990-06-14', '2021-05-14'),
(3,'monica','marquez', 'F', '1991-10-07', '2020-09-25'),
(4,'guadalupe','rodriguez', 'F', '1996-06-07', '2012-01-30'),
(5,'concepcion','perez', 'F', '1999-02-07', '2014-03-02'),
(6,'marva','sanchez', 'F', '1990-09-07', '2003-06-16'),
(7,'elia','contreras', 'F', '1986-10-07', '2015-05-25'),
(8,'marigel','dominguez', 'F', '1960-11-07', '2016-04-27'),
(9,'leonor','burrola', 'F', '1987-10-08', '2000-05-15'),
(10,'silvia','hernandez', 'F', '1976-11-09', '2011-04-17'),
(11,'augusto','argaez', 'M', '1995-08-07', '2021-08-12'),
(12,'francisco','salcido', 'M', '1990-09-14', '2022-06-14'),
(13,'carlos','marquez', 'M', '1991-12-07', '2021-07-25'),
(14,'jose','rodriguez', 'M', '1996-07-07', '2011-07-30'),
(15,'miguel','perez', 'M', '1999-08-07', '2013-06-02'),
(16,'luis','sanchez', 'M', '1990-02-07', '2004-06-16'),
(17,'david','contreras', 'M', '1986-12-07', '2016-02-25'),
(18,'diego','dominguez', 'M', '1960-10-07', '2017-02-27'),
(19,'ivan','burrola', 'M', '1987-12-08', '2001-09-15'),
(20,'tomas','hernandez', 'M', '1976-11-09', '2011-12-17')
;

INSERT into departments (dept_no,dept_name) values
('mkt', 'marketing'),
('fin', 'finanzas'),
('cia', 'centro de investigacion aplicada'),
('sale', 'ventas'),
('rh','recursos humanos')
;
```