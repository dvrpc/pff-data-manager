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
    port_code text,
    port_name text,
    port_type text,
    year smallint
);

CREATE TABLE IF NOT EXISTS army_corps.dvrpc_port_names (
    port_name text,
    dvrpc text
);

CREATE VIEW army_corps.panj_port_names AS
    SELECT DISTINCT port_tonnage.port_name, 
        army_corps.principal_ports.port_code
    FROM army_corps.port_tonnage 
    LEFT OUTER JOIN army_corps.principal_ports ON principal_ports.port_name = port_tonnage.port_name
    WHERE (port_tonnage.port_name LIKE '%PA' OR port_tonnage.port_name LIKE '%NJ');

CREATE VIEW army_corps.dvrpc_region_tonnage AS
    SELECT port_tonnage."year", 
        SUM(port_tonnage.domestic_tons) AS domestic_tons,
        SUM(port_tonnage.import_tons) AS import_tons,
        SUM(port_tonnage.export_tons) AS export_tons
    FROM army_corps.port_tonnage LEFT JOIN army_corps.dvrpc_port_names ON dvrpc_port_names.port_name = port_tonnage.port_name
    WHERE dvrpc_port_names.dvrpc = 'y'
    GROUP BY port_tonnage."year" 
    ORDER BY port_tonnage."year" DESC;