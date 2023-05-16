CREATE SCHEMA IF NOT EXISTS army_corps;
CREATE TABLE IF NOT EXISTS army_corps.port_tonnage (
    port_name text,
    year smallint,
    total_tons double precision,
    domestic_tons double precision,
    foreign_tons double precision,
    import_tons double precision,
    export_tons double precision
);

CREATE TABLE IF NOT EXISTS army_corps.principal_ports (
    port_name text,
    x double precision,
    y double precision,
    msa_geoid character(5),
    dvrpc text
);

CREATE VIEW army_corps.dvrpc_region_tonnage AS
    SELECT port_tonnage."year", 
        SUM(port_tonnage.domestic_tons) AS domestic_tons,
        SUM(port_tonnage.import_tons) AS import_tons,
        SUM(port_tonnage.export_tons) AS export_tons
    FROM army_corps.port_tonnage LEFT JOIN army_corps.principal_ports ON principal_ports.port_name = port_tonnage.port_name
    WHERE principal_ports.dvrpc = 'y'
    GROUP BY port_tonnage."year" 
    ORDER BY port_tonnage."year" DESC;

CREATE VIEW army_corps.msa_yearly_rankings AS
    SELECT principal_ports.msa_geoid,
        port_tonnage.year,
        mode() WITHIN GROUP (ORDER BY msas.basename) AS msa_name,
        sum(port_tonnage.domestic_tons) AS domestic_tons,
        sum(port_tonnage.import_tons) AS import_tons,
        sum(port_tonnage.export_tons) AS export_tons,
        sum(port_tonnage.domestic_tons + port_tonnage.import_tons + port_tonnage.export_tons) AS total_tons,
        rank() OVER (PARTITION BY port_tonnage.year ORDER BY (sum(port_tonnage.total_tons)) DESC) AS rank
    FROM census.msas
        LEFT JOIN army_corps.principal_ports ON msas.geoid = principal_ports.msa_geoid::text
        LEFT JOIN army_corps.port_tonnage ON port_tonnage.port_name = principal_ports.port_name
    WHERE port_tonnage.year <> 0
    GROUP BY principal_ports.msa_geoid, port_tonnage.year
    ORDER BY (rank() OVER (ORDER BY (sum(port_tonnage.total_tons)) DESC));
