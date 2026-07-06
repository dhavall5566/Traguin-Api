"""Curated destination gallery URLs — mirrors traguin.in/destinations frontend fallbacks."""

from __future__ import annotations

def _p(photo_id: int) -> str:
    return (
        f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg"
        f"?auto=compress&cs=tinysrgb&w=1400"
    )


def _u(photo_id: str) -> str:
    return (
        f"https://images.unsplash.com/photo-{photo_id}"
        f"?ixlib=rb-4.1.0&auto=format&fit=crop&w=1400&q=80"
    )


FALLBACK_IMAGE = _p(2387866)

# Matches traguin/src/data/destination-galleries.ts
DESTINATION_GALLERIES: dict[str, list[str]] = {
    "switzerland": [_p(417173), _p(6720718), _p(1365425), _p(5728978), _u("1506905925346-21bda4d32df4")],
    "japan": [_p(30988649), _p(402028), _p(31604390), _p(16412311), _p(3408354)],
    "dubai": [_u("1512453979798-5ea266f8880c"), _p(338504), _p(189296), _p(3768111), _p(6642521)],
    "bali": [_p(3608263), _p(2581922), _p(2166553), _p(7061662), _p(2766971)],
    "kashmir": [_p(6738359), _p(164372), _p(1457842), _p(1024993), _p(2885324)],
    "thailand": [_u("1552465011-b4e21bf6e79a"), _p(1040880), _p(2175682), _p(1764207), _p(3227646)],
    "vietnam": [_p(3787839), _p(4099234), _p(3951377), _p(2666816), _p(5773808)],
    "singapore": [_p(259447), _p(1823384), _p(3385153), _p(2132465), _p(5824529)],
    "kerala": [_u("1717069541470-9b1a2b085e1f"), _p(960733), _p(2507010), _p(2785317), _p(4497193)],
    "himachal": [_p(3574440), _p(4877062), _p(7170023), _u("1657894736581-ccc35d62d9e2"), _p(261181)],
    "uttarakhand": [_p(5726011), _p(1365425), _p(1693441), _p(2387873), _p(2666297)],
    "punjab": [_p(25264894), _p(3601425), _p(1179229), _p(631317), _p(1121111)],
    "delhi": [_p(1070535), _p(358532), _p(6231570), _p(3278215), _p(4606211)],
    "uttar-pradesh": [_p(316458), _p(2367253), _p(752042), _p(1179229), _p(358532)],
    "gujarat": [_p(631317), _p(1179229), _p(2367253), _p(752042), _p(1121111)],
    "rajasthan": [_p(1271619), _p(3278215), _p(358532), _p(6231570), _p(4606211)],
    # International destinations shown on /destinations (hero + gallery frames)
    "australia": [
        _p(1872053),
        _p(1032650),
        _p(3601425),
        _p(2387873),
        _p(6720718),
    ],
    "france": [_p(161853), _p(1128440), _p(236698), _p(338515), _p(161901)],
    "italy": [_p(2521621), _p(315566), _p(2030966), _p(834892), _p(268351)],
    "malaysia": [_p(325933), _p(2161219), _p(1450360), _p(3601425), _p(2387866)],
    "south-africa": [_p(2594474), _p(631317), _p(631325), _p(1179229), _p(3601425)],
    "south-korea": [_p(2376999), _p(2089937), _p(358532), _p(3251170), _p(6303798)],
    "turkey": [_p(161825), _p(325933), _p(3601425), _p(2387873), _p(161853)],
    "usa": [_p(64271), _p(64270), _p(64272), _p(64273), _p(2387873)],
    "maharashtra": [_p(2387866), _p(316458), _p(2367253), _p(752042), _p(358532)],
}

SLUG_ALIASES: dict[str, str] = {
    "jammu-kashmir": "kashmir",
    "uae": "dubai",
    "id": "bali",
}


def gallery_urls_for_destination_slug(slug: str, *, region: str | None = None, india_region: str | None = None) -> list[str]:
    key = SLUG_ALIASES.get(slug, slug)
    if key in DESTINATION_GALLERIES:
        return list(DESTINATION_GALLERIES[key])

    if region == "domestic" and india_region:
        region_heroes = {
            "north": DESTINATION_GALLERIES["himachal"][0],
            "south": DESTINATION_GALLERIES["kerala"][0],
            "west": DESTINATION_GALLERIES["rajasthan"][0],
            "east": _p(1693441),
        }
        hero = region_heroes.get(india_region, FALLBACK_IMAGE)
        return [hero, FALLBACK_IMAGE]

    return [FALLBACK_IMAGE]
