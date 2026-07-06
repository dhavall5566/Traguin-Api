#!/usr/bin/env python3
"""Re-sync itinerary highlights, days, hotels, and inclusions for all seeded packages.

Safe to re-run: existing packages/itineraries are updated in place; nothing is deleted
except nested rows that are replaced by the script definitions.
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

# Standalone and batch insert scripts that define full itinerary nested content.
SYNC_MODULES = [
    "insert_ch_006_chandigarh_package",
    "insert_mh_003_package",
    "insert_gj_003_package",
    "insert_hp_003_package",
    "insert_gj_004_005_packages",
    "insert_hp_004_006_007_009_010_packages",
    "insert_hp_011_020_packages",
    "insert_kl_packages",
    "insert_jk_packages",
    "insert_us_packages",
    "insert_za_packages",
    "insert_it_packages",
    "insert_th_packages",
    "insert_uk_packages",
    "insert_sg_packages",
    "insert_rj_packages",
    "insert_uae_packages",
    "insert_vn_packages",
    "insert_my_packages",
    "insert_fr_packages",
    "insert_ch_packages",
    "insert_tr_packages",
    "insert_au_packages",
    "insert_jp_packages",
    "insert_id_packages",
    "insert_kr_packages",
]


def main() -> None:
    failures: list[str] = []
    for module_name in SYNC_MODULES:
        print(f"\n========== {module_name} ==========")
        try:
            module = importlib.import_module(module_name)
            module.main()
        except Exception as exc:
            failures.append(f"{module_name}: {exc}")
            print(f"FAILED {module_name}: {exc}", file=sys.stderr)

    print("\n========== Summary ==========")
    if failures:
        print(f"Completed with {len(failures)} failure(s):", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        sys.exit(1)
    print(f"Successfully synced nested content via {len(SYNC_MODULES)} script(s).")


if __name__ == "__main__":
    main()
