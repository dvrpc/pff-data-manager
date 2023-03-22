CREATE SCHEMA IF NOT EXISTS census;
CREATE TABLE IF NOT EXISTS census.msas (
    basename text,
    name text,
    geoid text,
    geom geometry
);
