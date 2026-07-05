#!/usr/bin/env bash
# Migrate cms + crm schemas from Neon to split VPS databases (public schema on each host).

set -euo pipefail

PG18_BIN="${PG18_BIN:-/opt/homebrew/opt/postgresql@18/bin}"
PG_DUMP="${PG_DUMP:-$PG18_BIN/pg_dump}"
PSQL="${PSQL:-psql}"

SOURCE_DATABASE_URL="${SOURCE_DATABASE_URL:-}"
CMS_TARGET_URL="${CMS_TARGET_URL:-postgresql://traguincms:WszAYrrwkGhRKrNP@195.35.7.208:5432/traguincms}"
CRM_TARGET_URL="${CRM_TARGET_URL:-postgresql://traguincrm:TS88DmHrL4ekZnSX@195.35.7.208:5432/traguincrm}"

if [[ -z "$SOURCE_DATABASE_URL" ]]; then
  if [[ -f .env ]]; then
    line="$(grep -E '^DATABASE_URL=' .env | head -1 || true)"
    if [[ "$line" == *neon* ]]; then
      SOURCE_DATABASE_URL="${line#DATABASE_URL=}"
      SOURCE_DATABASE_URL="${SOURCE_DATABASE_URL//\"/}"
    fi
  fi
fi

if [[ -z "$SOURCE_DATABASE_URL" ]]; then
  echo "Set SOURCE_DATABASE_URL to the Neon unified database URL." >&2
  exit 1
fi

WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

restore_schema_to_public() {
  local schema="$1"
  local target_url="$2"
  local sql_file="$WORKDIR/${schema}.sql"
  local transformed="$WORKDIR/${schema}_public.sql"

  echo "==> Dumping ${schema} schema..."
  "$PG_DUMP" "$SOURCE_DATABASE_URL" \
    --schema="$schema" \
    --no-owner \
    --no-privileges \
    --format=plain \
    --file="$sql_file"

  echo "==> Transforming ${schema} → public on target..."
  sed \
    -e "/^CREATE SCHEMA ${schema};/d" \
    -e "/^COMMENT ON SCHEMA ${schema}/d" \
    -e "s/\"${schema}\"\\.\"public\"/\"public\"/g" \
    -e "s/${schema}\\./public./g" \
    -e "s/SCHEMA ${schema}/SCHEMA public/g" \
    -e "/REFERENCES cms\\./d" \
    -e "/REFERENCES crm\\./d" \
    "$sql_file" > "$transformed"

  echo "==> Wiping public tables on target..."
  "$PSQL" "$target_url" -v ON_ERROR_STOP=1 <<'SQL'
DO $$ DECLARE r RECORD;
BEGIN
  FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
    EXECUTE 'DROP TABLE IF EXISTS public.' || quote_ident(r.tablename) || ' CASCADE';
  END LOOP;
END $$;
SQL

  echo "==> Restoring to target..."
  set +e
  "$PSQL" "$target_url" -v ON_ERROR_STOP=0 -f "$transformed" >/dev/null
  set -e

  local count
  count="$("$PSQL" "$target_url" -Atc "SELECT count(*) FROM information_schema.tables WHERE table_schema='public'")"
  echo "    public tables: $count"
}

echo "Migrating Traguin database to VPS..."
restore_schema_to_public cms "$CMS_TARGET_URL"
restore_schema_to_public crm "$CRM_TARGET_URL"
echo "==> Migration complete."
