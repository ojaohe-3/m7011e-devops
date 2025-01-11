-- Database: core-app

-- DROP DATABASE IF EXISTS "core-app";

CREATE DATABASE "core-app"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- Database: keycloak

-- DROP DATABASE IF EXISTS keycloak;

CREATE DATABASE keycloak
    WITH
    OWNER = keycloak
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- Database: registry

-- DROP DATABASE IF EXISTS registry;

CREATE DATABASE registry
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- Database: event-log

-- DROP DATABASE IF EXISTS "event-log";

CREATE DATABASE "event-log"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- Role: keycloak
-- password is 'secret' change to appropriate
-- DROP ROLE IF EXISTS keycloak;

CREATE ROLE keycloak WITH
  LOGIN
  SUPERUSER
  INHERIT
  CREATEDB
  CREATEROLE
  NOREPLICATION
  BYPASSRLS
  ENCRYPTED PASSWORD 'SCRAM-SHA-256$4096:bNsZXzv4OQWJ6lnwaMzCOQ==$VqRYXqG9mCy3eGvkMJ1fsNWjI54HjwquqCqrYEJBQ6s=:ypm6s/hdt/iU1Y2t1TCgm/vDB7rq3HI5cqTDbwFPm3M='; 

