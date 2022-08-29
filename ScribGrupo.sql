-- CREAR PRIMARY KEY

-- Constraint: Entidades_pkey
-- ALTER TABLE IF EXISTS public."Entidades" DROP CONSTRAINT IF EXISTS "Entidades_pkey";
ALTER TABLE IF EXISTS public."Entidades"
    ADD CONSTRAINT "Entidades_pkey" PRIMARY KEY ("Id_Entity");
	

-- Constraint: Entity
-- Constraint: CarbonIntensityElectricity_pkey
-- ALTER TABLE IF EXISTS public."CarbonIntensityElectricity" DROP CONSTRAINT IF EXISTS "CarbonIntensityElectricity_pkey";
ALTER TABLE IF EXISTS public."CarbonIntensityElectricity"
    ADD CONSTRAINT "CarbonIntensityElectricity_pkey" PRIMARY KEY ("Id_carbon-intensity-electricity");

-- Constraint: ElecMixBar_pkey
-- ALTER TABLE IF EXISTS public."ElecMixBar" DROP CONSTRAINT IF EXISTS "ElecMixBar_pkey";
ALTER TABLE IF EXISTS public."ElecMixBar"
    ADD CONSTRAINT "ElecMixBar_pkey" PRIMARY KEY ("Id_elec-mix-bar");

-- Constraint: ElectricityProdSourceStacked_pkey
-- ALTER TABLE IF EXISTS public."ElectricityProdSourceStacked" DROP CONSTRAINT IF EXISTS "ElectricityProdSourceStacked_pkey";
ALTER TABLE IF EXISTS public."ElectricityProdSourceStacked"
    ADD CONSTRAINT "ElectricityProdSourceStacked_pkey" PRIMARY KEY ("Id_electricity-prod-source-stacked");

-- Constraint: Energyco_pkey
-- ALTER TABLE IF EXISTS public."Energyco" DROP CONSTRAINT IF EXISTS "Energyco_pkey";
ALTER TABLE IF EXISTS public."Energyco"
    ADD CONSTRAINT "Energyco_pkey" PRIMARY KEY ("Id_Energyco2");

-- Constraint: GlobalEnergySubstitution_pkey
-- ALTER TABLE IF EXISTS public."GlobalEnergySubstitution" DROP CONSTRAINT IF EXISTS "GlobalEnergySubstitution_pkey";
ALTER TABLE IF EXISTS public."GlobalEnergySubstitution"
    ADD CONSTRAINT "GlobalEnergySubstitution_pkey" PRIMARY KEY ("Id_global-energy-substitution");

-- Constraint: GlobalPowerPlantDatabase_pkey
-- ALTER TABLE IF EXISTS public."GlobalPowerPlantDatabase" DROP CONSTRAINT IF EXISTS "GlobalPowerPlantDatabase_pkey";
ALTER TABLE IF EXISTS public."GlobalPowerPlantDatabase"
    ADD CONSTRAINT "GlobalPowerPlantDatabase_pkey" PRIMARY KEY ("Id_global_power_plant");

-- Constraint: LowCarbonShareEnergy_pkey
-- ALTER TABLE IF EXISTS public."LowCarbonShareEnergy" DROP CONSTRAINT IF EXISTS "LowCarbonShareEnergy_pkey";
ALTER TABLE IF EXISTS public."LowCarbonShareEnergy"
    ADD CONSTRAINT "LowCarbonShareEnergy_pkey" PRIMARY KEY ("Id_low-carbon-share-energy");

-- Constraint: ModernRenewableEnergyConsumption_pkey
-- ALTER TABLE IF EXISTS public."ModernRenewableEnergyConsumption" DROP CONSTRAINT IF EXISTS "ModernRenewableEnergyConsumption_pkey";
ALTER TABLE IF EXISTS public."ModernRenewableEnergyConsumption"
    ADD CONSTRAINT "ModernRenewableEnergyConsumption_pkey" PRIMARY KEY ("Id_modern-renewable-energy-consumption");

-- Constraint: PerCapitaEnergyUse_pkey
-- ALTER TABLE IF EXISTS public."PerCapitaEnergyUse" DROP CONSTRAINT IF EXISTS "PerCapitaEnergyUse_pkey";
ALTER TABLE IF EXISTS public."PerCapitaEnergyUse"
    ADD CONSTRAINT "PerCapitaEnergyUse_pkey" PRIMARY KEY ("Id_per-capita-energy-use");

-- Constraint: PrimaryEnergySourceBar_pkey
-- ALTER TABLE IF EXISTS public."PrimaryEnergySourceBar" DROP CONSTRAINT IF EXISTS "PrimaryEnergySourceBar_pkey";
ALTER TABLE IF EXISTS public."PrimaryEnergySourceBar"
    ADD CONSTRAINT "PrimaryEnergySourceBar_pkey" PRIMARY KEY ("Id_primary-energy-source-bar");

-- Constraint: ShareElecBySource_pkey
-- ALTER TABLE IF EXISTS public."ShareElecBySource" DROP CONSTRAINT IF EXISTS "ShareElecBySource_pkey";
ALTER TABLE IF EXISTS public."ShareElecBySource"
    ADD CONSTRAINT "ShareElecBySource_pkey" PRIMARY KEY ("Id_share-elec-by-source");








--CREAR CLAVES FORANEAS

	

-- Constraint: Entity
-- ALTER TABLE IF EXISTS public."CarbonIntensityElectricity" DROP CONSTRAINT IF EXISTS "Entity";
ALTER TABLE IF EXISTS public."CarbonIntensityElectricity"
    ADD CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
    REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;
	
-- Constraint: Entity
-- ALTER TABLE IF EXISTS public."ElecMixBar" DROP CONSTRAINT IF EXISTS "Entity";
ALTER TABLE IF EXISTS public."ElecMixBar"
    ADD CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
    REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;	
	
-- Constraint: Entity
-- ALTER TABLE IF EXISTS public."ElectricityProdSourceStacked" DROP CONSTRAINT IF EXISTS "Entity";
ALTER TABLE IF EXISTS public."ElectricityProdSourceStacked"
    ADD CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
    REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;	
	
-- Constraint: Entity
-- ALTER TABLE IF EXISTS public."Energyco" DROP CONSTRAINT IF EXISTS "Entity";
ALTER TABLE IF EXISTS public."Energyco"
    ADD CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
    REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;	

-- Constraint: Entity
-- ALTER TABLE IF EXISTS public."GlobalEnergySubstitution" DROP CONSTRAINT IF EXISTS "Entity";
ALTER TABLE IF EXISTS public."GlobalEnergySubstitution"
    ADD CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
    REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;
	
-- Constraint: Entity
-- ALTER TABLE IF EXISTS public."GlobalPowerPlantDatabase" DROP CONSTRAINT IF EXISTS "Entity";
ALTER TABLE IF EXISTS public."GlobalPowerPlantDatabase"
    ADD CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
    REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;	
	
-- Constraint: Entity
-- ALTER TABLE IF EXISTS public."LowCarbonShareEnergy" DROP CONSTRAINT IF EXISTS "Entity";
ALTER TABLE IF EXISTS public."LowCarbonShareEnergy"
    ADD CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
    REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;	

-- Constraint: Entity
-- ALTER TABLE IF EXISTS public."ModernRenewableEnergyConsumption" DROP CONSTRAINT IF EXISTS "Entity";
ALTER TABLE IF EXISTS public."ModernRenewableEnergyConsumption"
    ADD CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
    REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

-- Constraint: Entity
-- ALTER TABLE IF EXISTS public."PerCapitaEnergyUse" DROP CONSTRAINT IF EXISTS "Entity";
ALTER TABLE IF EXISTS public."PerCapitaEnergyUse"
    ADD CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
    REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

-- Constraint: Entity
-- ALTER TABLE IF EXISTS public."PrimaryEnergySourceBar" DROP CONSTRAINT IF EXISTS "Entity";
ALTER TABLE IF EXISTS public."PrimaryEnergySourceBar"
    ADD CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
    REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

-- Constraint: Entity
-- ALTER TABLE IF EXISTS public."ShareElecBySource" DROP CONSTRAINT IF EXISTS "Entity";
ALTER TABLE IF EXISTS public."ShareElecBySource"
    ADD CONSTRAINT "Entity" FOREIGN KEY ("Id_Entity")
    REFERENCES public."Entidades" ("Id_Entity") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;







--INDEX


CREATE INDEX IF NOT EXISTS "fki_Entity"
    ON public."CarbonIntensityElectricity" USING btree
    ("Id_Entity" ASC NULLS LAST)
    TABLESPACE pg_default;
	
CREATE INDEX IF NOT EXISTS "fki_Entity"
    ON public."ElecMixBar" USING btree
    ("Id_Entity" ASC NULLS LAST)
    TABLESPACE pg_default;
	
CREATE INDEX IF NOT EXISTS "fki_Entity"
    ON public."ElectricityProdSourceStacked" USING btree
    ("Id_Entity" ASC NULLS LAST)
    TABLESPACE pg_default;
	
CREATE INDEX IF NOT EXISTS "fki_Entity"
    ON public."Energyco" USING btree
    ("Id_Entity" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX IF NOT EXISTS "fki_Entity"
    ON public."GlobalEnergySubstitution" USING btree
    ("Id_Entity" ASC NULLS LAST)
    TABLESPACE pg_default;
	
CREATE INDEX IF NOT EXISTS "fki_Entity"
    ON public."GlobalPowerPlantDatabase" USING btree
    ("Id_Entity" ASC NULLS LAST)
    TABLESPACE pg_default;
	
CREATE INDEX IF NOT EXISTS "fki_Entity"
    ON public."LowCarbonShareEnergy" USING btree
    ("Id_Entity" ASC NULLS LAST)
    TABLESPACE pg_default;	
	
CREATE INDEX IF NOT EXISTS "fki_Entity"
    ON public."ModernRenewableEnergyConsumption" USING btree
    ("Id_Entity" ASC NULLS LAST)
    TABLESPACE pg_default;
	
CREATE INDEX IF NOT EXISTS "fki_Entity"
    ON public."PerCapitaEnergyUse" USING btree
    ("Id_Entity" ASC NULLS LAST)
    TABLESPACE pg_default;
	
CREATE INDEX IF NOT EXISTS "fki_Entity"
    ON public."PrimaryEnergySourceBar" USING btree
    ("Id_Entity" ASC NULLS LAST)
    TABLESPACE pg_default;
	
CREATE INDEX IF NOT EXISTS "fki_Entity"
    ON public."ShareElecBySource" USING btree
    ("Id_Entity" ASC NULLS LAST)
    TABLESPACE pg_default;
	



	
--	ERROR:  could not create unique index "ID_entidad"
--DETAIL:  Key ("Id_Entity")=(158) is duplicated.