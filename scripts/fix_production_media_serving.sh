#!/bin/bash
# Fix gallery/client-story images on production.
# Run on the API server as root: bash scripts/fix_production_media_serving.sh

set -euo pipefail

API_DIR="${API_DIR:-/www/wwwroot/api}"
NGINX_CONF="/www/server/panel/vhost/nginx/python_api.conf"
UPLOADS_DIR="$API_DIR/uploads/media"

echo "==> Upload files on disk: $(find "$UPLOADS_DIR" -type f 2>/dev/null | wc -l | tr -d ' ')"

if ! grep -q "location /uploads/" "$NGINX_CONF" 2>/dev/null; then
  echo "==> Adding nginx /uploads/ proxy to $NGINX_CONF"
  sed -i '/#REWRITE-END/a\
\
    location /uploads/ {\
        proxy_pass http://127.0.0.1:8000;\
        proxy_set_header Host $host;\
        proxy_set_header X-Real-IP $remote_addr;\
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;\
        proxy_http_version 1.1;\
    }' "$NGINX_CONF"
  nginx -t && nginx -s reload
  echo "==> nginx reloaded"
else
  echo "==> nginx already has /uploads/ location"
fi

SAMPLE="$(find "$UPLOADS_DIR" -type f -name '*.jpg' 2>/dev/null | head -1)"
if [ -n "$SAMPLE" ]; then
  BASENAME="$(basename "$SAMPLE")"
  echo "==> Local API test:"
  curl -sI "http://127.0.0.1:8000/uploads/media/$BASENAME" | head -3
else
  echo "WARNING: No jpg files in $UPLOADS_DIR — re-upload portraits via CMS admin."
fi

echo "==> Done. Ensure website .env has CMS_API_URL=http://127.0.0.1:8000 and redeploy web."
