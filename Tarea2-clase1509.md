# *Tarea 2  de la clase correspondiente al día 15 de Septiembre de 2022*

**Universidad Autónoma de Nuevo León**

**Facultad de Físico Matemáticas**

**Maestría en Ciencia de Datos**

**Hecha por Ma. Luisa Argáez Salcido**

**Correo Universitario: maria.argaezs@uanl.edu.mx**

**Matricula 2173261**



## **Instrucciones**

1. [8 puntos] Convierte tu base de datos no estructurada en un modelo entidad-relación, representándolo con un diagrama entidad-relación. Usa nodos con figuras correctas y aristas claramente señaladas con los números correspondientes para las relaciones.
2. [2 punto] Muestra el dominio de los atributos.
3. Subir esta descripción en un archivo markdown o PDF nombrado claramente (tarea 1 o algo por el estilo).



## **Respuestas**

1. "Diagrama de entidades de la BD de Employees"
   </br>
   <img src="entitydiagramemployees.png" alt="Diagrama de entidades de la BD de Employees" />
   </br>
   No encontre el elipse con doble raya, asi que se intercambio por un círculo.

    *Mermaid code* 
    ~~~
    flowchart TD;

    E[Employees]--- E1(((emp_no)));
    E[Employees]--- E2([birth_date]);
    E[Employees]--- E3([first_name]);
    E[Employees]--- E4([last_name]);
    E[Employees]--- E5([gender]);
    E[Employees]--- E6([hire_date]);

    E[Employees]--- |1|J{tiene};
    J{tiene} ---> |N| F[Salaries];

    F[Salaries]---F1([emp_no]);
    F[Salaries]---F2([salary]);
    F[Salaries]---F3(((from_date)));
    F[Salaries]---F4([to_date]);

    E[Employees]--- |1|K{tiene};
    K{tiene} ---> |N| G[Titles];

    G[Titles]---G1([emp_no]);
    G[Titles]---G2(((title)));
    G[Titles]---G3(((from_date)));
    G[Titles]---G4([to_date]);


    E[Employees]--- |1|H{tiene};
    H{tiene} ---> |N| C[dept_emp];

    C[dept_emp]---C1([emp_no]);
    C[dept_emp]---C2([dept_no]);
    C[dept_emp]---C3([from_date]);
    C[dept_emp]---C4([to_date]);

    E[Employees]--- |1|L{tiene};
    L{tiene} ---> |N| D[dept_manager];

    B[Departments]--- |1|N{tiene};
    N{tiene} ---> |N| D[dept_manager];

    D[dept_manager]---D1([dept_no]);
    D[dept_manager]---D2([emp_no]);
    D[dept_manager]---D3([from_date]);
    D[dept_manager]---D4([to_date]);

    B[Departments]--- B1(((dept_no)));
    B[Departments]--- B2([dept_name]);

    C[dept_emp]--- |N|I{tiene};
    I{tiene} ---> |1| B[Departments] ;

    ;
    ~~~
    [Código mermaid live](https://mermaid.live/edit#pako:eNqNlFtv4jAQhf9K5KcgAcp9Qyr1oQ29bLu8tE_rVMhLHIgUO5Ex2mUJ_30noSTktgUJiRl_PppzbHxAqzSkyENRkv5ebYiQyrt_E_CAK_CZ4znLknRP6fZjMpkoc11VVcqyJU9Ho9HNAGSo-Fcs5GYZEkk_BjFTxVEstnLJCfsPZqk4IV9StorXlIdUDCOOijexoPVU_Vyu598PMqacHj-VzqUCy7dKvsiVB_xGEiJi2FLpXPSAe9BVfAqqGqgFQErbot4PASZkHYmUlQPXcbcoiEemV3h6aXp66Xh6xO-xTC4dVR1gHrt-GssGDCuLsh60sT5gpsF0rAyaeWqaeeqYucchzeQSJq7tXPSAu-8aagFwQGU9TBQ3-OxpiLn2fF6bll47lvyTLiOcrOGaV1p32KcZ_G8Z5bJSWzTVFlertfrA-3o3hx7K6MTZA_UG1sP1htY1elc8R5-z1Xeqh6uO8vyG9B1VkctzM7fnZm563hJXKqlyAxojRgUjcQgP6qHoBEhuKKMB8uBnSCOyS2SAAn4ElOxk-rbnK-RJsaNjtMsKw35M1oIw5EUk2UKXhrFMxY_TI12-1WOUEf4zTdl5I5TIO6A_yNMdfepajjszdEuzLVMzxmiPPNeazgxXMzXXcYqvdRyjv6WANv1mOrZl25qpmzNrZrvHf_EN6vo)



2. El dominio de los atributos se detalla a continuación en el siguiente listado de las entidades:
    </br></br>
    $Departments$

    |Atributo|Dominio|
    | --- | --- |
    |dept_no (primary_key)|1|
    |dept_name (unique_key)|Ventas|

    </br>

    $Employees$
    |Atributo|Dominio|
    | --- | --- |
    |emp_no|1,2,3,...,n|
    |birth_date|1995-08-07|
    |first_name|Maria|
    |last_name|Argáez|
    |gender|F / M |
    |hire_date|2020-03-17|

    </br>

    $Dept$_$emp$
    |Atributo|Dominio|
    | --- | --- |
    |emp_no|1,2,3,...,n|
    |dept_no|1,2,3,...,n|
    |from_date|2020-03-17|
    |to_date|2022-09-12|

    </br>

    $Dept$_$manager$ 
    |Atributo|Dominio|
    | --- | --- |
    |emp_no|1,2,3,...,n|
    |dept_no|1,2,3,...,n|
    |from_date|2020-03-17|
    |to_date|2022-09-12|

    </br>

    $Title$ 
    |Atributo|Dominio|
    | --- | --- |
    |emp_no|1,2,3,...,n|
    |title|Data Scientist|
    |from_date|2020-03-17|
    |to_date|2022-09-12|

    </br>
    
    $Salaries$
    |Atributo|Dominio|
    | --- | --- |
    |emp_no|1,2,3,...,n|
    |Salary|200 000|
    |from_date|2020-03-17|
    |to_date|2022-09-12|



3. Mi repositorio esta en el siguiente link: [Repositorio Maria Luisa](https://github.com/MaLuisa7/Clase_BDRelacionales.git  "Repositorio Maria Luisa") con el nombre de "Tarea2-clase1509"

<!---
Para ver el pdf
ctrl+shift+v


Para git 
git status
git add .
git commit -m "Cambios en redaccion 3 "
git push origin main
-->