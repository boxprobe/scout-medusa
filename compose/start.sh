#!/usr/bin/env bash
# scout-medusa — bring up Medusa baseline + target on local ports.
#
# Pinned to two specific dtc-starter commits matching Medusa releases.
# Edit BASELINE_COMMIT / TARGET_COMMIT to switch the version pair.
#
# Local access after start completes:
#   Baseline (v2.13.6): http://localhost:19000/app
#   Target   (v2.14.0): http://localhost:29000/app
#
# Login: admin@medusa-test.com / supersecret

set -euo pipefail

# === Version config ===
BASELINE_COMMIT=a57eb5114957ff215c37b314c5d9080de1f99847  # dtc-starter @ Medusa v2.13.6
TARGET_COMMIT=8327b6390f1cef5f0f5bc232f60f775e8ad69954    # dtc-starter @ Medusa v2.14.0
# ======================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# Ensure shared network exists (target backend joins baseline's DB through it).
docker network create medusa-shared 2>/dev/null || true

start_baseline() {
    local commit="$1"
    local port_backend="$2"

    echo "==> Starting medusa-baseline (commit: ${commit:0:12})"
    TAG=baseline \
    COMMIT="$commit" \
    PORT_BACKEND="$port_backend" \
    docker compose --profile with-db -p medusa-baseline up --build -d
}

start_target() {
    local commit="$1"
    local port_backend="$2"

    echo "==> Starting medusa-target (commit: ${commit:0:12}, shared DB)"
    TAG=target \
    COMMIT="$commit" \
    PORT_BACKEND="$port_backend" \
    DB_HOST=medusa-pg-baseline \
    REDIS_HOST=medusa-redis-baseline \
    docker compose -p medusa-target up --build -d
}

stop_instance() {
    local tag="$1"
    if docker compose -p "medusa-${tag}" ps -q 2>/dev/null | grep -q .; then
        echo "==> Stopping medusa-${tag}"
        docker compose -p "medusa-${tag}" down
    fi
}

start_baseline "$BASELINE_COMMIT" 19000

if [ -n "${TARGET_COMMIT:-}" ]; then
    start_target "$TARGET_COMMIT" 29000
else
    stop_instance target
fi

echo ""
echo "==> Done. Login: admin@medusa-test.com / supersecret"
echo "    Baseline (v2.13.6): http://localhost:19000/app"
if [ -n "${TARGET_COMMIT:-}" ]; then
    echo "    Target   (v2.14.0): http://localhost:29000/app"
fi
