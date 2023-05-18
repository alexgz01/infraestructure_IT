# Descripción.

Mediante esta práctica haremos lecturas de estudios científicos, mediante un 'corpus.txt' que se nos proporciona con distintos dois. Dichos dois tras un preprocesado de los mismos haremos distintas consultas para obtener información de éstos.

-----------------------------------------------------------------------

## Contenido en el repositorio.
-----------------------------------------------------------------------

1. Archivos:

Encontramos distintos archivos:

- Los que se encuentran en carpetas es de un ejemplo realizado con el 'corpus.txt' que se encuentra en el repositorio *publications*.
- Los ficheros '.ipynb' son los que hay que ejecutar para realizar la tarea propuesta.

2. Docker:

Encontramos un Dockerfile necesario para que funcione nuestra infraestructura.

3. Readme.md:

Es la descripción del trabajo.

4. LICENSE:

Licencia del repositorio en github.

5. Repository.md:

Contiene la ruta al repositorio.

-----------------------------------------------------------------------

## Instrucciones preparación infraestructura.
-----------------------------------------------------------------------

1. Clonamos el repositorio github en nuestro ordenador:

```shell
$ git clone 'https://github.com/alexgz01/infraestructure_IT.git'
```

2. Nos dirigimos a la carpeta donde se sitúa el Dockerfile:

```shell
$ cd .\infraestructure_IT\Docker\
```

3. Creamos la imagen mediante el Dockerfile:

```shell
$ docker build -t neo4j-image .
```

4. Levantamos un contenedor con la imagen:

```shell
$ docker run -d -p 7474:7474 -p 7687:7687 --name neo4j-container neo4j-image
```

-----------------------------------------------------------------------

## Archivos
-----------------------------------------------------------------------

Encontramos 3 carpetas: 

- En publications hay que poner el 'corpus.txt' del cual queremos extraer los dois.
- En csvs se guardan los '.csv' que hemos generado, en este caso solo se generarán 3, 'authors.csv', 'documents.csv' y 'general.csv'.
- En dynamicdata estaría guardada el 'Keywords.csv'.

También econtramos distintos python notebooks, los explicaremos en orden de uso:

- parser.ipynb: Su funcionalidad es coger el 'corpus.txt' y convertirlo a los '.csv' mencionados.
- wordCount.ipynb: Su funcionalidad es mediante el 'general.csv' generar el 'Keyword.csv' que según x palabras que le escribas devuelve la palabra y cuantas veces sale en el abstract.
- articles.ipynb: Devuelve un listado ordenado de artículos en los que un autor específico ha participado. La relevancia viene determinada por el número de autores (menor número de autores, mayor relevancia del autor concreto).
- texts.ipynb: Devuelve un listado ordenado de párrafos, junto con el título del artículo al que pertenecen, que contienen un término específico. La relevancia viene determinada por el tamaño del párrafo y la frecuencia del término.
- collaborators.ipynb: Devuelve un listado ordenado de autores relacionados con un autor específico. La relación entre autores viene determinada por su colaboración directa en un artículo o indirecta a través de autores comunes.
- word.ipynb: Devuelve el número de palabras en el corpus cuya longitud es de un tamaño específico.
■ Palabras con sólo una letra, o con dos letras, o con tres letras…hasta 20 letras.














