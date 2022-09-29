# *Tarea 3  de la clase correspondiente al día 22 de Septiembre de 2022*

**Universidad Autónoma de Nuevo León**

**Facultad de Físico Matemáticas**

**Maestría en Ciencia de Datos**

**Hecha por Ma. Luisa Argáez Salcido**

**Correo Universitario: maria.argaezs@uanl.edu.mx**

**Matricula 2173261**


## **Instrucciones**

1. [3 puntos] Crea un esquema del modelo relacional de tu base de datos a partir del modelo e-r de la tarea anterior.
2. [3 puntos] Representa con un diagrama relacional tu esquema del punto anterior.
3. [4 puntos] Encuentra cuatro operaciones que vayas a usar en tu base de datos y exprésalas mediante operadores del álgebra relacional. Explica con tus propias palabras cada una de estas operaciones.

* Reporta tu tarea de una manera claramente identificable en el repositorio. Sube la evidencia a Nexus.

## **Respuestas**

1. 

Employees (_id-emp-no_, birth_date, first_name, last_name, gender, hire_date )

departments (_id-dept-no_, dept_name )

titles (_id-title_, _id-from-date_,  to_date, id-emp-no ) 

dept_manager (from_date, to_date, id-emp-no, id-dept-no )

dept_emp (from_date, to_date, id-emp-no, id-dept-no )

salaries (_id-from-date_, salary, to_date, id-dept-no )


2.

[![](https://mermaid.ink/img/pako:eNq1VE2PgkAM_SukZzSoA7ic97qnvW1MSFeKTsLMmKEmuuh_3xFQET_W3WThwvS9tq_t0ArmJiNIgOyrxIVFNdMz7bmH1KowW6LS2-0Gg13lseSCvGQG7r3NyGjFqUKNC7JdYuPZJTnXLsHZ0LIizeVfaDdSXthbbokFWunktryrSqvmXNs0kzWezA4aUm3OSE7zJXqf0vIyzZDpjDBt2Hi5tCWnGtUVUuAdYEE6I9tPsZSWOhn2R7lNN6t-ECe1RvphnD23RvW0Nhibnrlfdpobi5rwmPskojOKW0rq9ne71iCN-dSBbrR62NVjJdRIuZftLPayyufKvxTTXp3qmdb8s57jtf2Vlkezb73ruNufNYAPiqxCmbk1UYuYAS_JDRES95lRjuuCDz_U3lFxzeZ9q-eQsF2TD-vVIVy7WyDJsSidlTLJxr41q6feQD6sUH8Yo46O7ghJBRtIRnE8DEIRiJcwiKJpICIftpAIMRzHcRSGURyMxEhM9j581QGC4TQUk5eJGI-jYBIF8Xj_DbPSjpo)](https://mermaid.live/edit#pako:eNq1VE2PgkAM_SukZzSoA7ic97qnvW1MSFeKTsLMmKEmuuh_3xFQET_W3WThwvS9tq_t0ArmJiNIgOyrxIVFNdMz7bmH1KowW6LS2-0Gg13lseSCvGQG7r3NyGjFqUKNC7JdYuPZJTnXLsHZ0LIizeVfaDdSXthbbokFWunktryrSqvmXNs0kzWezA4aUm3OSE7zJXqf0vIyzZDpjDBt2Hi5tCWnGtUVUuAdYEE6I9tPsZSWOhn2R7lNN6t-ECe1RvphnD23RvW0Nhibnrlfdpobi5rwmPskojOKW0rq9ne71iCN-dSBbrR62NVjJdRIuZftLPayyufKvxTTXp3qmdb8s57jtf2Vlkezb73ruNufNYAPiqxCmbk1UYuYAS_JDRES95lRjuuCDz_U3lFxzeZ9q-eQsF2TD-vVIVy7WyDJsSidlTLJxr41q6feQD6sUH8Yo46O7ghJBRtIRnE8DEIRiJcwiKJpICIftpAIMRzHcRSGURyMxEhM9j581QGC4TQUk5eJGI-jYBIF8Xj_DbPSjpo)


3.

**a)** ¿Cuáles empleados son hombres y cuáles son mujeres ? 

$\sigma_{gender == F}(employees)$
</br>
$\sigma_{gender == M}(employees)$
  
**b)** ¿Cuáles empleados ganan más de 50 000 al mes?

$\sigma_{salary>50000}(salaries)$

  
**c)** ¿Cuáles empleados son managers?

$\Pi_{id-emp-no}(Employes) \cap \Pi_{id-emp-no}(dept_manager)$
  
**d)** ¿Cuántos departamentos hay?

$\Pi_{id-dept-no}(departments)$




<!---
Para ver el pdf
ctrl+shift+v


Para git 
git status
git add .
git commit -m "Cambios en redaccion 3 "
git push origin main
-->