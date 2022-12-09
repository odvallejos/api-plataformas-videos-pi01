# <p align=center>**Proyecto Individual Nº1**</p>
## <p align=center>**Daniel Vallejos**</p>

## <p align=center>Data Engineering</p>


<p align="center">
<img src="https://files.realpython.com/media/What-is-Data-Engineering_Watermarked.607e761a3c0e.jpg"  height=300>
</p>

## **Propuesta de trabajo**

El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API deberán construirla en un entorno virtual dockerizado.

Los datos serán provistos en archivos de diferentes extensiones, como *csv* o *json*. Se espera que realicen un EDA para cada dataset y corrijan los tipos de datos, valores nulos y duplicados, entre otras tareas. Posteriormente, tendrán que relacionar los datasets así pueden acceder a su información por medio de consultas a la API.

Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:<br/>
    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma<br/>
    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.<br/>
    El request debe ser: get_listedin('genero')

+ Actor que más se repite según plataforma y año.<br/>
  El request debe ser: get_actor(plataforma, año)

<hr> 

## **Pasos del proyecto realizados**

### **1. Ingesta y normalización de datos**

+ Se proveyeron 4 archivos con información de Títulos de plataformas de streaming de video: Amazon Prime, Netflix, Disney Plus y Hulu.

+ 3 de estos archivos estaban en formato csv y 1 en formato json.

+ Todos contaban con la misma estructura de datos.

+ Se procedió a realizar el análisis exploratorio de los datos.

+ No se encontraron titulos duplicados en la misma plataforma.

+ Se agregó una columna a cada dataframe con el dato de la plataforma: amazon, netflix, disney, hulu.

+ Se unificaron los 4 dataframes en uno solo que concentra toda la información y podemos identificar a qué plataforma pertenece con la columna recientemente mencionada.

+ Para la consigna de obtener la ***Máxima duración según tipo de film (película/serie), por plataforma y por año***, el campo *duration* almacena la información en formato de unidades y descripción, por ejemplo: *113 min* ó *7 Seasons*, para poder cumplir con la consigna se creó una nueva columna de tipo integer con el valor correspondiente sobre el cual se puede realizar operaciones y responder a la solicitud de la consigna.

+ Se reemplazaron los valores nulos con string vacíos ('')

+ Para resolver la consigna de: ***Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo***, se observó que la columna *listed_in* guarda los géneros, por ejemplo: *"Comedy, Drama"*, para resolver de mejor manera el requerimiento, se creó un nuevo archivo de datos con la estructura: plataforma, título, género.

+ Para resolver la consigna de: ***Actor que más se repite según plataforma y año***, se observó que la columna *cast* guarda los actores, por ejemplo: *"David Tennant, Lucy Punch, Faye Marsay, Gemma Jones"*, para resolver de mejor manera el requerimiento, se creó un nuevo archivo de datos con la estructura: plataforma, título, actor.

<hr> 

### **2. Creación de la API utilizando FastAPI y Uvicorn**

Se creó la API que responde a la consigna solicitada utilizando FastAPI

+ get_max_duration(year, plataform, type)<br/>
    *year*: parámetro de tipo entero de 4 dígitos, por ejemplo: 2018<br/>
    *plataform*: parámetro de tipo string, valores posibles: amazon, netflix, disney, hulu<br/>
    *type*: parámetro de tipo string, valores posibles: min, season

+ get_count_plataform(plataform)<br/>
    *plataform*: parámetro de tipo string, valores posibles: amazon, netflix, disney, hulu<br/>
  
+ get_listedin(gender)<br/>
    *gender*: parámetro de tipo string

+ get_actor(plataform, year)<br/>
    *plataform*: parámetro de tipo string, valores posibles: amazon, netflix, disney, hulu<br/>
    *year*: parámetro de tipo entero de 4 dígitos, por ejemplo: 2018

<hr> 

### **3. Entorno Docker**

Se creó el entorno docker con la estructura y los archivos necesarios.

Se ejecutó la API desde le entorno local con docker puerto 80

<hr> 

### **4. Video demostrativo**

Aquí el video donde se muestra el trabajo realizado y en funcionamiento.

<hr> 

### **5. Deployment en Mogenius**

Se procedió al deployment en la plataforma Mogenius:


