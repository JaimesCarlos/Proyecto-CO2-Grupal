-- Database: ProyectoGrupal
-- DROP DATABASE "ProyectoGrupal";
/*
CREATE DATABASE "ProyectoGrupal"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
	*/
	
-- Table: public.CarbonIntensityElectricity
-- DROP TABLE IF EXISTS public."CarbonIntensityElectricity";
CREATE TABLE IF NOT EXISTS public."CarbonIntensityElectricity"
(
    "Id_carbon-intensity-electricity" bigint NOT NULL,
    "Id_Entity" bigint,
    "Code" text COLLATE pg_catalog."default",
    "Year" bigint,
    "Id_CarbonIntensityofElectricity(gCO2/kWh)" double precision,
    "Outlier_Carbon_(gCO2/kWh)" bigint,
    CONSTRAINT "CarbonIntensityElectricity_pkey" PRIMARY KEY ("Id_carbon-intensity-electricity"),
    CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
        REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."CarbonIntensityElectricity"
    OWNER to postgres;

-- Index: fki_Entity
-- DROP INDEX IF EXISTS public."fki_Entity";
CREATE INDEX IF NOT EXISTS "fki_Entity"
    ON public."CarbonIntensityElectricity" USING btree
    ("Id_Entity" ASC NULLS LAST)
    TABLESPACE pg_default;	
	
	
	
-- Table: public.ElecMixBar
-- DROP TABLE IF EXISTS public."ElecMixBar";
CREATE TABLE IF NOT EXISTS public."ElecMixBar"
(
    "Id_elec-mix-bar" bigint NOT NULL,
    "Id_Entity" bigint,
    "Code" text COLLATE pg_catalog."default",
    "Year" bigint,
    "ElectricityFromFossilFuels(TWh)" double precision,
    "ElectricityFromNuclear(TWh)" double precision,
    "ElectricityFromRenewables(TWh)" double precision,
    "Outlier_ElectricityFromFossilFuels(TWh)" bigint,
    "Outlier_ElectricityFromNuclear(TWh)" bigint,
    "Outlier_ElectricityFromRenewables(TWh)" bigint,
    CONSTRAINT "ElecMixBar_pkey" PRIMARY KEY ("Id_elec-mix-bar"),
    CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
        REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."ElecMixBar"
    OWNER to postgres;	



-- Table: public.ElectricityProdSourceStacked
-- DROP TABLE IF EXISTS public."ElectricityProdSourceStacked";
CREATE TABLE IF NOT EXISTS public."ElectricityProdSourceStacked"
(
    "Id_electricity-prod-source-stacked" bigint NOT NULL,
    "Id_Entity" bigint,
    "Code" text COLLATE pg_catalog."default",
    "Year" bigint,
    "ElectricityFromCoal(TWh)" double precision,
    "ElectricityFromGas(TWh)" double precision,
    "ElectricityFromHydro(TWh)" double precision,
    "OtherRenewablesIncludingBioenergy(TWh)" double precision,
    "ElectricityFromSolar(TWh)" double precision,
    "ElectricityFromOil(TWh)" double precision,
    "ElectricityFromWind(TWh)" double precision,
    "Electricity from nuclear (TWh)" double precision,
    "Outlier_ElectricityFromCoal(TWh)" bigint,
    "Outlier_ElectricityFromGas(TWh)" bigint,
    "Outlier_ElectricityFromHydro(TWh)" bigint,
    "Outlier_OtherRenewablesIncludingBioenergy(TWh)" bigint,
    "Outlier_ElectricityFromSolar(TWh)" bigint,
    "Outlier_ElectricityFromOil(TWh)" bigint,
    "Outlier_ElectricityFromWind(TWh)" bigint,
    CONSTRAINT "ElectricityProdSourceStacked_pkey" PRIMARY KEY ("Id_electricity-prod-source-stacked"),
    CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
        REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."ElectricityProdSourceStacked"
    OWNER to postgres;	
	
	
-- Table: public.Energyco
-- DROP TABLE IF EXISTS public."Energyco";
CREATE TABLE IF NOT EXISTS public."Energyco"
(
    "Id_Energyco2" bigint NOT NULL,
    "Id_Entity" bigint,
    "Energy_type" text COLLATE pg_catalog."default",
    "Year" bigint,
    "Energy_consumption" double precision,
    "Energy_production" double precision,
    "GDP" double precision,
    "Population" double precision,
    "Energy_intensity_per_capita" double precision,
    "Energy_intensity_by_GDP" double precision,
    "CO2_emission" double precision,
    "Outlier_CO2_emission" bigint,
    "Outlier_Energy_consumption" bigint,
    "Outlier_Energy_production" bigint,
    CONSTRAINT "Energyco_pkey" PRIMARY KEY ("Id_Energyco2"),
    CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
        REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Energyco"
    OWNER to postgres;
	
-- Table: public.Entidades
-- DROP TABLE IF EXISTS public."Entidades";
CREATE TABLE IF NOT EXISTS public."Entidades"
(
    "Id_Entity" bigint NOT NULL,
    "Code" text COLLATE pg_catalog."default",
    "Entity" text COLLATE pg_catalog."default",
    "Lat" double precision,
    "Long" double precision,
    CONSTRAINT "Entidades_pkey" PRIMARY KEY ("Id_Entity")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Entidades"
    OWNER to postgres;
	

-- Table: public.GlobalEnergySubstitution
-- DROP TABLE IF EXISTS public."GlobalEnergySubstitution";
CREATE TABLE IF NOT EXISTS public."GlobalEnergySubstitution"
(
    "Id_global-energy-substitution" bigint NOT NULL,
    "Id_Entity" bigint,
    "Code" text COLLATE pg_catalog."default",
    "Year" bigint,
    "Wind(TWh;SubstitutedEnergy)" bigint,
    "Oil(TWh;SubstitutedEnergy)" bigint,
    "Nuclear(TWh;SubstitutedEnergy)" bigint,
    "Hydropower(TWh;SubstitutedEnergy)" bigint,
    "TraditionalBimass(TWh;SubstitutedEnergy)" bigint,
    "OtherRenewables(TWh;SubstitutedEnergy)" bigint,
    "Biofuels(TWh;SubstitutedEnergy)" bigint,
    "Solar(TWh;SubstitutedEnergy)" bigint,
    "Coal(TWh;SubstitutedEnergy)" bigint,
    "Gas(TWh;SubstitutedEnergy)" bigint,
    "Outlier_Wind(TWh;SubstitutedEnergy)" bigint,
    "Outlier_Oil(TWh;SubstitutedEnergy)" bigint,
    "Outlier_Nuclear(TWh;SubstitutedEnergy)" bigint,
    "Outlier_Hydropower(TWh;SubstitutedEnergy)" bigint,
    "Outlier_TraditionalBimass(TWh;SubstitutedEnergy)" bigint,
    "Outlier_OtherRenewables(TWh;SubstitutedEnergy)" bigint,
    "Outlier_Biofuels(TWh;SubstitutedEnergy)" bigint,
    "Outlier_Solar(TWh;SubstitutedEnergy)" bigint,
    "Outlier_Coal(TWh;SubstitutedEnergy)" bigint,
    "Outlier_Gas(TWh;SubstitutedEnergy)" bigint,
    CONSTRAINT "GlobalEnergySubstitution_pkey" PRIMARY KEY ("Id_global-energy-substitution"),
    CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
        REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."GlobalEnergySubstitution"
    OWNER to postgres;


-- Table: public.GlobalPowerPlantDatabase
-- DROP TABLE IF EXISTS public."GlobalPowerPlantDatabase";
CREATE TABLE IF NOT EXISTS public."GlobalPowerPlantDatabase"
(
    "Id_global_power_plant" bigint NOT NULL,
    country text COLLATE pg_catalog."default",
    "Id_Entity" bigint,
    name text COLLATE pg_catalog."default",
    gppd_idnr text COLLATE pg_catalog."default",
    capacity_mw double precision,
    latitude double precision,
    longitude double precision,
    primary_fuel text COLLATE pg_catalog."default",
    other_fuel1 text COLLATE pg_catalog."default",
    other_fuel2 text COLLATE pg_catalog."default",
    other_fuel3 text COLLATE pg_catalog."default",
    commissioning_year double precision,
    owner text COLLATE pg_catalog."default",
    geolocation_source text COLLATE pg_catalog."default",
    wepp_id text COLLATE pg_catalog."default",
    generation_data_source text COLLATE pg_catalog."default",
    "Outlier_capacity_mw" bigint,
    CONSTRAINT "GlobalPowerPlantDatabase_pkey" PRIMARY KEY ("Id_global_power_plant"),
    CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
        REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."GlobalPowerPlantDatabase"
    OWNER to postgres;
	

-- Table: public.LowCarbonShareEnergy
-- DROP TABLE IF EXISTS public."LowCarbonShareEnergy";
CREATE TABLE IF NOT EXISTS public."LowCarbonShareEnergy"
(
    "Id_low-carbon-share-energy" bigint NOT NULL,
    "Id_Entity" bigint,
    "Code" text COLLATE pg_catalog."default",
    "Year" bigint,
    "Low-CarbonEnergy(%PrimaryEnergy)" double precision,
    "Outlier_Low-CarbonEnergy(%PrimaryEnergy)" bigint,
    CONSTRAINT "LowCarbonShareEnergy_pkey" PRIMARY KEY ("Id_low-carbon-share-energy"),
    CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
        REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."LowCarbonShareEnergy"
    OWNER to postgres;
	
-- Table: public.ModernRenewableEnergyConsumption
-- DROP TABLE IF EXISTS public."ModernRenewableEnergyConsumption";
CREATE TABLE IF NOT EXISTS public."ModernRenewableEnergyConsumption"
(
    "Id_modern-renewable-energy-consumption" bigint NOT NULL,
    "Id_Entity" bigint,
    "Code" text COLLATE pg_catalog."default",
    "Year" bigint,
    "WindGeneration-TWh" double precision,
    "SolarGeneration-TWh" double precision,
    "GeoBiomassOther-TWh" double precision,
    "HydroGeneration-TWh" double precision,
    "Outlier_WindGeneration-TWh" bigint,
    "Outlier_SolarGeneration-TWh" bigint,
    "Outlier_GeoBiomassOther-TWh" bigint,
    "Outlier_HydroGeneration-TWh" bigint,
    CONSTRAINT "ModernRenewableEnergyConsumption_pkey" PRIMARY KEY ("Id_modern-renewable-energy-consumption"),
    CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
        REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."ModernRenewableEnergyConsumption"
    OWNER to postgres;	
	
-- Table: public.PerCapitaEnergyUse
-- DROP TABLE IF EXISTS public."PerCapitaEnergyUse";
CREATE TABLE IF NOT EXISTS public."PerCapitaEnergyUse"
(
    "Id_per-capita-energy-use" bigint NOT NULL,
    "Id_Entity" bigint,
    "Code" text COLLATE pg_catalog."default",
    "Year" bigint,
    "PrimaryEnergyConsumptionPerCapita(kWh/Person)" double precision,
    "Outlier_PrimaryEnergyConsumptionPerCapita(kWh/Person)" bigint,
    CONSTRAINT "PerCapitaEnergyUse_pkey" PRIMARY KEY ("Id_per-capita-energy-use"),
    CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
        REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."PerCapitaEnergyUse"
    OWNER to postgres;
	
-- Table: public.PrimaryEnergySourceBar
-- DROP TABLE IF EXISTS public."PrimaryEnergySourceBar";
CREATE TABLE IF NOT EXISTS public."PrimaryEnergySourceBar"
(
    "Id_primary-energy-source-bar" bigint NOT NULL,
    "Id_Entity" bigint,
    "Code" text COLLATE pg_catalog."default",
    "Year" bigint,
    "CoalConsumption-TWh" double precision,
    "OilConsumption-TWh" double precision,
    "GasConsumption-TWh" double precision,
    "NuclearConsumption-TWh" double precision,
    "HydroConsumption-TWh" double precision,
    "WindConsumption-TWh" double precision,
    "SolarConsumption-TWh" double precision,
    "GeoBiomassOther-TWh" double precision,
    "Outlier_CoalConsumption-TWh" bigint,
    "Outlier_OilConsumption-TWh" bigint,
    "Outlier_GasConsumption-TWh" bigint,
    "Outlier_NuclearConsumption-TWh" bigint,
    "Outlier_HydroConsumption-TWh" bigint,
    "Outlier_WindConsumption-TWh" bigint,
    "Outlier_SolarConsumption-TWh" bigint,
    "Outlier_GeoBiomassOther-TWh" bigint,
    CONSTRAINT "PrimaryEnergySourceBar_pkey" PRIMARY KEY ("Id_primary-energy-source-bar"),
    CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
        REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."PrimaryEnergySourceBar"
    OWNER to postgres;	
	

-- Table: public.ShareElecBySource
-- DROP TABLE IF EXISTS public."ShareElecBySource";
CREATE TABLE IF NOT EXISTS public."ShareElecBySource"
(
    "Id_share-elec-by-source" bigint NOT NULL,
    "Id_Entity" bigint,
    "Code" text COLLATE pg_catalog."default",
    "Year" bigint,
    "ElectricityCoal%" double precision,
    "ElectricityGas%" double precision,
    "ElectricityHydro%" double precision,
    "ElectricitySolar%" double precision,
    "ElectricityWind%" double precision,
    "ElectricityOil%" double precision,
    "ElectricityNuclear%" double precision,
    "ElectricityOtherRenewablesIncludingBioenergy%" double precision,
    "Outlier_ElectricityCoal%" bigint,
    "Outlier_ElectricityGas%" bigint,
    "Outlier_ElectricityHydro%" bigint,
    "Outlier_ElectricitySolar%" bigint,
    "Outlier_ElectricityWind%" bigint,
    "Outlier_ElectricityOil%" bigint,
    "Outlier_ElectricityNuclear%" bigint,
    "Outlier_ElectricityOtherRenewablesIncludingBioenergy%" bigint,
    CONSTRAINT "ShareElecBySource_pkey" PRIMARY KEY ("Id_share-elec-by-source"),
    CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
        REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."ShareElecBySource"
    OWNER to postgres;