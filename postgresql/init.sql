-- Drop the public schema if it exists
ALTER DATABASE postgres OWNER TO postgres;
DROP SCHEMA IF EXISTS public;
CREATE SCHEMA real_estate;
ALTER ROLE postgres SET search_path TO real_estate;