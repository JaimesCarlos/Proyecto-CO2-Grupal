
import numpy as np
import pandas as pd
import os
import __main__
def Year(data,anio,year):
    dr=data.loc[:,['name',anio]]
    dr['year']=year
    dr.rename({anio:'generation_gwh'},axis=1,inplace=True)
    return dr

def generation_gwh():
    data = pd.read_csv('.\Datasets\global_power_plant_database.csv',delimiter = ',',decimal =".", encoding="UTF-8")
    d2013=Year(data,'generation_gwh_2013',2013)
    d2014=Year(data,'generation_gwh_2014',2014)
    d2015=Year(data,'generation_gwh_2015',2015)
    d2016=Year(data,'generation_gwh_2016',2016)
    d2017=Year(data,'generation_gwh_2017',2017)
    d2018=Year(data,'generation_gwh_2018',2018)
    d2019=Year(data,'generation_gwh_2019',2019)
    generation_gwh=pd.concat([d2013, d2014,d2016,d2017,d2018,d2019,d2015], ignore_index=True)
    return generation_gwh


def detectar_outliers(df:pd.DataFrame,columna:str,name:str,tecnica='cajas') -> pd.DataFrame:

    #Detección por medio de Diagrama de Cajas:
    if tecnica == 'cajas':
        q1 = df[columna].describe().loc['25%']
        q3 = df[columna].describe().loc['75%']
        rango_IC = q3 - q1
        minimo = q1 - ((1.5) * (rango_IC))
        maximo = q3 + ((1.5) * (rango_IC))


    #Detección de outliers por medio de las 3 sigmas:
    elif tecnica == 'sigmas':
        promedio = df[columna].mean()
        stddev = df[columna].std()
        maximo = promedio + (3 * stddev)
        minimo = promedio - (3 * stddev)

    df[name] = 1

    df[name][(df[columna] > maximo) | (df[columna] < minimo)] = 0
    #df['Outlier'][(df[columna] > maximo) | (df[columna] < minimo)] = 0
    #para llamar la funcion es necesario enviarle esta estructura
    #Dataframe= detectar_outliers(Dataframe,'Columna_a validar outlier','nombre_de_nueva_columna_Outlier_CO2_emission')
    return df


def transformar_entidades(path:str,sep:str,encoding:str) -> pd.DataFrame:

    try:
        df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)
    except(ValueError):
        df = pd.read_csv(f'Datasets/{path}',sep=';',encoding=encoding)
    
    df.fillna({'Code': 'Sin Informacion'}, inplace=True)
    df.fillna(0, inplace=True)
   
    df= df.drop_duplicates()
    #Entity = Entity.fillna('SIN INFORMACION')
    return df

def transformar_energyco2(path:str,sep:str,encoding:str,d:dict,f:dict) -> pd.DataFrame:
    
    try:
        df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)
    except(ValueError):
        df = pd.read_csv(f'Datasets/{path}',sep=';',encoding=encoding)
    df.rename(columns={'Unnamed: 0':'Id_Energyco2','Code': 'Sin Informacion'}, inplace=True)
    df.fillna(0, inplace=True)
    #df= detectar_outliers(df,'CO2_emission','Outlier_CO2_emission')
    #df= detectar_outliers(df,'Energy_consumption','Outlier_Energy_consumption')
    #df= detectar_outliers(df,'Energy_production','Outlier_Energy_production')
    df['Country'] = df.Country.map(d)
    df['Country'] = df.Country.map(f)
    df.rename(columns={'Country':'Id_Entity'}, inplace=True)
    return df


def transformar_GPPD(path:str,sep:str,encoding:str,d:dict,f:dict) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)
    df['country_long'] = df.country_long.map(d)
    df['country_long'] = df.country_long.map(f)
    df.rename(columns={'country_long':'Id_Entity'}, inplace=True)

  
    df.rename(columns={'country_long':'Id_Entity'}, inplace=True)
    tabla_general=df.loc[:,['Id_Entity','country','name','capacity_mw','primary_fuel']]
    tabla_general=tabla_general.reset_index()
    tabla_general.rename({'index':'Id_planta','country':'Code'},axis=1,inplace=True)

    return tabla_general




def transformar_ATCFATFC(path:str,sep:str,encoding:str,d:dict,f:dict) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)
    df = df.reset_index()
    df.rename(columns={'index':'Id_Access-to-clean-fuels-and-technologies','Indicator:Proportion of population with primary reliance on clean fuels and technologies for cooking (%) - Residence Area Type:Total':'Indicador%'}, inplace=True)
    df.fillna({'Code': 'Sin Informacion'}, inplace=True)
    #df= detectar_outliers(df,'Indicador%','Outlier_Indicador%')
    df['Entity'] = df.Entity.map(d)
    df['Entity'] = df.Entity.map(f)
    df.fillna(0, inplace=True)
    df.rename(columns={'Entity':'Id_Entity'}, inplace=True)
    df = df.astype({"Id_Entity": np.dtype("int64")})
    return df


def transformar_CIE(path:str,sep:str,encoding:str,d:dict,f:dict) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)
    df = df.reset_index()
    df.rename(columns={'index':'Id_carbon-intensity-electricity','Carbon intensity of electricity (gCO2/kWh)':'Id_CarbonIntensityofElectricity(gCO2/kWh)'}, inplace=True)
    df.fillna({'Code': 'Sin Informacion'}, inplace=True)
    #df= detectar_outliers(df,'Id_CarbonIntensityofElectricity(gCO2/kWh)','Outlier_Carbon_(gCO2/kWh)')
    df['Entity'] = df.Entity.map(d)
    df['Entity'] = df.Entity.map(f)
    df.rename(columns={'Entity':'Id_Entity'}, inplace=True)
    return df


def transformar_EMB(path:str,sep:str,encoding:str,d:dict,f:dict) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df = df.reset_index()
    df.rename(columns={'index':'Id_elec-mix-bar','Electricity from fossil fuels (TWh)':'ElectricityFromFossilFuels(TWh)','Electricity from nuclear (TWh)':'ElectricityFromNuclear(TWh)','Electricity from renewables (TWh)':'ElectricityFromRenewables(TWh)'}, inplace=True)
    df.fillna({'Code': 'Sin Informacion'}, inplace=True)
    df.fillna(0, inplace=True)
    #df= detectar_outliers(df,'ElectricityFromFossilFuels(TWh)','Outlier_ElectricityFromFossilFuels(TWh)')
    #df= detectar_outliers(df,'ElectricityFromNuclear(TWh)','Outlier_ElectricityFromNuclear(TWh)')
    #df= detectar_outliers(df,'ElectricityFromRenewables(TWh)','Outlier_ElectricityFromRenewables(TWh)')
    df['Entity'] = df.Entity.map(d)
    df['Entity'] = df.Entity.map(f)
    df.rename(columns={'Entity':'Id_Entity'}, inplace=True)

    return df


def transformar_EPSS(path:str,sep:str,encoding:str,d:dict,f:dict) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df = df.reset_index()
    df.rename(columns={'index':'Id_electricity-prod-source-stacked','Electricity from coal (TWh)':'ElectricityFromCoal(TWh)','Electricity from gas (TWh)':'ElectricityFromGas(TWh)',
    'Electricity from hydro (TWh)':'ElectricityFromHydro(TWh)','Other renewables including bioenergy (TWh)':'OtherRenewablesIncludingBioenergy(TWh)','Electricity from solar (TWh)':'ElectricityFromSolar(TWh)',
    'Electricity from oil (TWh)':'ElectricityFromOil(TWh)','Electricity from wind (TWh)':'ElectricityFromWind(TWh)'}, inplace=True)
    df.fillna({'Code': 'Sin Informacion'}, inplace=True)
    df.fillna(0, inplace=True)
    #df= detectar_outliers(df,'ElectricityFromCoal(TWh)','Outlier_ElectricityFromCoal(TWh)')
    #df= detectar_outliers(df,'ElectricityFromGas(TWh)','Outlier_ElectricityFromGas(TWh)')
    #df= detectar_outliers(df,'ElectricityFromHydro(TWh)','Outlier_ElectricityFromHydro(TWh)')
    #df= detectar_outliers(df,'OtherRenewablesIncludingBioenergy(TWh)','Outlier_OtherRenewablesIncludingBioenergy(TWh)')
    #df= detectar_outliers(df,'ElectricityFromSolar(TWh)','Outlier_ElectricityFromSolar(TWh)')
    #df= detectar_outliers(df,'ElectricityFromOil(TWh)','Outlier_ElectricityFromOil(TWh)')
    #df= detectar_outliers(df,'ElectricityFromWind(TWh)','Outlier_ElectricityFromWind(TWh)')
    df['Entity'] = df.Entity.map(d)
    df['Entity'] = df.Entity.map(f)
    df.rename(columns={'Entity':'Id_Entity'}, inplace=True)
    
    
    return df

def transformar_GES(path:str,sep:str,encoding:str,d:dict,f:dict) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df = df.reset_index()
    df.rename(columns={'index':'Id_global-energy-substitution','Wind (TWh; substituted energy)':'Wind(TWh;SubstitutedEnergy)','Oil (TWh; substituted energy)':'Oil(TWh;SubstitutedEnergy)',
    'Nuclear (TWh; substituted energy)':'Nuclear(TWh;SubstitutedEnergy)','Hydropower (TWh; substituted energy)':'Hydropower(TWh;SubstitutedEnergy)','Traditional bimass (TWh; substituted energy)':'TraditionalBimass(TWh;SubstitutedEnergy)','Other renewables (TWh; substituted energy)':'OtherRenewables(TWh;SubstitutedEnergy)',
    'Biofuels (TWh; substituted energy)':'Biofuels(TWh;SubstitutedEnergy)','Solar (TWh; substituted energy)':'Solar(TWh;SubstitutedEnergy)','Coal (TWh; substituted energy)':'Coal(TWh;SubstitutedEnergy)','Gas (TWh; substituted energy)':'Gas(TWh;SubstitutedEnergy)'}, inplace=True)
    #df= detectar_outliers(df,'Wind(TWh;SubstitutedEnergy)','Outlier_Wind(TWh;SubstitutedEnergy)')
    #df= detectar_outliers(df,'Oil(TWh;SubstitutedEnergy)','Outlier_Oil(TWh;SubstitutedEnergy)')
    #df= detectar_outliers(df,'Nuclear(TWh;SubstitutedEnergy)','Outlier_Nuclear(TWh;SubstitutedEnergy)')
    #df= detectar_outliers(df,'Hydropower(TWh;SubstitutedEnergy)','Outlier_Hydropower(TWh;SubstitutedEnergy)')
    #df= detectar_outliers(df,'TraditionalBimass(TWh;SubstitutedEnergy)','Outlier_TraditionalBimass(TWh;SubstitutedEnergy)')
    #df= detectar_outliers(df,'OtherRenewables(TWh;SubstitutedEnergy)','Outlier_OtherRenewables(TWh;SubstitutedEnergy)')
    #df= detectar_outliers(df,'Biofuels(TWh;SubstitutedEnergy)','Outlier_Biofuels(TWh;SubstitutedEnergy)')
    #df= detectar_outliers(df,'Solar(TWh;SubstitutedEnergy)','Outlier_Solar(TWh;SubstitutedEnergy)')
    #df= detectar_outliers(df,'Coal(TWh;SubstitutedEnergy)','Outlier_Coal(TWh;SubstitutedEnergy)')
    #df= detectar_outliers(df,'Gas(TWh;SubstitutedEnergy)','Outlier_Gas(TWh;SubstitutedEnergy)')
    df['Entity'] = df.Entity.map(d)
    df['Entity'] = df.Entity.map(f)
    df.rename(columns={'Entity':'Id_Entity'}, inplace=True)
    
    
    return df

def transformar_LCSE(path:str,sep:str,encoding:str,d:dict,f:dict) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df = df.reset_index()
    df.rename(columns={'index':'Id_low-carbon-share-energy','Low-carbon energy (% equivalent primary energy)':'Low-CarbonEnergy(%PrimaryEnergy)'}, inplace=True)
    df.fillna({'Code': 'Sin Informacion'}, inplace=True)
    #df= detectar_outliers(df,'Low-CarbonEnergy(%PrimaryEnergy)','Outlier_Low-CarbonEnergy(%PrimaryEnergy)')
    df['Entity'] = df.Entity.map(d)
    df['Entity'] = df.Entity.map(f)
    df.rename(columns={'Entity':'Id_Entity'}, inplace=True)
    
    
    return df

def transformar_MREC(path:str,sep:str,encoding:str,d:dict,f:dict) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df = df.reset_index()
    df.rename(columns={'index':'Id_modern-renewable-energy-consumption','Wind Generation - TWh':'WindGeneration-TWh','Solar Generation - TWh':'SolarGeneration-TWh',
    'Geo Biomass Other - TWh':'GeoBiomassOther-TWh','Hydro Generation - TWh':'HydroGeneration-TWh'}, inplace=True)
    df.fillna({'Code': 'Sin Informacion'}, inplace=True)
    df.fillna(0, inplace=True)
    #df= detectar_outliers(df,'WindGeneration-TWh','Outlier_WindGeneration-TWh')
    #df= detectar_outliers(df,'SolarGeneration-TWh','Outlier_SolarGeneration-TWh')
    #df= detectar_outliers(df,'GeoBiomassOther-TWh','Outlier_GeoBiomassOther-TWh')
    #df= detectar_outliers(df,'HydroGeneration-TWh','Outlier_HydroGeneration-TWh')
    df['Entity'] = df.Entity.map(d)
    df['Entity'] = df.Entity.map(f)
    df.rename(columns={'Entity':'Id_Entity'}, inplace=True)
    
    
    return df

def transformar_PCE(path:str,sep:str,encoding:str,d:dict,f:dict) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df = df.reset_index()
    df.rename(columns={'index':'Id_per-capita-energy-use','Primary energy consumption per capita (kWh/person)':'PrimaryEnergyConsumptionPerCapita(kWh/Person)'}, inplace=True)
    df.fillna({'Code': 'Sin Informacion'}, inplace=True)
    #df= detectar_outliers(df,'PrimaryEnergyConsumptionPerCapita(kWh/Person)','Outlier_PrimaryEnergyConsumptionPerCapita(kWh/Person)')
    df['Entity'] = df.Entity.map(d)
    df['Entity'] = df.Entity.map(f)
    df.rename(columns={'Entity':'Id_Entity'}, inplace=True)
    
    
    return df

def transformar_PESB(path:str,sep:str,encoding:str,d:dict,f:dict) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df = df.reset_index()
    df.rename(columns={'index':'Id_primary-energy-source-bar','Coal Consumption - TWh':'CoalConsumption-TWh',
    'Oil Consumption - TWh':'OilConsumption-TWh','Gas Consumption - TWh':'GasConsumption-TWh',
    'Nuclear Consumption - TWh':'NuclearConsumption-TWh','Hydro Consumption - TWh':'HydroConsumption-TWh',
    'Wind Consumption - TWh':'WindConsumption-TWh','Solar Consumption - TWh':'SolarConsumption-TWh',
    'Geo Biomass Other - TWh':'GeoBiomassOther-TWh'}, inplace=True)
    df.fillna({'Code': 'Sin Informacion'}, inplace=True)
    df.fillna(0, inplace=True)
    #df= detectar_outliers(df,'CoalConsumption-TWh','Outlier_CoalConsumption-TWh')
    #df= detectar_outliers(df,'OilConsumption-TWh','Outlier_OilConsumption-TWh')
    #df= detectar_outliers(df,'GasConsumption-TWh','Outlier_GasConsumption-TWh')
    #df= detectar_outliers(df,'NuclearConsumption-TWh','Outlier_NuclearConsumption-TWh')
    #df= detectar_outliers(df,'HydroConsumption-TWh','Outlier_HydroConsumption-TWh')
    #df= detectar_outliers(df,'WindConsumption-TWh','Outlier_WindConsumption-TWh')
    #df= detectar_outliers(df,'SolarConsumption-TWh','Outlier_SolarConsumption-TWh')
    #df= detectar_outliers(df,'GeoBiomassOther-TWh','Outlier_GeoBiomassOther-TWh')

    df['Entity'] = df.Entity.map(d)
    df['Entity'] = df.Entity.map(f)
    df.rename(columns={'Entity':'Id_Entity'}, inplace=True)
    
    
    return df

def transformar_SEBS(path:str,sep:str,encoding:str,d:dict,f:dict) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df = df.reset_index()
    df.rename(columns={'index':'Id_share-elec-by-source','Coal (% electricity)':'ElectricityCoal%','Gas (% electricity)':'ElectricityGas%'
    ,'Hydro (% electricity)':'ElectricityHydro%','Solar (% electricity)':'ElectricitySolar%','Wind (% electricity)':'ElectricityWind%'
    ,'Oil (% electricity)':'ElectricityOil%','Nuclear (% electricity)':'ElectricityNuclear%','Other renewables including bioenergy (% electricity)':'ElectricityOtherRenewablesIncludingBioenergy%'}, inplace=True)
    df.fillna({'Code': 'Sin Informacion'}, inplace=True)
    df.fillna(0, inplace=True)

    #df= detectar_outliers(df,'ElectricityCoal%','Outlier_ElectricityCoal%')
    #df= detectar_outliers(df,'ElectricityGas%','Outlier_ElectricityGas%')
    #df= detectar_outliers(df,'ElectricityHydro%','Outlier_ElectricityHydro%')
    #df= detectar_outliers(df,'ElectricitySolar%','Outlier_ElectricitySolar%')
    #df= detectar_outliers(df,'ElectricityWind%','Outlier_ElectricityWind%')
    #df= detectar_outliers(df,'ElectricityOil%','Outlier_ElectricityOil%')
    #df= detectar_outliers(df,'ElectricityNuclear%','Outlier_ElectricityNuclear%')
    #df= detectar_outliers(df,'ElectricityOtherRenewablesIncludingBioenergy%','Outlier_ElectricityOtherRenewablesIncludingBioenergy%')

    df['Entity'] = df.Entity.map(d)
    df['Entity'] = df.Entity.map(f)
    df.rename(columns={'Entity':'Id_Entity'}, inplace=True)
    
    
    return df

def transformar_SOTPWATE(path:str,sep:str,encoding:str,d:dict,f:dict) -> pd.DataFrame:

    df = pd.read_csv(f'Datasets/{path}',sep=sep,encoding=encoding)

    df = df.reset_index()
    df.rename(columns={'index':'Id_share-of-the-population-with-access-to-electricity','Access to electricity (% of population)':'AccessToElectricity(%Population)'}, inplace=True)
    df.fillna({'Code': 'Sin Informacion'}, inplace=True)
    #df= detectar_outliers(df,'AccessToElectricity(%Population)','Outlier_AccessToElectricity(%Population)')
    
    df['Entity'] = df.Entity.map(d)
    df['Entity'] = df.Entity.map(f)
    df.rename(columns={'Entity':'Id_Entity'}, inplace=True)
    return df

def exportCSV(df1,name):
    df1.to_csv(name, encoding='utf-8', index=False)

def exportar_archivo(carpeta_actual:str,carpeta_destino:str,name:str,carpeta_normalizada:str,df:pd.DataFrame) -> None:
    """
    Cambia la ubicación de un archivo.

    Parameters:
    carpeta_actual: Nombre de la carpeta donde se encuentra el archivo actualmente. Ejemplo: 'archivos'
    carpeta_destino: Nombre de la carpeta donde será reubicado el archivo. En caso de que la carpeta no exista, 
                     será creada. Ejemplo: 'archivos_reubicados'
    name: Nombre del archivo que será reubicado. Ejemplo: 'archivo.txt'
    """
    ruta = carpeta_normalizada+'/'+name
    exportCSV(df,ruta)
    
    directory = os.getcwd()
    os.makedirs(os.path.dirname(f"{directory}\{carpeta_destino}\{name}"), exist_ok=True)
    try:
        os.rename(f"{directory}\{carpeta_actual}\{name}",f"{directory}\{carpeta_destino}\{name}")
    except(FileNotFoundError) as error:
        print(error)