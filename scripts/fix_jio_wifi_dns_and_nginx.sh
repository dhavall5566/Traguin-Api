#!/bin/bash
# Re-apply Jio WiFi / IPv6 nginx fix and restart website.
# Run on server as root: bash fix_jio_wifi_dns_and_nginx.sh

set -euo pipefail

echo "==> 1. Ensure nginx listens on IPv6 for website, API, CRM"
for f in node_website.conf node_crm.conf python_api.conf; do
  path="/www/server/panel/vhost/nginx/$f"
  if [ ! -f "$path" ]; then
    echo "skip missing $path"
    continue
  fi
  if ! grep -q 'listen \[::\]:80' "$path"; then
    sed -i 's/listen 80;/listen 80;\n    listen [::]:80;/' "$path"
    echo "  added IPv6 :80 to $f"
  fi
  if ! grep -q 'listen \[::\]:443' "$path"; then
    sed -i 's/listen 443 ssl;/listen 443 ssl;\n    listen [::]:443 ssl;/' "$path"
    echo "  added IPv6 :443 to $f"
  fi
done

nginx -t
nginx -s reload
echo "==> nginx reloaded (IPv4 + IPv6)"

echo "==> 2. Disable aaPanel auto-build (prevents CPU + conflicts)"
python3 << 'PY'
import json, sqlite3
db = sqlite3.connect("/www/server/panel/data/default.db")
for site_id in (4, 6):
    row = db.execute("SELECT project_config FROM sites WHERE id=?", (site_id,)).fetchone()
    if not row:
        continue
    cfg = json.loads(row[0])
    cfg["is_power_on"] = 0
    cfg["project_script"] = "start"
    db.execute("UPDATE sites SET project_config=? WHERE id=?", (json.dumps(cfg), site_id))
    print(f"  site {site_id}: is_power_on=0")
db.commit()
PY

echo "==> 3. Restart website (PM2 as www)"
sudo -u www pm2 restart website 2>/dev/null || {
  cd /www/wwwroot/website
  sudo -u www bash -c 'export NODE_ENV=production && pm2 start npm --name website -- start'
}
sudo -u www pm2 save
sudo -u www pm2 list

echo "==> 4. Local health check"
curl -s -o /dev/null -w "  http://127.0.0.1:3000 => %{http_code}\n" http://127.0.0.1:3000
curl -6 -s -o /dev/null -w "  https://[2a02:4780:12:cf75::1]/ (Host: traguin.in) => %{http_code}\n" \
  -H 'Host: traguin.in' --insecure https://[2a02:4780:12:cf75::1]/ 2>/dev/null || echo "  IPv6 curl skipped"

echo ""
echo "==> IMPORTANT: Fix DNS in Hostinger (browser) — Jio WiFi uses this!"
echo "  Domain traguin.in → DNS records:"
echo "    A     @    195.35.7.208"
echo "    AAAA  @    2a02:4780:12:cf75::1   (or DELETE AAAA to force IPv4 only)"
echo "  Remove wrong A record 147.93.99.216 if present."
echo "  Nameservers should be Hostinger's, NOT dns-parking.com."
echo ""
echo "Done."
