"""Builder functions for RJ-003, RJ-004, RJ-006, RJ-008, and RJ-010 Rajasthan packages (no images)."""

from __future__ import annotations

from decimal import Decimal
from uuid import UUID

from schemas.itineraries import (
    ItineraryCreate,
    ItineraryDayNested,
    ItineraryHighlightNested,
    ItineraryHotelNested,
    ItineraryInclusionNested,
)
from schemas.packages import PackageCreate, PackageHighlightNested

RAJASTHAN_SLUG = "rajasthan"


def _day(
    day_number: int,
    title: str,
    description: str,
    activities: list[str],
    sort_order: int | None = None,
) -> ItineraryDayNested:
    return ItineraryDayNested(
        day_number=day_number,
        title=title,
        description=description,
        activities=activities,
        sort_order=sort_order if sort_order is not None else day_number,
    )


def _hotel(
    name: str,
    location: str,
    nights_label: str,
    category_label: str,
    room_type: str,
    meal_plan: str,
    stars: int,
    sort_order: int,
    description: str | None = None,
) -> ItineraryHotelNested:
    return ItineraryHotelNested(
        name=name,
        location=location,
        nights_label=nights_label,
        description=description or f"Option {sort_order:02d} — {category_label} tier handpicked property.",
        stars=stars,
        category_label=category_label,
        room_type=room_type,
        meal_plan=meal_plan,
        sort_order=sort_order,
    )


def _inc_included(text: str, sort_order: int) -> ItineraryInclusionNested:
    return ItineraryInclusionNested(kind="included", text=text, sort_order=sort_order)


def _inc_excluded(text: str, sort_order: int) -> ItineraryInclusionNested:
    return ItineraryInclusionNested(kind="excluded", text=text, sort_order=sort_order)


def _ih(text: str, sort_order: int) -> ItineraryHighlightNested:
    return ItineraryHighlightNested(text=text, sort_order=sort_order)


def _ph(text: str, sort_order: int) -> PackageHighlightNested:
    return PackageHighlightNested(text=text, sort_order=sort_order)


def _duration_days(duration_label: str) -> int:
    return int(duration_label.split("/")[-1].strip().split()[0])


def build_rj_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "RJ-003"
    tour_code = "TRAGUIN-RJ-003-DD"
    title = "Jodhpur Jaisalmer Desert Discovery"
    duration = "05 Nights / 06 Days"
    slug = "rj-003-jodhpur-jaisalmer-desert-discovery"
    itin_slug = "rj-003-jodhpur-jaisalmer-desert-discovery-itinerary"
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph("Serial RJ-003 | Tour code TRAGUIN-RJ-003-DD", 1),
            _ph("Jodhpur (2N) → Jaisalmer Desert (1N) → Jaisalmer City (2N)", 2),
            _ph("Family / Desert Discovery — MAPAI breakfast & dinner", 3),
            _ph("Sunset camel safari and folk dance at Sam Sand Dunes", 4),
            _ph("Mehrangarh Fort, Umaid Bhawan, Jaisalmer Living Fort", 5),
            _ph("TRAGUIN 24/7 digital concierge support", 6),
        ],
        moods=["Family", "Heritage", "Luxury", "Adventure"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Scale)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Jodhpur • Jaisalmer Desert • Jaisalmer City",
        overview=(
            "Embark on an extraordinary journey through the heart of the Thar Desert with this signature Desert "
            "Discovery itinerary. Tailored for discerning families, this bespoke circuit takes you from the striking "
            "Blue City of Jodhpur to the shimmering golden ramparts of Jaisalmer. Travel in complete luxury with a "
            "dedicated private premium vehicle, savor gourmet daily breakfasts and dinners, and indulge in exclusive "
            "local experiences carefully arranged by TRAGUIN. Route: Jodhpur (2N) → Sam Sand Dunes (1N) → Jaisalmer "
            "City (2N). Best season: October to March."
        ),
        seo_title="RJ-003 | Jodhpur Jaisalmer Desert Discovery | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Rajasthan family tour (RJ-003): Jodhpur, Sam Sand Dunes desert camp, "
            "Jaisalmer Living Fort, Patwon ki Haveli, and sunset camel safari."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Mehrangarh Fort & Umaid Bhawan Palace", 1),
            _ih("Sam Sand Dunes sunset camel safari", 2),
            _ih("Jaisalmer Living Fort (Sonar Qila)", 3),
            _ih("Patwon ki Haveli & Kuldhara Ghost Village", 4),
            _ih("TRAGUIN Signature rooftop dining experience", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Jodhpur | Welcome to the Blue City",
                "Traditional royal greeting at Jodhpur airport or railway station. Priority check-in at handpicked "
                "premium heritage hotel. Afternoon visit Jaswant Thada and Clock Tower local bazaars.",
                [
                    "Sightseeing Included: Jaswant Thada, Ghanta Ghar (Clock Tower) & Local Bazaars",
                    "Evening Experience: Leisured walk through traditional Spice Markets and heritage lanes",
                    "Overnight Stay: Premium Luxury Hotel / Heritage Resort in Jodhpur",
                    "Meals Included: Dinner",
                ],
            ),
            _day(
                2,
                "Jodhpur Sightseeing | Mighty Mehrangarh & Royal Legacies",
                "Full-day Jodhpur sightseeing at Mehrangarh Fort with expert guide, Sheesh Mahal, Phool Mahal, "
                "and Umaid Bhawan Palace Museum. Optional Flying Fox zipline adventure.",
                [
                    "Sightseeing Included: Mehrangarh Fort, Sheesh Mahal, Phool Mahal, Umaid Bhawan Palace Museum",
                    "Optional Activities: Thrilling Flying Fox (Zipline) adventure over Mehrangarh Fort",
                    "Evening Experience: Exclusive rooftop dinner overlooking illuminated Mehrangarh Fort",
                    "Overnight Stay: Premium Luxury Hotel / Heritage Resort in Jodhpur",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Jodhpur to Jaisalmer Desert | Journey to the Golden Sand Dunes",
                "Scenic drive to Sam Sand Dunes. Traditional welcome at luxury tented desert camp. Sunset camel "
                "safari with optional 4x4 jeep dune bashing. Evening folk dance and traditional dinner under stars.",
                [
                    "Sightseeing Included: Scenic drive through the Thar Desert, traditional rural desert vistas",
                    "Optional Activities: 4x4 Jeep Safari, Quad Biking, or Paramotoring over dunes",
                    "Evening Experience: Sunset camel ride, live folk dance, cultural music, and stargazing",
                    "Overnight Stay: Premium Luxury Desert Camp (AC Swiss Tents) at Sam Sand Dunes",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                4,
                "Jaisalmer Desert to Jaisalmer City | The Living Fort",
                "Desert sunrise, then transfer to Jaisalmer City. Explore Jaisalmer Fort (Sonar Qila), Patwon ki "
                "Haveli, Nathmal ki Haveli, and Salim Singh ki Haveli. Evening visit Gadisar Lake.",
                [
                    "Sightseeing Included: Jaisalmer Fort, Patwon ki Haveli, Nathmal ki Haveli, Salim Singh ki Haveli",
                    "Evening Experience: Scenic evening visit to Gadisar Lake surrounded by shrines",
                    "Overnight Stay: Premium Luxury Hotel / Palace Heritage Property in Jaisalmer",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                5,
                "Jaisalmer Heritage Exploration | Haunted Legends & Imperial Cenotaphs",
                "Visit Bada Bagh royal cenotaphs, Kuldhara Ghost Village, and Vyas Chhatri. Afternoon leisure for "
                "shopping Jaisalmer souvenirs — leather goods, sandstone carvings, and traditional jewelry.",
                [
                    "Sightseeing Included: Bada Bagh Cenotaphs, Kuldhara Ghost Village, Vyas Chhatri",
                    "Evening Experience: Relaxed sunset view at Vyas Chhatri",
                    "Overnight Stay: Premium Luxury Hotel / Palace Heritage Property in Jaisalmer",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                6,
                "Departure from Jaisalmer / Jodhpur | Bidding Farewell to Marwar",
                "Final breakfast and private transfer to Jaisalmer or Jodhpur airport/railway station for onward journey.",
                [
                    "Transfers Included: Private drop-off at Jaisalmer or Jodhpur Airport / Railway Station",
                    "Meals Included: Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("The Fern Residency", "Jodhpur", "2N Jodhpur", "Deluxe", "Executive Room", "MAPAI (Breakfast & Dinner)", 4, 1),
            _hotel("Desert Springs Resort", "Jaisalmer Desert", "1N Sam Dunes", "Deluxe", "AC Swiss Tent", "MAPAI (Breakfast & Dinner)", 4, 2),
            _hotel("Jaisalkot Resort", "Jaisalmer City", "2N Jaisalmer", "Deluxe", "Heritage Room", "MAPAI (Breakfast & Dinner)", 4, 3),
            _hotel("Ranbanka Palace", "Jodhpur", "2N Jodhpur", "Premium Heritage", "Heritage Room", "MAPAI (Breakfast & Dinner)", 4, 4),
            _hotel("Le Royal Camps", "Jaisalmer Desert", "1N Sam Dunes", "Premium", "Luxury Tent", "MAPAI (Breakfast & Dinner)", 4, 5),
            _hotel("Hotel Rawal Kot", "Jaisalmer City", "2N Jaisalmer", "Premium", "Deluxe Room", "MAPAI (Breakfast & Dinner)", 4, 6),
            _hotel("Radisson Jodhpur", "Jodhpur", "2N Jodhpur", "Luxury", "Superior Room", "MAPAI (Breakfast & Dinner)", 5, 7),
            _hotel("Serai Desert Camp", "Jaisalmer Desert", "1N Sam Dunes", "Luxury", "Luxury Tent", "MAPAI (Breakfast & Dinner)", 5, 8),
            _hotel("Suryagarh Jaisalmer", "Jaisalmer City", "2N Jaisalmer", "Luxury", "Fort Room", "MAPAI (Breakfast & Dinner)", 5, 9),
            _hotel("Umaid Bhawan Palace", "Jodhpur", "2N Jodhpur", "Ultra Luxury", "Palace Room", "MAPAI (Breakfast & Dinner)", 5, 10),
            _hotel("The Serai (Suján)", "Jaisalmer Desert", "1N Sam Dunes", "Ultra Luxury", "Luxury Tented Suite", "MAPAI (Breakfast & Dinner)", 5, 11),
            _hotel("Suryagarh (Bespoke Suite)", "Jaisalmer City", "2N Jaisalmer", "Ultra Luxury", "Bespoke Suite", "MAPAI (Breakfast & Dinner)", 5, 12),
        ],
        inclusions=[
            _inc_included("05 Nights stay in highly rated handpicked hotels and luxury desert camps", 1),
            _inc_included("Gourmet meal plan: daily breakfast and dinners throughout the trip", 2),
            _inc_included("Private air-conditioned premium vehicle for all transfers and sightseeing", 3),
            _inc_included("Sunset camel safari and evening cultural folk dance with traditional dinner buffet", 4),
            _inc_included("Traditional royal welcome greeting and personalized assistance upon arrival", 5),
            _inc_included("24/7 dedicated TRAGUIN digital concierge support, package taxes, and driver allowances", 6),
            _inc_excluded("Airfare / railfare to and from Jodhpur/Jaisalmer", 7),
            _inc_excluded("Monuments entry fees, camera fees for forts, palaces, and museums", 8),
            _inc_excluded("Optional adventure: ziplining, 4x4 jeep safari, quad biking, paramotoring", 9),
            _inc_excluded("Personal expenses: laundry, telephone, alcoholic drinks, tips, extra meals", 10),
            _inc_excluded("Comprehensive medical or trip cancellation travel insurance", 11),
        ],
    )
    return package, itinerary


def build_rj_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "RJ-004"
    tour_code = "TRAGUIN-RJ-004-UDAIPUR"
    title = "Udaipur Romance Luxury Tour"
    duration = "03 Nights / 04 Days"
    slug = "rj-004-udaipur-romance-luxury-tour"
    itin_slug = "rj-004-udaipur-romance-luxury-tour-itinerary"
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph("Serial RJ-004 | Tour code TRAGUIN-RJ-004-UDAIPUR", 1),
            _ph("Udaipur (3N) — Honeymoon / Luxury Romance circuit", 2),
            _ph("Private Lake Pichola sunset solar boat cruise", 3),
            _ph("City Palace, Monsoon Palace, Bagore-ki-Haveli cultural show", 4),
            _ph("CP plan with welcome drink and honeymoon amenities", 5),
            _ph("TRAGUIN 24/7 on-call backend concierge support", 6),
        ],
        moods=["Romantic", "Luxury", "Heritage"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Scale)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Udaipur Romance Tour — City of Lakes & Palaces",
        overview=(
            "Udaipur, acclaimed as the Venice of the East, is a mesmerizing oasis of white marble palaces, tranquil "
            "azure lakes, and breathtaking landscapes. This meticulously curated honeymoon package transforms your "
            "escape into a royal fairytale with premium handpicked hotels, private luxury transportation, and highly "
            "curated romantic experiences. Route: Udaipur arrival → Lake Pichola cruise → City Palace → Monsoon "
            "Palace → departure. Meal plan: CP (Bed & Breakfast). Best season: October to March."
        ),
        seo_title="RJ-004 | Udaipur Romance Luxury Tour | TRAGUIN",
        seo_description=(
            "Luxury 03 Nights / 04 Days Udaipur honeymoon (RJ-004): private Lake Pichola sunset cruise, City Palace, "
            "Saheliyon-ki-Bari, Sajjangarh Monsoon Palace, and Bagore-ki-Haveli folk show."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Private Lake Pichola sunset solar boat cruise", 1),
            _ih("City Palace & Crystal Gallery", 2),
            _ih("Sajjangarh Monsoon Palace panoramic views", 3),
            _ih("Bagore-ki-Haveli Rajasthani folk dance show", 4),
            _ih("TRAGUIN Signature twilight cruise with onboard musician", 5),
        ],
        days=[
            _day(
                1,
                "Udaipur Arrival | Royal Reception & Private Lake Pichola Sunset Cruise",
                "Private chauffeur welcome with cold towels and floral bouquet. Check-in at premium hotel. Exclusive "
                "private solar boat cruise on Lake Pichola past Lake Palace at sunset. Exquisite lakeside dinner.",
                [
                    "Sightseeing Included: Lake Pichola, Gangaur Ghat, Ambrai Viewpoint",
                    "Optional Activities: Couples' traditional aromatherapy spa session at the hotel",
                    "Evening Experience: Ultra-luxury lakeside dinner featuring authentic Mewari cuisine",
                    "Overnight Stay: Handpicked Premium Luxury Hotel / Resort in Udaipur",
                    "Meals Included: Welcome Drink & Breakfast",
                ],
            ),
            _day(
                2,
                "Udaipur Sightseeing | Monumental Romance & Grand City Palace",
                "Full-day Udaipur sightseeing with heritage guide: City Palace, Crystal Gallery, Saheliyon-ki-Bari, "
                "and Jagdish Temple. Romantic walk through old city markets.",
                [
                    "Sightseeing Included: City Palace, Crystal Gallery, Saheliyon-ki-Bari, Jagdish Temple",
                    "Optional Activities: Private professional vintage photoshoot in royal Mewari costumes",
                    "Evening Experience: Panoramic views and coffee at boutique cafe overlooking Fateh Sagar Lake",
                    "Overnight Stay: Handpicked Premium Luxury Hotel / Resort in Udaipur",
                    "Meals Included: Breakfast",
                ],
            ),
            _day(
                3,
                "Sajjangarh Palace & Culture | Monsoon Palace Vista & Mewari Cultural Show",
                "Visit Sajjangarh Monsoon Palace for sweeping lake views. Afternoon at Bagore-ki-Haveli for vibrant "
                "Rajasthani folk dance and puppet show. Romantic candlelight rooftop dinner.",
                [
                    "Sightseeing Included: Sajjangarh Monsoon Palace, Biological Park, Bagore-ki-Haveli",
                    "Optional Activities: Private pottery making workshop and rural art tour at Shilpgram",
                    "Evening Experience: Vibrant live cultural dance performance at Bagore-ki-Haveli",
                    "Overnight Stay: Handpicked Premium Luxury Hotel / Resort in Udaipur",
                    "Meals Included: Breakfast",
                ],
            ),
            _day(
                4,
                "Departure | Souvenir Collection & Cherished Farewell",
                "Leisurely breakfast, last-minute shopping at Bada Bazaar and Hathi Pol, and private transfer to "
                "Udaipur airport or railway station with customized farewell token.",
                [
                    "Sightseeing Included: Local craft emporiums and shopping bazaars (Bada Bazaar, Hathi Pol)",
                    "Optional Activities: Quick mid-day luxury high tea before heading to the terminal",
                    "Evening Experience: Flawless departure transfer assist",
                    "Meals Included: Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("Radisson Blu Udaipur Palace Resort", "Udaipur", "3N Udaipur", "Deluxe", "Superior Lake View Room", "CP (Breakfast)", 5, 1),
            _hotel("The Ananta Udaipur / Aurika Udaipur", "Udaipur", "3N Udaipur", "Premium", "Premium Valley View Room", "CP (Breakfast)", 5, 2),
            _hotel("The Leela Palace Udaipur / Taj Lake Palace", "Udaipur", "3N Udaipur", "Luxury", "Luxury Grand Heritage Room", "CP (Breakfast)", 5, 3),
            _hotel("The Oberoi Udaivilas", "Udaipur", "3N Udaipur", "Ultra Luxury", "Premier Room with Semi-Private Pool", "Gourmet CP (Breakfast)", 5, 4),
        ],
        inclusions=[
            _inc_included("Luxury accommodations at chosen handpicked tier hotels (3 nights)", 1),
            _inc_included("Daily buffet breakfast featuring international and local options", 2),
            _inc_included("Private luxury AC sedan for all transfers, excursions, and sightseeing", 3),
            _inc_included("Exclusive private sunset boat cruise on Lake Pichola curated by TRAGUIN", 4),
            _inc_included("Professional English-speaking local heritage guide for City Palace tour", 5),
            _inc_included("24/7 on-call backend concierge support from TRAGUIN", 6),
            _inc_included("Traditional welcome amenities, custom floral arrangements, and honeymoon cake", 7),
            _inc_included("All applicable state taxes, parking fees, toll fees, and driver allowances", 8),
            _inc_excluded("Domestic or international airfares / train tickets", 9),
            _inc_excluded("Monument entrance tickets and camera fees", 10),
            _inc_excluded("Mandatory dynamic gala dinners during Christmas, New Year, or peak festivals", 11),
            _inc_excluded("Personal expenses: laundry, mini-bar, telephone calls, and gratuities", 12),
            _inc_excluded("Optional adventure tours, premium water sports, or extra sightseeing trips", 13),
            _inc_excluded("Travel and medical insurance cover", 14),
        ],
    )
    return package, itinerary


def build_rj_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "RJ-006"
    tour_code = "TRAGUIN-RJ-006"
    title = "Rajasthan Palace Trail"
    duration = "07 Nights / 08 Days"
    slug = "rj-006-rajasthan-palace-trail"
    itin_slug = "rj-006-rajasthan-palace-trail-itinerary"
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph("Serial RJ-006 | Tour code TRAGUIN-RJ-006", 1),
            _ph("Jaipur (2N) → Jodhpur (2N) → Udaipur (3N) Grand Palace Circuit", 2),
            _ph("Luxury chauffeur SUV / executive sedan with CP breakfast plan", 3),
            _ph("Complimentary private sunset boat cruise on Lake Pichola", 4),
            _ph("Amber Fort, Mehrangarh Fort, Ranakpur Jain Temple", 5),
            _ph("TRAGUIN 24/7 dedicated concierge support", 6),
        ],
        moods=["Luxury", "Heritage", "Family", "Romantic"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Ultra Luxury Private)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Jaipur • Jodhpur • Udaipur — 07 Nights / 08 Days Ultra-Luxury Holiday",
        overview=(
            "The Best Rajasthan Tour Package welcomes you into a refined world of unmatched heritage hospitality, "
            "magnificent palace trails, and world-class architectural marvels. This bespoke circuit connects the Pink "
            "City of Jaipur, the imposing fortress landscapes of Jodhpur, and the peaceful romantic lakes of Udaipur. "
            "Private chauffeur-driven luxury vehicle, handpicked palace properties, and TRAGUIN signature hospitality "
            "throughout. Route: Jaipur → Jodhpur via Ajmer/Pushkar → Udaipur via Ranakpur → departure. Best season: "
            "October to March."
        ),
        seo_title="RJ-006 | Rajasthan Palace Trail | TRAGUIN",
        seo_description=(
            "Ultra-luxury 07 Nights / 08 Days Rajasthan palace trail (RJ-006): Jaipur, Jodhpur, Udaipur with Amber "
            "Fort, Mehrangarh Fort, Ranakpur Jain Temple, and Lake Pichola cruise."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Amber Fort & Hawa Mahal", 1),
            _ih("Mehrangarh Fort & Jaswant Thada", 2),
            _ih("Ranakpur Jain Temple (1,444 marble pillars)", 3),
            _ih("City Palace Udaipur & Lake Pichola cruise", 4),
            _ih("Sajjangarh Monsoon Palace panoramic views", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Jaipur | Royal Welcome to the Pink City",
                "Traditional royal welcome at Jaipur Airport. Transfer to handpicked luxury palace hotel. Evening walk "
                "through old city rose-pink bazaars.",
                [
                    "Sightseeing Included: Historic Old City Gates, Pink City Bazaars walk",
                    "Optional Activities: Royal culinary introduction dinner",
                    "Evening Experience: Leisure time at the luxury property gardens",
                    "Overnight Stay: Jaipur (Handpicked Heritage Palace)",
                ],
            ),
            _day(
                2,
                "Jaipur Full Day Sightseeing | Majestic Forts & Crown Jewels",
                "Amber Fort, Hawa Mahal photo stop, City Palace, Jantar Mantar UNESCO site, and Jal Mahal view.",
                [
                    "Sightseeing Included: Amber Fort, Hawa Mahal, City Palace, Jantar Mantar, Jal Mahal",
                    "Optional Activities: Exclusive private shopping tour for authentic jewelry and block prints",
                    "Evening Experience: Gourmet dinner at an award-winning fort restaurant",
                    "Overnight Stay: Jaipur Palace Hotel",
                ],
            ),
            _day(
                3,
                "Jaipur to Jodhpur via Ajmer/Pushkar | Scenic Highways & Sacred Faith Trails",
                "Scenic drive to Jodhpur with en-route stop at Ajmer Dargah or Pushkar Holy Lake and Brahma Temple.",
                [
                    "Sightseeing Included: Ajmer Dargah / Pushkar Holy Lake circuit",
                    "Optional Activities: Sunset camel rides on Pushkar's gentle desert dunes",
                    "Evening Experience: Relaxation by the hotel's heritage pool",
                    "Overnight Stay: Jodhpur (Premium Palace Stay)",
                ],
            ),
            _day(
                4,
                "Jodhpur Full Day Sightseeing | Mighty Mehrangarh Citadel",
                "Mehrangarh Fort, Jaswant Thada, Clock Tower, and Umaid Bhawan Museum. Walking tour through blue lanes.",
                [
                    "Sightseeing Included: Mehrangarh Fort, Jaswant Thada, Clock Tower, Umaid Bhawan Museum",
                    "Optional Activities: Adventurous zip-lining over the majestic fort battlements",
                    "Evening Experience: Romantic rooftop dinner overlooking illuminated fort walls",
                    "Overnight Stay: Jodhpur Heritage Resort",
                ],
            ),
            _day(
                5,
                "Jodhpur to Udaipur via Ranakpur | Exquisite Marble Sculptures",
                "En-route Ranakpur Jain Temple with 1,444 uniquely carved marble pillars. Arrive Udaipur lakeside hotel.",
                [
                    "Sightseeing Included: Ranakpur Jain Temple, Aravali Valley Drive",
                    "Optional Activities: Authentic Mewari lunch stop",
                    "Evening Experience: A peaceful lakeside walk at sunset",
                    "Overnight Stay: Udaipur (Premium Handpicked Hotel)",
                ],
            ),
            _day(
                6,
                "Udaipur Palace Tour & Lake Pichola Cruise | Grand Mewar Regality",
                "City Palace, Jagdish Temple, Saheliyon-ki-Bari, and private sunset boat cruise on Lake Pichola.",
                [
                    "Sightseeing Included: City Palace, Jagdish Temple, Saheliyon-ki-Bari, Lake Pichola Cruise",
                    "Optional Activities: Elegant evening folk dance show at Bagore Ki Haveli",
                    "Evening Experience: Fine dining at a spectacular lakeside restaurant",
                    "Overnight Stay: Udaipur Lakeside Palace",
                ],
            ),
            _day(
                7,
                "Udaipur Secondary Lakes & Hill Fort Excursion | Monsoon Palace Panoramas",
                "Sajjangarh Monsoon Palace, Fateh Sagar Lake, Nehru Park, and boutique lakeside cafés.",
                [
                    "Sightseeing Included: Sajjangarh Palace, Fateh Sagar Lake, Nehru Park",
                    "Optional Activities: Vintage Car Museum tour",
                    "Evening Experience: Custom couples' or family photography session",
                    "Overnight Stay: Udaipur Lakeside Palace",
                ],
            ),
            _day(
                8,
                "Udaipur Departure | Royal Farewell",
                "Relaxed breakfast, optional souvenir shopping, and smooth transfer to Udaipur Airport.",
                [
                    "Sightseeing Included: Souvenir stops and local handicraft markets",
                    "Meals Included: Premium Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("The Fern Residency", "Jaipur", "2N Jaipur", "Deluxe", "Executive Room", "CP (Breakfast)", 4, 1),
            _hotel("Fern Residency", "Jodhpur", "2N Jodhpur", "Deluxe", "Comfort Room", "CP (Breakfast)", 4, 2),
            _hotel("The Fern Residency", "Udaipur", "3N Udaipur", "Deluxe", "Lake View Room", "CP (Breakfast)", 4, 3),
            _hotel("Radisson Blu City Centre", "Jaipur", "2N Jaipur", "Premium", "Superior Room", "CP (Breakfast)", 5, 4),
            _hotel("Welcomhotel by ITC", "Jodhpur", "2N Jodhpur", "Premium", "Executive Room", "CP (Breakfast)", 5, 5),
            _hotel("Radisson Blu Palace", "Udaipur", "3N Udaipur", "Premium", "Palace Room", "CP (Breakfast)", 5, 6),
            _hotel("ITC Rajputana / Taj Jai Mahal", "Jaipur", "2N Jaipur", "Luxury", "Luxury Room", "CP (Breakfast)", 5, 7),
            _hotel("Taj Hari Mahal", "Jodhpur", "2N Jodhpur", "Luxury", "Deluxe Garden Room", "CP (Breakfast)", 5, 8),
            _hotel("The Leela Palace / Taj Lake Palace", "Udaipur", "3N Udaipur", "Luxury", "Grand Heritage View", "CP (Breakfast)", 5, 9),
            _hotel("Rambagh Palace", "Jaipur", "2N Jaipur", "Ultra Luxury", "Palace Room", "CP (Breakfast)", 5, 10),
            _hotel("Umaid Bhawan Palace", "Jodhpur", "2N Jodhpur", "Ultra Luxury", "Palace Room", "CP (Breakfast)", 5, 11),
            _hotel("The Oberoi Udaivilas", "Udaipur", "3N Udaipur", "Ultra Luxury", "Premier Room", "CP (Breakfast)", 5, 12),
        ],
        inclusions=[
            _inc_included("Luxury heritage palace accommodation across all cities", 1),
            _inc_included("Daily premium buffet breakfast options", 2),
            _inc_included("Private chauffeur-driven executive vehicle for all journeys", 3),
            _inc_included("All parking fees, highway tolls, and driver allowances", 4),
            _inc_included("Complimentary private sunset boat cruise on Lake Pichola", 5),
            _inc_included("Welcome amenities and traditional garland greetings", 6),
            _inc_included("24/7 dedicated TRAGUIN concierge support", 7),
            _inc_excluded("Airfares or interstate train ticket expenses", 8),
            _inc_excluded("Monument entry fees, camera fees, or local guide services", 9),
            _inc_excluded("Personal expenses: mini-bar, phone calls, laundry", 10),
            _inc_excluded("Optional adventure activities: zip-lining, desert safaris", 11),
            _inc_excluded("Mandatory gala dinner surcharges during holiday peaks", 12),
            _inc_excluded("Personal travel and medical insurance", 13),
        ],
    )
    return package, itinerary


def build_rj_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "RJ-008"
    tour_code = "TRAGUIN-RJ-008"
    title = "Rajasthan Royal Ladies Tour"
    duration = "05 Nights / 06 Days"
    slug = "rj-008-rajasthan-royal-ladies-tour"
    itin_slug = "rj-008-rajasthan-royal-ladies-tour-itinerary"
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph("Serial RJ-008 | Tour code TRAGUIN-RJ-008", 1),
            _ph("Jaipur (3N) → Pushkar (1N) → Jodhpur (1N) — Female Only Royal Ladies Tour", 2),
            _ph("Hands-on Anokhi block printing workshop with women artisans", 3),
            _ph("Sunset camel-cart desert safari with Kalbeliya dance", 4),
            _ph("Patrika Gate, Mehrangarh Fort, Pushkar Brahma Temple", 5),
            _ph("TRAGUIN 24/7 priority support and safety tracking", 6),
        ],
        moods=["Women", "Heritage", "Luxury", "Cultural"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Handpicked Luxury)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Jaipur • Pushkar • Jodhpur — 05 Nights / 06 Days of Sisterhood & Splendor",
        overview=(
            "An ultra-exclusive, luxurious celebration of sisterhood designed by TRAGUIN for women solo travelers, "
            "girlfriends, and mother-daughter duos. This female-only getaway features verified professional chauffeurs, "
            "handpicked hotels with top-tier hospitality, artisan workshops, and high-end shopping excursions. Route: "
            "Jaipur (3N) → Pushkar desert glamping (1N) → Jodhpur (1N). Meal plan: CP (Gourmet Buffet Breakfast). "
            "Best season: October to March."
        ),
        seo_title="RJ-008 | Rajasthan Royal Ladies Tour | TRAGUIN",
        seo_description=(
            "Female-only 05 Nights / 06 Days Rajasthan tour (RJ-008): Jaipur palaces, Anokhi block printing, Pushkar "
            "desert glamping, and Mehrangarh Fort with TRAGUIN safety support."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Amer Fort & Anokhi block printing workshop", 1),
            _ih("Patrika Gate & City Palace", 2),
            _ih("Pushkar Lake & Brahma Temple", 3),
            _ih("Sunset camel-cart safari with folk dance", 4),
            _ih("Mehrangarh Fort & Toorji Ka Jhalra Stepwell", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Jaipur | Royal Cocktails & High-Tea Welcome",
                "Traditional greeting with rose petals and mocktails. Transfer to luxury heritage hotel. Evening "
                "signature TRAGUIN royal welcome high-tea at restored haveli café with live sitar music.",
                [
                    "Sightseeing Included: Historic Old City Drive, Albert Hall Museum illumination exterior view",
                    "Optional Activities: Henna/Mehendi artwork session at the hotel courtyard",
                    "Evening Experience: Welcome high-tea with traditional live sitar music",
                    "Overnight Stay: Jaipur (Handpicked Luxury Heritage Hotel)",
                ],
            ),
            _day(
                2,
                "Jaipur Palace Exploration | Fortress Splendor & Block Printing",
                "Amer Fort and Sheesh Mahal, Jal Mahal photo stop. Exclusive hands-on block printing workshop at "
                "Anokhi artisan village with local women artisans.",
                [
                    "Sightseeing Included: Amer Fort, Jal Mahal, Hawa Mahal photography bay",
                    "Optional Activities: Professional royal styling and saree draping experience",
                    "Evening Experience: Private dining featuring authentic local Rajasthani delicacies",
                    "Overnight Stay: Jaipur Luxury Heritage Hotel",
                ],
            ),
            _day(
                3,
                "Jaipur's Secret Gems & Bazaars | Instagrammable Palaces & Jewelry Shopping",
                "Patrika Gate, City Palace royal rooms, Jantar Mantar. Guided shopping at Johari Bazar and Bapu Bazar.",
                [
                    "Sightseeing Included: Patrika Gate, City Palace Museum, Jantar Mantar",
                    "Optional Activities: Private jewelry curation consult with local experts",
                    "Evening Experience: Sunset cocktails at trendy rooftop café overlooking the city",
                    "Overnight Stay: Jaipur Luxury Heritage Hotel",
                ],
            ),
            _day(
                4,
                "Jaipur to Pushkar | Sacred Lakes, Desert Glamping & Sunset Camel Safari",
                "Drive to Pushkar. Walking tour of Pushkar Lake and Brahma Temple. Sunset camel-cart ride across "
                "desert dunes with Kalbeliya dance and starlit dinner.",
                [
                    "Sightseeing Included: Pushkar Lake Ghats, Brahma Temple, Thar Desert Dunes",
                    "Optional Activities: Private spiritual evening blessing ceremony at the ghats",
                    "Evening Experience: Live folk music, Kalbeliya dance, and starlit desert dinner",
                    "Overnight Stay: Pushkar (Premium Luxury Desert Resort)",
                ],
            ),
            _day(
                5,
                "Pushkar to Jodhpur | Blue City Bastions & Boutique Stepwell Cafés",
                "Optional morning yoga. Mehrangarh Fort, Jaswant Thada, and Toorji Ka Jhalra stepwell café. "
                "Special farewell dinner.",
                [
                    "Sightseeing Included: Mehrangarh Fort, Jaswant Thada, Toorji Ka Jhalra Stepwell",
                    "Optional Activities: Zip-lining over the majestic fort battlements",
                    "Evening Experience: Special farewell dinner to celebrate an unforgettable trip",
                    "Overnight Stay: Jodhpur (Premium Boutique Heritage Stay)",
                ],
            ),
            _day(
                6,
                "Jodhpur Departure | Farewell Royal Sisters",
                "Final breakfast, Clock Tower market souvenir shopping, and private transfer to Jodhpur Airport.",
                [
                    "Sightseeing Included: Clock Tower local market strolls",
                    "Meals Included: Premium Gourmet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("Mandawa Haveli", "Jaipur", "3N Jaipur", "Deluxe", "Heritage Room", "CP (Breakfast)", 4, 1),
            _hotel("Pushkar Resort", "Pushkar", "1N Pushkar", "Deluxe", "Desert Tent", "CP (Breakfast)", 4, 2),
            _hotel("The Fern Residency", "Jodhpur", "1N Jodhpur", "Deluxe", "Comfort Room", "CP (Breakfast)", 4, 3),
            _hotel("Shahpura House", "Jaipur", "3N Jaipur", "Premium", "Heritage Suite", "CP (Breakfast)", 4, 4),
            _hotel("Aaram Baagh Luxury", "Pushkar", "1N Pushkar", "Premium", "Luxury Tent", "CP (Breakfast)", 4, 5),
            _hotel("Welcomhotel by ITC", "Jodhpur", "1N Jodhpur", "Premium", "Executive Room", "CP (Breakfast)", 5, 6),
            _hotel("ITC Rajputana / Taj Mahal Palace", "Jaipur", "3N Jaipur", "Luxury", "Luxury Room", "CP (Breakfast)", 5, 7),
            _hotel("The Orchard Retreat", "Pushkar", "1N Pushkar", "Luxury", "Glamping Suite", "CP (Breakfast)", 5, 8),
            _hotel("Taj Hari Mahal Palace", "Jodhpur", "1N Jodhpur", "Luxury", "Deluxe Garden Room", "CP (Breakfast)", 5, 9),
            _hotel("The Raj Palace / Rambagh Palace", "Jaipur", "3N Jaipur", "Ultra Luxury", "Palace Room", "CP (Breakfast)", 5, 10),
            _hotel("Greenhouse Luxury Glamping", "Pushkar", "1N Pushkar", "Ultra Luxury", "Luxury Glamping Tent", "CP (Breakfast)", 5, 11),
            _hotel("Umaid Bhawan Palace Suite", "Jodhpur", "1N Jodhpur", "Ultra Luxury", "Palace Suite", "CP (Breakfast)", 5, 12),
        ],
        inclusions=[
            _inc_included("Bespoke luxury accommodations across premium properties", 1),
            _inc_included("Daily gourmet hot buffet breakfasts at all hotels", 2),
            _inc_included("Dedicated private luxury vehicle with expert chauffeur", 3),
            _inc_included("All road taxes, toll fees, fuel costs, and driver allowances", 4),
            _inc_included("Complimentary private high-tea experience on Day 1", 5),
            _inc_included("Hands-on block printing workshop admission fees", 6),
            _inc_included("Sunset camel-cart desert safari with live cultural dances", 7),
            _inc_included("24/7 priority support and safety tracking from TRAGUIN", 8),
            _inc_excluded("Domestic flight tickets or internal train bookings", 9),
            _inc_excluded("Standard monument entrance fees and camera licenses", 10),
            _inc_excluded("Personal laundry, tipping, and room service orders", 11),
            _inc_excluded("Optional activities like zip-lining or hot air ballooning", 12),
            _inc_excluded("Any meal options not explicitly mentioned in the itinerary", 13),
            _inc_excluded("Comprehensive personal travel insurance policies", 14),
        ],
    )
    return package, itinerary


def build_rj_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "RJ-010"
    tour_code = "TRAGUIN-RJ-010"
    title = "Premium Rajasthan Family Tour"
    duration = "06 Nights / 07 Days"
    slug = "rj-010-premium-rajasthan-family-tour"
    itin_slug = "rj-010-premium-rajasthan-family-tour-itinerary"
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph("Serial RJ-010 | Tour code TRAGUIN-RJ-010", 1),
            _ph("Jaipur (2N) → Jodhpur (2N) → Udaipur (2N) Imperial Family Circuit", 2),
            _ph("Spacious Innova Crysta MUV with family concierge support", 3),
            _ph("Chokhi Dhani ethnic village fair and Lake Pichola family cruise", 4),
            _ph("Bishnoi Village jeep safari and Ranakpur Jain Temple", 5),
            _ph("TRAGUIN 24/7 dedicated family concierge", 6),
        ],
        moods=["Family", "Heritage", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Custom)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Jaipur • Jodhpur • Udaipur — 06 Nights / 07 Days of Royal Grandeur",
        overview=(
            "A spectacular royal adventure for multi-generational families. This meticulously planned Rajasthan Family "
            "Tour balances immersive cultural experiences with absolute comfort for children and grandparents alike. "
            "Spacious dedicated Innova Crysta MUV, handpicked family-friendly hotels, Chokhi Dhani cultural night, "
            "Bishnoi village safari, and private Lake Pichola family cruise. Route: Jaipur (2N) → Jodhpur (2N) → "
            "Udaipur (2N). Meal plan: CP (Premium Family Buffet Breakfast). Best season: October to March."
        ),
        seo_title="RJ-010 | Premium Rajasthan Family Tour | TRAGUIN",
        seo_description=(
            "Premium 06 Nights / 07 Days Rajasthan family tour (RJ-010): Jaipur Chokhi Dhani, Mehrangarh Fort, "
            "Bishnoi village safari, Ranakpur Jain Temple, and Lake Pichola family cruise."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Chokhi Dhani ethnic village fair & dinner", 1),
            _ih("Amer Fort & City Palace Jaipur", 2),
            _ih("Mehrangarh Fort & Bishnoi Village Safari", 3),
            _ih("Ranakpur Jain Temple", 4),
            _ih("Lake Pichola private family boat cruise", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Jaipur | Traditional Greetings & Cultural Night",
                "Traditional royal greeting at Jaipur Airport. Evening drive past Albert Hall Museum and Chokhi Dhani "
                "ethnic village resort with folk dances, puppet shows, camel rides, and authentic dinner.",
                [
                    "Sightseeing Included: Albert Hall Museum Outer View, Chokhi Dhani Cultural Experience",
                    "Optional Activities: Pottery making and traditional family dress photography",
                    "Evening Experience: Immersive Rajasthani village fair and dinner",
                    "Overnight Stay: Jaipur (Handpicked Family Premium Hotel)",
                ],
            ),
            _day(
                2,
                "Jaipur Full-Day Sightseeing | Fortresses & Palace of Winds",
                "Amer Fort with Sheesh Mahal, Jal Mahal photo stop, City Palace, Jantar Mantar, and Hawa Mahal.",
                [
                    "Sightseeing Included: Amer Fort, Jal Mahal View, City Palace, Jantar Mantar, Hawa Mahal",
                    "Optional Activities: Private block-printing workshop for the family",
                    "Evening Experience: Shopping walk through Johari and Bapu Bazaars",
                    "Overnight Stay: Jaipur",
                ],
            ),
            _day(
                3,
                "Jaipur to Jodhpur | Majestic Blue City Arrival",
                "Scenic drive to Jodhpur with family-friendly refreshment stops. Evening relaxation with Mehrangarh "
                "Fort illuminated views from hotel.",
                [
                    "Sightseeing Included: Countryside landscape drive, heritage hotel exploration",
                    "Optional Activities: Traditional high tea featuring classic Marwari sweets",
                    "Evening Experience: Relaxed sit-down dinner on a panoramic rooftop terrace",
                    "Overnight Stay: Jodhpur (Premium Palace Hotel)",
                ],
            ),
            _day(
                4,
                "Jodhpur Heritage Sightseeing | Citadels of Power",
                "Mehrangarh Fort, Jaswant Thada, Umaid Bhawan outer view. Optional Bishnoi Village jeep safari.",
                [
                    "Sightseeing Included: Mehrangarh Fort, Jaswant Thada, Umaid Bhawan Palace Outer View",
                    "Optional Activities: Bishnoi Village Jeep Safari",
                    "Evening Experience: Walk past historic Clock Tower and Sadar Market",
                    "Overnight Stay: Jodhpur",
                ],
            ),
            _day(
                5,
                "Jodhpur to Udaipur via Ranakpur | Sacred Architecture",
                "En-route Ranakpur Jain Temple with 1,444 uniquely carved marble pillars. Check into Udaipur lakeside resort.",
                [
                    "Sightseeing Included: Ranakpur Jain Temple, Aravali Mountain Pass Drive",
                    "Optional Activities: Lunch stop featuring authentic local cuisine",
                    "Evening Experience: Relaxing lakeside walk at your resort",
                    "Overnight Stay: Udaipur (Premium Lakeside Resort)",
                ],
            ),
            _day(
                6,
                "Udaipur Full-Day Sightseeing | Lakeside City Palace & Cruise",
                "City Palace, Jagdish Temple, Saheliyon-ki-Bari, and private family boat cruise on Lake Pichola at sunset.",
                [
                    "Sightseeing Included: City Palace, Saheliyon-ki-Bari, Jagdish Temple, Lake Pichola Cruise",
                    "Optional Activities: Ropeway ride to Karni Mata Temple for panoramic views",
                    "Evening Experience: Folk dance show at historic Bagore Ki Haveli",
                    "Overnight Stay: Udaipur",
                ],
            ),
            _day(
                7,
                "Udaipur Sightseeing & Departure | Royal Farewell",
                "Final breakfast, souvenir shopping for local artwork and block-printed textiles, transfer to Udaipur Airport.",
                [
                    "Sightseeing Included: Souvenir stops and local market walks",
                    "Meals Included: Premium Family Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("The Fern Residency", "Jaipur", "2N Jaipur", "Deluxe", "Family Room", "CP (Breakfast)", 4, 1),
            _hotel("Fern Residency", "Jodhpur", "2N Jodhpur", "Deluxe", "Executive Room", "CP (Breakfast)", 4, 2),
            _hotel("The Fern Residency", "Udaipur", "2N Udaipur", "Deluxe", "Lake View Room", "CP (Breakfast)", 4, 3),
            _hotel("Radisson Blu Palace", "Jaipur", "2N Jaipur", "Premium", "Superior Room", "CP (Breakfast)", 5, 4),
            _hotel("Welcomhotel by ITC", "Jodhpur", "2N Jodhpur", "Premium", "Executive Room", "CP (Breakfast)", 5, 5),
            _hotel("Radisson Blu Udaipur", "Udaipur", "2N Udaipur", "Premium", "Palace Room", "CP (Breakfast)", 5, 6),
            _hotel("ITC Rajputana", "Jaipur", "2N Jaipur", "Luxury", "Luxury Room", "CP (Breakfast)", 5, 7),
            _hotel("Taj Hari Mahal", "Jodhpur", "2N Jodhpur", "Luxury", "Deluxe Garden Room", "CP (Breakfast)", 5, 8),
            _hotel("The Leela Palace", "Udaipur", "2N Udaipur", "Luxury", "Grand Heritage View", "CP (Breakfast)", 5, 9),
            _hotel("Rambagh Palace (Luxury Suite)", "Jaipur", "2N Jaipur", "Ultra Luxury", "Luxury Suite", "CP + Welcome Mix", 5, 10),
            _hotel("Umaid Bhawan Palace", "Jodhpur", "2N Jodhpur", "Ultra Luxury", "Palace Room", "CP + Welcome Mix", 5, 11),
            _hotel("Oberoi Udaivilas (Lake View)", "Udaipur", "2N Udaipur", "Ultra Luxury", "Lake View Room", "CP + Welcome Mix", 5, 12),
        ],
        inclusions=[
            _inc_included("Luxury family-friendly heritage palace/hotel stays", 1),
            _inc_included("Daily multi-cuisine buffet breakfasts with kids' options", 2),
            _inc_included("Private chauffeur-driven executive Innova Crysta vehicle", 3),
            _inc_included("All road taxes, parking fees, tolls, and driver allowances", 4),
            _inc_included("Complimentary private boat cruise for the family on Lake Pichola", 5),
            _inc_included("Chokhi Dhani ethnic village fair passes and dinner", 6),
            _inc_included("24/7 dedicated TRAGUIN family concierge support", 7),
            _inc_excluded("Domestic or international airfares/train bookings", 8),
            _inc_excluded("Monument entry tickets, camera fees, and local guide fees", 9),
            _inc_excluded("Personal laundry, telephone calls, or mini-bar charges", 10),
            _inc_excluded("Optional activities: Bishnoi village safari or ropeway rides", 11),
            _inc_excluded("Peak season surcharges for holiday gala dinners", 12),
            _inc_excluded("Personal travel and medical insurance", 13),
            _inc_excluded("Any items not explicitly listed under inclusions", 14),
        ],
    )
    return package, itinerary


RAJASTHAN_RJ_003_004_006_008_010_BUILDERS = [
    build_rj_003,
    build_rj_004,
    build_rj_006,
    build_rj_008,
    build_rj_010,
]
