from typing import Union
from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="API Plaformas de Series y Películas", description="PI 01 DTS-05 Daniel Vallejos")

#cargo los archivos csv con los datos datos

#titles_todos.csv contiene los datos de las 4 plataformas
df_titles = pd.read_csv('./Datasets/titles_todos.csv')

#plataform_title_cast contiene los datos: platafroma, titulo, actor (individual)
df_cast_title = pd.read_csv('./Datasets/plataform_title_cast.csv')

#plataform_title_gender contiene los datos: platafroma, titulo, genero (individual)
df_gender_title = pd.read_csv('./Datasets/plataform_title_gender.csv')

@app.get("/")
async def read_root():
    return {"PI01": "Funcionando ..."}

#Máxima duración según tipo de film (película/serie), por plataforma y por año
@app.get("/get_max_duration/")
async def get_max_duration( year: int, plataform: str, type: str):

    #verifico el tipo, si es minutos o capítulos para filtrar adecuadamente
    if type.lower() == 'min':
        type_f = 'Movie'
    elif type.lower() == 'season':
        type_f = 'TV Show'
    else:
        type_f = ''

    #reliza el fitro con los parámetros de la query
    df_filtro = df_titles[(df_titles.release_year == year) & (df_titles.plataform == plataform) & (df_titles.type == type_f)]
    
    #si encontró resultados con los parámetros determina el título com mayor duración y retorna ese valor
    if df_filtro.shape[0] > 0:

        max_duration = df_filtro.duration_val.max()

        title = df_titles[(df_titles.release_year == year) & (df_titles.plataform == plataform) & (df_titles.type == type_f) & (df_titles.duration_val == max_duration)].title.values[0]

        retorno = {'title': title }

    else:

        retorno = {'title': 'Data not found' }

    return retorno


#Cantidad de películas y series (separado) por plataforma
@app.get("/get_count_plataform/")
async def get_count_plataform( plataform: str ):

    #realiza el filtro por la plataforma pasada por parámetro y contando por tipo
    df_plataform_count = df_titles[(df_titles.plataform == plataform.lower() )].type.value_counts()

    #si encontró valores ... retorna los resultados
    if df_plataform_count.shape[0] > 0:
        
        retorno = {'plataform': plataform }
        retorno.update(df_plataform_count.to_dict())

    else:
        retorno = {
            'plataform': 'Data not found'
        }
    return retorno

#Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo
@app.get("/get_listedin/")
async def get_listedin( gender: str ):

    #realiza el fitro por el género desde el dataframe que contiene plataforma, título y género
    df_1 = df_gender_title[( df_gender_title['gender'].str.lower() == gender.lower() )].plataform.value_counts().sort_values(ascending=False)

    #si encontro resultado, retorna los valores
    if df_1.shape[0] > 0:
        df_2 = df_1.to_dict()

        retorno = { 
            'plataform': df_1.index[0],
            'count': df_2[df_1.index[0]]
        }
    else:
        retorno = { 
            'plataform': 'Data not found',
            'count': 'n/a'
        }

    return retorno


#Actor que más se repite según plataforma y año
@app.get("/get_actor/")
async def get_actor( plataform: str, year: int ):

    #realiza el fitro por con la plataforma y año pasados por parámetro desde el dataframe que contiene plataforma, título y actor
    df_2 = df_cast_title[(df_cast_title.plataform == plataform.lower()) & (df_cast_title.year == year)].groupby(['cast']).count().sort_values(by=['title'],ascending=False)
    
    #si encontro resultado, retorna los valores
    if df_2.shape[0] > 0:
        retorno = {
            'plataform': plataform.lower(),
            'count': df_2.head(1)['year'].to_dict()[df_2.head(1).index[0]],
            'actor': df_2.head(1).index[0]
        }
    else:
        retorno = {
            'plataform': 'Data not found',
            'count': 'n/a',
            'actor': 'n/a'
        }
    return retorno
