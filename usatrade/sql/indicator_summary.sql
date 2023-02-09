-- View: ustrade.indicator_summary
-- DROP VIEW ustrade.indicator_summary;

CREATE OR REPLACE VIEW ustrade.indicator_summary AS
SELECT annual_trade.year,
       round(sum(annual_trade.vessel_kg * 0.00110231::double precision) FILTER (
                                                                                WHERE annual_trade.type = 'exports'::text)) AS swt_exports,
       round(sum(annual_trade.vessel_kg * 0.00110231::double precision) FILTER (
                                                                                WHERE annual_trade.type = 'imports'::text)) AS swt_imports
FROM ustrade.annual_trade
GROUP BY annual_trade.year
ORDER BY annual_trade.year;


ALTER TABLE ustrade.indicator_summary OWNER TO mruane;

COMMENT ON VIEW ustrade.indicator_summary IS 'Annual summary data for PFF maritime indicators';

COMMENT ON COLUMN ustrade.indicator_summary.swt_exports IS 'Export volume by shipping weight in tons';

COMMENT ON COLUMN ustrade.indicator_summary.swt_imports IS 'Import volume by shipping weight in tons';