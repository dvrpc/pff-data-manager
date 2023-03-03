CREATE TABLE IF NOT EXISTS army_corps.port_tonnage (
    port_name text,
    year smallint,
    total_tons double precision,
    domestic_tons double precision,
    foreign_tons double precision,
    import_tons double precision,
    export_tons double precision
)

CREATE TABLE IF NOT EXISTS army_corps.principal_ports (
    port_code text
    port_name text,
    port_type text
    year smallint
)
