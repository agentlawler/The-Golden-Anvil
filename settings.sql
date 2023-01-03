CREATE DATABASE ganvil_with_auth;
CREATE USER ganviluser WITH PASSWORD 'ganvil';
GRANT ALL PRIVILEGES ON DATABASE ganvil_with_auth TO ganviluser;