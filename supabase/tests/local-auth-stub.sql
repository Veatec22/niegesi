-- Minimalna namiastka środowiska Supabase dla testów na zwykłym PostgreSQL (bez Dockera):
-- role API i auth.uid() czytające identyfikator z ustawienia sesji jak PostgREST.
create role anon nologin;
create role authenticated nologin;
create role service_role nologin bypassrls;
create schema auth;
create table auth.users (id uuid primary key, email text);
create function auth.uid() returns uuid language sql stable as $$
  select nullif(current_setting('request.jwt.claim.sub', true), '')::uuid
$$;
grant usage on schema auth to anon, authenticated;
grant execute on function auth.uid() to anon, authenticated;
grant usage on schema public to anon, authenticated;
