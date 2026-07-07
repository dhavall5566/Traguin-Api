#!/usr/bin/env python3
"""Export existing batch-def builder modules to JSON import files.

Examples:
  python scripts/export_batch_defs_to_json.py --all-domestic
  python scripts/export_batch_defs_to_json.py --all-international
  python scripts/export_batch_defs_to_json.py --all
  python scripts/export_batch_defs_to_json.py --preset ap,tn,uk
  python scripts/export_batch_defs_to_json.py --module andhra_pradesh_domestic_batch_defs \\
      --destination-slug andhra-pradesh --builders-var ANDHRA_PRADESH_DOMESTIC_BUILDERS
"""

from __future__ import annotations

import argparse
import importlib
import sys
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
_API_DIR = _SCRIPTS_DIR.parent
if str(_API_DIR) not in sys.path:
    sys.path.insert(0, str(_API_DIR))
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from package_json_io import PLACEHOLDER_DESTINATION_ID, export_builder_to_dict, write_package_import_file

# (module_name, destination_slug, builders_var OR tuple of builder function names)
ExportSpec = tuple[str, str, str | tuple[str, ...]]

DOMESTIC_SOURCES: list[ExportSpec] = [
    ("chhattisgarh_domestic_batch_defs", "chhattisgarh", "CHHATTISGARH_DOMESTIC_BUILDERS"),
    ("bihar_domestic_batch_defs", "bihar", "BIHAR_DOMESTIC_BUILDERS"),
    ("assam_domestic_batch_defs", "assam", "ASSAM_DOMESTIC_BUILDERS"),
    ("arunachal_pradesh_domestic_batch_defs", "arunachal-pradesh", "ARUNACHAL_PRADESH_DOMESTIC_BUILDERS"),
    ("andhra_pradesh_domestic_batch_defs", "andhra-pradesh", "ANDHRA_PRADESH_DOMESTIC_BUILDERS"),
    ("andaman_domestic_batch_defs", "andaman-and-nicobar", "ANDAMAN_DOMESTIC_BUILDERS"),
    ("west_bengal_domestic_batch_defs", "west-bengal", "WEST_BENGAL_DOMESTIC_BUILDERS"),
    ("tamil_nadu_domestic_batch_defs", "tamil-nadu", "TAMIL_NADU_DOMESTIC_BUILDERS"),
    ("uk_011_018_batch_defs", "uttarakhand", "UK_011_018_BUILDERS"),
    ("rajasthan_domestic_batch_defs", "rajasthan", "RAJASTHAN_DOMESTIC_BUILDERS"),
    ("puducherry_domestic_batch_defs", "puducherry", "PUDUCHERRY_DOMESTIC_BUILDERS"),
    ("madhya_pradesh_domestic_batch_defs", "madhya-pradesh", "MADHYA_PRADESH_DOMESTIC_BUILDERS"),
    ("madhya_pradesh_mp_001_010_domestic_batch_defs", "madhya-pradesh", "MADHYA_PRADESH_MP_001_010_BUILDERS"),
    ("maharashtra_domestic_batch_defs", "maharashtra", "MAHARASHTRA_DOMESTIC_BUILDERS"),
    ("maharashtra_mh_001_005_domestic_batch_defs", "maharashtra", "MAHARASHTRA_MH_001_005_BUILDERS"),
    ("meghalaya_domestic_batch_defs", "meghalaya", "MEGHALAYA_DOMESTIC_BUILDERS"),
    ("manipur_domestic_batch_defs", "manipur", "MANIPUR_DOMESTIC_BUILDERS"),
    ("mizoram_domestic_batch_defs", "mizoram", "MIZORAM_DOMESTIC_BUILDERS"),
    ("odisha_domestic_batch_defs", "odisha", "ODISHA_DOMESTIC_BUILDERS"),
    ("nagaland_domestic_batch_defs", "nagaland", "NAGALAND_DOMESTIC_BUILDERS"),
    ("punjab_pb_001_010_domestic_batch_defs", "punjab", "PUNJAB_PB_001_010_BUILDERS"),
    ("lakshadweep_lk_batch_defs", "lakshadweep", "LAKSHADWEEP_LK_BUILDERS"),
    ("lakshadweep_domestic_batch_defs", "lakshadweep", "LAKSHADWEEP_DOMESTIC_BUILDERS"),
    ("ladakh_domestic_batch_defs", "ladakh", "LADAKH_DOMESTIC_BUILDERS"),
    ("kerala_domestic_batch_defs", "kerala", "KERALA_DOMESTIC_BUILDERS"),
    ("kerala_kl_001_010_domestic_batch_defs", "kerala", "KERALA_KL_001_010_BUILDERS"),
    ("karnataka_domestic_batch_defs", "karnataka", "KARNATAKA_DOMESTIC_BUILDERS"),
    ("kashmir_domestic_batch_defs", "kashmir", "KASHMIR_DOMESTIC_BUILDERS"),
    ("kashmir_jk_001_010_domestic_batch_defs", "kashmir", "KASHMIR_JK_001_010_BUILDERS"),
    ("gujarat_domestic_batch_defs", "gujarat", "GUJARAT_DOMESTIC_BUILDERS"),
    ("dadra_nagar_haveli_batch_defs", "dadra-and-nagar-haveli", "DADRA_NAGAR_HAVELI_BUILDERS"),
    ("goa_domestic_batch_defs", "goa", "GOA_DOMESTIC_BUILDERS"),
    ("daman_diu_batch_defs", "daman-and-diu", "DAMAN_DIU_BUILDERS"),
    ("delhi_domestic_batch_defs", "delhi", "DELHI_DOMESTIC_BUILDERS"),
    ("himachal_domestic_batch_defs", "himachal", "HIMACHAL_DOMESTIC_BUILDERS"),
    ("haryana_domestic_batch_defs", "haryana", "HARYANA_DOMESTIC_BUILDERS"),
    ("jharkhand_domestic_batch_defs", "jharkhand", "JHARKHAND_DOMESTIC_BUILDERS"),
    ("chandigarh_domestic_batch_defs", "punjab", "CHANDIGARH_DOMESTIC_BUILDERS"),
    ("rj_batch_package_defs", "rajasthan", "RJ_BUILDERS"),
    ("rajasthan_rj_003_004_006_008_010_domestic_batch_defs", "rajasthan", "RAJASTHAN_RJ_003_004_006_008_010_BUILDERS"),
    ("uk_batch_package_defs", "uttarakhand", "UK_BUILDERS"),
    (
        "hp_batch_package_defs",
        "himachal",
        ("build_hp_004", "build_hp_006", "build_hp_007", "build_hp_009", "build_hp_010"),
    ),
    (
        "hp_batch_package_defs_011_020",
        "himachal",
        (
            "build_hp_011",
            "build_hp_012",
            "build_hp_013",
            "build_hp_014",
            "build_hp_015",
            "build_hp_017",
            "build_hp_018",
            "build_hp_019",
            "build_hp_020",
        ),
    ),
    (
        "jk_batch_package_defs",
        "kashmir",
        ("build_jk_001", "build_jk_002", "build_jk_003", "build_jk_004", "build_jk_006", "build_jk_007", "build_jk_010"),
    ),
    (
        "kl_batch_package_defs",
        "kerala",
        ("build_kl_001", "build_kl_002", "build_kl_003", "build_kl_005", "build_kl_006", "build_kl_009", "build_kl_010"),
    ),
]

INTERNATIONAL_SOURCES: list[ExportSpec] = [
    ("th_batch_package_defs", "thailand", "TH_BUILDERS"),
    ("us_batch_package_defs", "usa", "US_BUILDERS"),
    ("za_batch_package_defs", "south-africa", "ZA_BUILDERS"),
    ("it_batch_package_defs", "italy", "IT_BUILDERS"),
    ("sg_batch_package_defs", "singapore", "SG_BUILDERS"),
    ("uae_batch_package_defs", "uae", "UAE_BUILDERS"),
    ("vn_batch_package_defs", "vietnam", "VN_BUILDERS"),
    ("my_batch_package_defs", "malaysia", "MY_BUILDERS"),
    ("fr_batch_package_defs", "france", "FR_BUILDERS"),
    ("ch_batch_package_defs", "switzerland", "CH_BUILDERS"),
    ("tr_batch_package_defs", "turkey", "TR_BUILDERS"),
    ("au_batch_package_defs", "australia", "AU_BUILDERS"),
    ("jp_batch_package_defs", "japan", "JP_BUILDERS"),
    ("id_batch_package_defs", "bali", "ID_BUILDERS"),
    ("kr_batch_package_defs", "south-korea", "KR_BUILDERS"),
]

PRESETS: dict[str, ExportSpec] = {
    "ap": DOMESTIC_SOURCES[0],
    "an": DOMESTIC_SOURCES[1],
    "wb": DOMESTIC_SOURCES[2],
    "tn": DOMESTIC_SOURCES[3],
    "uk": DOMESTIC_SOURCES[4],
}


def _resolve_builders(module, spec: str | tuple[str, ...]) -> list[Callable]:
    if isinstance(spec, str):
        builders = getattr(module, spec)
        return list(builders)
    return [getattr(module, name) for name in spec]


def _unpack_builder_result(result):
    if len(result) == 3:
        return result[0], result[1]
    return result[0], result[1]


def export_spec(spec: ExportSpec, out_dir: Path) -> int:
    module_name, destination_slug, builders_spec = spec
    module = importlib.import_module(module_name)
    builders = _resolve_builders(module, builders_spec)
    count = 0

    for builder in builders:
        package, itinerary = _unpack_builder_result(builder(PLACEHOLDER_DESTINATION_ID))
        filename = f"{package.serial_code}.json" if package.serial_code else f"{package.slug}.json"
        payload = export_builder_to_dict(
            destination_slug=destination_slug,
            package=package,
            itinerary=itinerary,
        )
        out_path = out_dir / filename
        write_package_import_file(out_path, payload)
        print(f"  Wrote {out_path.name} ({len(itinerary.days)} days, {len(itinerary.hotels)} hotels)")
        count += 1

    return count


def export_sources(sources: Sequence[ExportSpec], out_dir: Path) -> int:
    total = 0
    for spec in sources:
        module_name = spec[0]
        print(f"\nExporting {module_name}...")
        total += export_spec(spec, out_dir)
    return total


def main() -> None:
    parser = argparse.ArgumentParser(description="Export batch-def builders to JSON import files.")
    parser.add_argument(
        "--out-dir",
        help="Output directory relative to api/ (overrides --all-domestic/international defaults)",
    )
    parser.add_argument("--preset", help="Comma-separated presets: ap, an, wb, tn, uk")
    parser.add_argument("--all-domestic", action="store_true", help="Export all domestic batch-def modules")
    parser.add_argument("--all-international", action="store_true", help="Export all international batch-def modules")
    parser.add_argument("--all", action="store_true", help="Export domestic + international")
    parser.add_argument("--module", help="Python module name under api/scripts/")
    parser.add_argument("--destination-slug", help="Destination slug for exported JSON")
    parser.add_argument("--builders-var", help="Module list constant name, e.g. ANDHRA_PRADESH_DOMESTIC_BUILDERS")
    args = parser.parse_args()

    if args.all:
        args.all_domestic = True
        args.all_international = True

    total = 0

    if args.all_domestic:
        out_dir = Path(args.out_dir or "data/packages/domestic")
        if not out_dir.is_absolute():
            out_dir = (_API_DIR / out_dir).resolve()
        print(f"=== Domestic export → {out_dir} ===")
        total += export_sources(DOMESTIC_SOURCES, out_dir)

    if args.all_international:
        out_dir = Path(args.out_dir or "data/packages/international")
        if not out_dir.is_absolute():
            out_dir = (_API_DIR / out_dir).resolve()
        print(f"\n=== International export → {out_dir} ===")
        total += export_sources(INTERNATIONAL_SOURCES, out_dir)

    if args.preset:
        out_dir = Path(args.out_dir or "data/packages/domestic")
        if not out_dir.is_absolute():
            out_dir = (_API_DIR / out_dir).resolve()
        for key in [p.strip() for p in args.preset.split(",") if p.strip()]:
            if key not in PRESETS:
                raise SystemExit(f"Unknown preset {key!r}. Choose from: {', '.join(PRESETS)}")
            print(f"\nExporting preset {key}...")
            total += export_spec(PRESETS[key], out_dir)

    if args.module:
        if not args.destination_slug or not args.builders_var:
            parser.error("--module requires --destination-slug and --builders-var")
        out_dir = Path(args.out_dir or "data/packages/domestic")
        if not out_dir.is_absolute():
            out_dir = (_API_DIR / out_dir).resolve()
        print(f"\nExporting {args.module}...")
        total += export_spec((args.module, args.destination_slug, args.builders_var), out_dir)

    if not any([args.all_domestic, args.all_international, args.preset, args.module]):
        parser.error("Provide --all, --all-domestic, --all-international, --preset, or --module")

    print(f"\nExported {total} package JSON file(s)")


if __name__ == "__main__":
    main()
