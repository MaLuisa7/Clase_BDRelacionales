# 0. Se importan las librerias necesarias

import pandas as pd  # manejo de datos
from pymysql import connect  # conectarse a Mysql
from sklearn.model_selection import train_test_split  # conjuntos de train y test para entrenamiento del modelo
from sklearn.ensemble import RandomForestClassifier  #Modelo de ML llamado Random Forest para clasificación
from sklearn import metrics  # para calcular la métrica de evaluación del modelo, exactitud.

# 1. Se realiza conección a Mysql
dbase = connect(                        # Devuelve objeto MySQLConnection si la conexión se estableció correctamente
                host = "localhost",     # nombre del servidor
                user = "root",          # Nombre de usuario que se utiliza para trabajar en mysql, default = root.
                passwd= "MoniFco7",     # Proporcionada por el usuario al momento de instalar el servidor MySQL
                database='ml_dataset')  # BD con la que se quiere trabajar

# 2. Se define el cursor
cur = dbase.cursor()  # Ayuda a realizar varias operaciones SQL.

# 3. Se escribe la consulta a la tabla
consulta = "select * from iris1"

# 4. Se ejecuta la consulta
cur.execute(consulta)  # Se ejecuta la consulta SQL y devuelve el resultado.

# 5. Se leen los datos a través de pandas
data = pd.read_sql(consulta, dbase)  # Necesita 2 args: la consulta y la conexión

data.head()

# 6. Reformato de str a numeric
data['clase'] = data['clase'].replace({'Iris-setos': 0, 'Iris-versi':1, 'Iris-virgi':2})

# 7. Modelo (aquí se pueden hace multiples pasos extras, los que presenté son los básicos)

# 8. Se separa el conjunto de datos en características (X) y la respuesta (y)
X=data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y=data['clase']  # Clase a la que pertenece la muestra

# 9. Se separan las características y la variable respuesta en conjunto de entramiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% entrenamiento and 30% prueba

# 10. Se Llama al objeto que es el modelo de random forest para clasificación
clf = RandomForestClassifier(n_estimators=11)

# 11. Se ajusta / entrena el modelo con las características y variable respuesta de entrenamiento
clf.fit(X_train, y_train)

# 12. Se estiman las variables de respuesta con base en el conjunto de test
y_pred = clf.predict(X_test)

# 13. Se califica el modelo con la exactitud  a ver que tan bien hizo su trabajo (Excelente = 1, Deplorable = 0)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# Se concluye la construcción del modelo con un accuracy o exactitud mayor al 80% , lo cual indica buen desempeño del modelo

# 14. Se realiza inferencia de una muestra de características

# 15. Se consulta la BD, en este caso el último registro de la BD indica el más reciente
consulta2 = " select * from features ORDER BY id DESC LIMIT 1;"

# 16. Se ejecuta la consulta
cur.execute(consulta2)

# 17. Se leen los datos a través de pandas
sample = pd.read_sql(consulta2, dbase)
sample

# 18. Se le da formato a los datos para que el modelo realice estimación
values = sample.values[0][1:]
features = values.reshape(1, -1)

# 19. Estimación del modelo
prediction = clf.predict( features )

# 20. Se reestructuran los datos para que sea fácil colocarlos en la consulta siguiente.
output = list(values) + list(prediction)
print(output)

# 21. Se realiza consulta para insertar las características y la estimación en la BD de output.
consulta3 = "INSERT INTO output (sepal_length, sepal_width, petal_length, petal_width, prediction) VALUES" +"(" + str(output[0])+ ','+ str(output[1])+  ','+   str(output[2])+   ','+  str(output[3]) +  ','+ str(output[4]) + ")"

# 22. Se ejecuta la consulta
cur.execute(consulta3)

# 23. Se confirma que la transacción fue exitosa
dbase.commit()
print(cur.rowcount, "Record inserted successfully into output table")

# 24. No olvides cerrar la conexión para que el programa de MySql pueda realizar otras tareas correctamente.
dbase.close()
print("MySQL connection is closed")