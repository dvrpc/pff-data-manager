
# US Census Trade data schema 
def create_usa_trade:
    """
    CREATE TABLE ustrade.annual_trade
        (
        uid SERIAL,
        portid character varying(4),
        portname text,
        year smallint,
        hs_group smallint,
        type text,
        vessel_kg double precision,
        vessel_value double precision,
        cont_kg double precision,
        cont_value double precision
        )
    """

# Maritime Exchange data schema
def create_port_lookup:
    """
    CREATE TABLE marex.ship_calls
        (
        oid serial NOT NULL,
        date timestamp without time zone,
        vessel text,
        rig text,
        flag text,
        name text,
        locid text,
        state character varying(2),
        cargo_typ text,
        cargo text,
        dir character varying(1),
        CONSTRAINT ship_calls_pkey PRIMARY KEY (oid)
        )
    """
