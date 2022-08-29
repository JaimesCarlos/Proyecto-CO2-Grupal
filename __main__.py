from configuracion import CONFIG_DATASETS,DATABASE_CONFIG,ARCHIVOS,DATASETS,DATASET_DESTINO,DATASET_NORMALIZADO
import transformar as t
from cargar import crear_db,cargar
import pandas as pd
import numpy as np

#ENTIDADES = pd.DataFrame()
def main():

    crear_db(DATABASE_CONFIG)
    #Ejecucion de scrip para normalizar las entidades
    Entity = pd.read_csv('.\Datasets\Datasets_extra\Entidades_Coor.csv',delimiter = ';',decimal =".", encoding="UTF-8") 
    Entity.fillna({'Code': 'Sin Informacion'}, inplace=True)
    Entity.fillna(0, inplace=True)
    d = dict(zip(Entity['Entity'],Entity['CountryNormalizado']))

    Entityfinal = pd.read_csv('.\Datasets\Datasets_extra\entidadesfinal.csv',delimiter = ';',decimal =".", encoding="UTF-8") 
    Entityfinal.fillna({'Code': 'Sin Informacion'}, inplace=True)
    Entityfinal.fillna(0, inplace=True)
    f = dict(zip(Entityfinal['Entity'],Entityfinal['Id_Entity']))
   
   
    for archivo in ARCHIVOS:
        
        if archivo[-3:] != 'csv':
           pass

        elif archivo[:9] == 'entidades':
            df = t.transformar_entidades(archivo,CONFIG_DATASETS['Entidades']['sep'],CONFIG_DATASETS['Entidades']['encoding'])
            #d = dict(zip(df['Entity'],df['Id_Entity']))
            cargar(DATABASE_CONFIG,df,'Entidades')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df)

        elif archivo[:8] == 'energyco':
            df = t.transformar_energyco2(archivo,CONFIG_DATASETS['energyco']['sep'],CONFIG_DATASETS['energyco']['encoding'],d,f)
            cargar(DATABASE_CONFIG,df,'Energyco')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df)
        
        elif archivo[:27] == 'global_power_plant_database':
            df = t.transformar_GPPD(archivo,CONFIG_DATASETS['global_power_plant_database']['sep'],CONFIG_DATASETS['global_power_plant_database']['encoding'],d,f)
            generation_gwh=t.generation_gwh()
            prueba=pd.merge(Entityfinal,df,on=('Id_Entity'),how='right')
            prueba.drop(['Entity','Code_x','Code_y','Lat','Long'],axis=1,inplace=True)
            prueba=prueba.reindex(columns=['Id_planta','Id_Entity','name','capacity_mw','primary_fuel'])
            prueba.fillna(0, inplace=True)
            prueba = prueba.astype({"Id_Entity": np.dtype("int64")})

            generation_gwh_id=pd.merge(prueba,generation_gwh,on=('name'),how='right')
            generation_gwh_id=generation_gwh_id.reset_index()
            generation_gwh_id.rename({'index':'Id_GeneracionPlantaYear'},axis=1,inplace=True)
            generation_gwh_id=generation_gwh_id.loc[:,['Id_GeneracionPlantaYear','Id_planta','generation_gwh','year']]
            generation_gwh_id.fillna(0,inplace=True)
            cargar(DATABASE_CONFIG,generation_gwh_id,'GeneracionPlantaYear')
            ruta = DATASET_NORMALIZADO+'/GeneracionPlantaYear.csv'
            t.exportCSV(df,ruta)
            cargar(DATABASE_CONFIG,prueba,'GlobalPowerPlantDatabase')
            ruta = DATASET_NORMALIZADO+'/GlobalPowerPlantDatabase.csv'
            t.exportCSV(df,ruta)
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df)

        elif archivo[:30] == 'owid-energy-consumption-source':
            df = t.transformar_OECS(archivo,CONFIG_DATASETS['owid-energy-consumption-source']['sep'],CONFIG_DATASETS['owid-energy-consumption-source']['encoding'],d,f)
            cargar(DATABASE_CONFIG,df,'OwidEnergyConsumptionSource')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df)

        elif archivo[:50] == 'Access-to-clean-fuels-and-technologies-for-cooking':
            df = t.transformar_ATCFATFC(archivo,CONFIG_DATASETS['Access-to-clean-fuels-and-technologies-for-cooking']['sep'],CONFIG_DATASETS['Access-to-clean-fuels-and-technologies-for-cooking']['encoding'],d,f)
            cargar(DATABASE_CONFIG,df,'AccesstoCleanFuelsAndTechnologiesForCooking')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df)
        
        elif archivo[:28] == 'carbon-intensity-electricity':
            df = t.transformar_CIE(archivo,CONFIG_DATASETS['carbon-intensity-electricity']['sep'],CONFIG_DATASETS['carbon-intensity-electricity']['encoding'],d,f)
            cargar(DATABASE_CONFIG,df,'CarbonIntensityElectricity')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df)
        
        elif archivo[:12] == 'elec-mix-bar':
            df = t.transformar_EMB(archivo,CONFIG_DATASETS['elec-mix-bar']['sep'],CONFIG_DATASETS['elec-mix-bar']['encoding'],d,f)
            cargar(DATABASE_CONFIG,df,'ElecMixBar')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df)
        
        elif archivo[:31] == 'electricity-prod-source-stacked':
            df = t.transformar_EPSS(archivo,CONFIG_DATASETS['electricity-prod-source-stacked']['sep'],CONFIG_DATASETS['electricity-prod-source-stacked']['encoding'],d,f)
            cargar(DATABASE_CONFIG,df,'ElectricityProdSourceStacked')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df)

        elif archivo[:26] == 'global-energy-substitution':
            df = t.transformar_GES(archivo,CONFIG_DATASETS['global-energy-substitution']['sep'],CONFIG_DATASETS['global-energy-substitution']['encoding'],d,f)
            cargar(DATABASE_CONFIG,df,'GlobalEnergySubstitution')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df)

        elif archivo[:23] == 'low-carbon-share-energy':
            df = t.transformar_LCSE(archivo,CONFIG_DATASETS['low-carbon-share-energy']['sep'],CONFIG_DATASETS['low-carbon-share-energy']['encoding'],d,f)
            cargar(DATABASE_CONFIG,df,'LowCarbonShareEnergy')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df) 

        elif archivo[:35] == 'modern-renewable-energy-consumption':
            df = t.transformar_MREC(archivo,CONFIG_DATASETS['modern-renewable-energy-consumption']['sep'],CONFIG_DATASETS['modern-renewable-energy-consumption']['encoding'],d,f)
            cargar(DATABASE_CONFIG,df,'ModernRenewableEnergyConsumption')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df) 

        elif archivo[:21] == 'per-capita-energy-use':
            df = t.transformar_PCE(archivo,CONFIG_DATASETS['per-capita-energy-use']['sep'],CONFIG_DATASETS['per-capita-energy-use']['encoding'],d,f)
            cargar(DATABASE_CONFIG,df,'PerCapitaEnergyUse')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df) 

        elif archivo[:25] == 'primary-energy-source-bar':
            df = t.transformar_PESB(archivo,CONFIG_DATASETS['primary-energy-source-bar']['sep'],CONFIG_DATASETS['primary-energy-source-bar']['encoding'],d,f)
            cargar(DATABASE_CONFIG,df,'PrimaryEnergySourceBar')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df) 

        elif archivo[:20] == 'share-elec-by-source':
            df = t.transformar_SEBS(archivo,CONFIG_DATASETS['share-elec-by-source']['sep'],CONFIG_DATASETS['share-elec-by-source']['encoding'],d,f)
            cargar(DATABASE_CONFIG,df,'ShareElecBySource')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df) 

        elif archivo[:50] == 'share-of-the-population-with-access-to-electricity':
            df = t.transformar_SOTPWATE(archivo,CONFIG_DATASETS['share-of-the-population-with-access-to-electricity']['sep'],CONFIG_DATASETS['share-of-the-population-with-access-to-electricity']['encoding'],d,f)
            cargar(DATABASE_CONFIG,df,'ShareOfThePopulationWithAccessToElectricity')
            t.exportar_archivo(DATASETS[:-1],DATASET_DESTINO,archivo,DATASET_NORMALIZADO,df) 

        
if __name__ == '__main__':
    main()  