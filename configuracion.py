from os import listdir
from os.path import isfile, join
import psycopg2
import pandas as pd


#Ubicación donde se alojan los datasets
DATASETS= 'Datasets/'

#Ubicación donde se reubicaran los datasets una vez cargados a las base de datos
DATASET_DESTINO= 'Datasets_cargados'

#Ubicación donde estan los datasets normalizados
DATASET_NORMALIZADO= 'Datasets_normalizados'

#Lista con los nombres de los datasets (no modificar)
ARCHIVOS = [f for f in listdir(DATASETS) if isfile(join(DATASETS, f))]

#Configuración de los datasets:
__CONFIG_GENERAL = {
                   'sep':',',
                   'encoding':'utf-8'
                  }

__CONFIG_OECSOURCE = {
                     'sep':';',
                     'encoding':'utf-8'
                    }

__CONFIG_PROVEEDORES = {
                      'sep':',',
                      'encoding':'latin1'
                     }
                   
#No modificar
CONFIG_DATASETS = {
                    'energyco':__CONFIG_GENERAL,
                    'global_power_plant_database':__CONFIG_GENERAL,
                    'owid-energy-consumption-source':__CONFIG_OECSOURCE,
                    'Access-to-clean-fuels-and-technologies-for-cooking':__CONFIG_GENERAL,
                    'carbon-intensity-electricity':__CONFIG_GENERAL,
                    'elec-mix-bar':__CONFIG_GENERAL,
                    'electricity-prod-source-stacked':__CONFIG_GENERAL,
                    'global-energy-substitution':__CONFIG_GENERAL,
                    'low-carbon-share-energy':__CONFIG_GENERAL,
                    'modern-renewable-energy-consumption':__CONFIG_GENERAL,
                    'per-capita-energy-use':__CONFIG_GENERAL,
                    'primary-energy-source-bar':__CONFIG_GENERAL,
                    'share-elec-by-source':__CONFIG_GENERAL,
                    'share-of-the-population-with-access-to-electricity':__CONFIG_GENERAL,
                    'Entidades':__CONFIG_OECSOURCE,
                    
                  }


#Información de la Base de Datos:

'''__DATABASE_INFO =  psycopg2.connect(user = "postgres",
                                    password = "postgres",
                                    host = "localhost",
                                    port = "5432",
                                    database = "ProyectoGrupal")'''


try:
    connection = psycopg2.connect(user = "postgres",
                                    password = "postgres",
                                    host = "localhost",
                                    port = "5432",
                                    database = "ProyectoGrupal")

    
    # Print PostgreSQL Connection properties
    #print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cur = connection.cursor()
    #cur.execute("select * from ciudades")
    records = cur.fetchall() 
 
    for row in records:
        print(row)
 
except (Exception, psycopg2.Error) as error :
    print ("Error", error)

#conexion a aws 
'''conn = redshift_connector.connect(
     host='examplecluster.abc123xyz789.us-west-1.redshift.amazonaws.com',
     database='dev',
     user='awsuser',
     password='my_password'
  )'''
                  

#Configuración para conectar con la base de datos (No modificar)
DATABASE_CONFIG = f'postgresql://postgres:postgres@localhost:5432/ProyectoGrupal'


