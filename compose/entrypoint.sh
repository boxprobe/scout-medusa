#!/bin/sh
set -e

echo "=== Medusa Demo Entrypoint ==="

BACKEND_DIR="/app/apps/backend"

# Write .env for the backend from compose-injected env vars.
cat > "$BACKEND_DIR/.env" <<EOF
DATABASE_URL=${DATABASE_URL}
REDIS_URL=${REDIS_URL}
JWT_SECRET=${JWT_SECRET}
COOKIE_SECRET=${COOKIE_SECRET}
STORE_CORS=${STORE_CORS}
ADMIN_CORS=${ADMIN_CORS}
AUTH_CORS=${AUTH_CORS}
NODE_ENV=${NODE_ENV:-production}
EOF

echo "--- Running database migrations ---"
cd "$BACKEND_DIR"
for i in $(seq 1 10); do
  if pnpm medusa db:migrate; then
    break
  fi
  echo "Migration failed, retry $i/10 in 5s..."
  sleep 5
done

echo "--- Creating admin user (admin@medusa-test.com / supersecret) ---"
pnpm medusa user -e admin@medusa-test.com -p supersecret 2>/dev/null || {
  echo "(Admin user may already exist, continuing...)"
}

echo "--- Starting Medusa ---"
exec pnpm medusa start
