"""Builder functions for JP-001 through JP-003 Japan packages (no images)."""

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


def build_jp_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="jp-001-japan-highlights-family-tour",
        destination_id=destination_id,
        title="Japan Highlights Family Tour",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=48,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Tokyo → Mt. Fuji → Kyoto → Osaka Golden Route family circuit", sort_order=1),
            PackageHighlightNested(text="Private sushi masterclass & TeamLab Planets skip-the-line", sort_order=2),
            PackageHighlightNested(text="First-class Shinkansen bullet train with luggage forwarding", sort_order=3),
            PackageHighlightNested(text="Fushimi Inari, Golden Pavilion & Dotonbori street food", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 bilingual family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-JPN-HIGHLIGHTS-2026 | Serial JP-001", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="jp-001-japan-highlights-itinerary",
        destination_id=destination_id,
        title="Japan Highlights Family Tour",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Premium Japan Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Tokyo • Mt. Fuji • Shinkansen • Kyoto • Osaka",
        overview=(
            "Step into a world where ancient traditions blend with ultra-futuristic innovations on TRAGUIN's curated "
            "family heritage expedition. Connecting Tokyo's neon high-rises, Kyoto's timeless shrines, and Osaka's "
            "culinary streets — with private executive vans, first-class Shinkansen, skip-the-line admissions, and "
            "24/7 bilingual concierge support."
        ),
        seo_title="JP-001 | Japan Highlights Family Tour | TRAGUIN",
        seo_description=(
            "Premium 06 Nights / 07 Days Japan family package (JP-001): Tokyo, Mt. Fuji, Hakone, Kyoto, "
            "Osaka, sushi masterclass, and Shinkansen bullet train."
        ),
        is_featured=True,
        featured_sort_order=48,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Shibuya Scramble & Senso-ji Temple", sort_order=1),
            ItineraryHighlightNested(text="Private Family Sushi Masterclass", sort_order=2),
            ItineraryHighlightNested(text="Mt. Fuji & Lake Ashi Cruise", sort_order=3),
            ItineraryHighlightNested(text="First-Class Shinkansen to Kyoto", sort_order=4),
            ItineraryHighlightNested(text="Fushimi Inari & Golden Pavilion", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Tokyo & Neon Initial Exploration", "Premium airport reception at Narita or Haneda. Private luxury van to central hotel. Evening orientation walk through Shinjuku or Shibuya and the famous Shibuya Scramble.", ["Sightseeing Included: VIP airport meet & greet, private luxury van transfer, Shibuya Scramble trail", "Evening Experience: Family welcome dinner at upscale Izakaya restaurant", "Overnight Stay: Tokyo City Centre (Premium Family-Friendly Luxury Hotel)", "Meals Included: Traditional Japanese Welcome Dinner"]),
            _day(2, "Historic Asakusa & Private Sushi Masterclass", "Visit Senso-ji Temple in Asakusa and Nakamise craft street. Private family sushi-making masterclass with expert Japanese chef. TeamLab Planets digital art experience.", ["Sightseeing Included: Senso-ji Temple guided tour, TeamLab Planets entry passes", "Special Curation: Private family sushi-making masterclass and premium lunch", "Overnight Stay: Tokyo City Centre (Premium Family-Friendly Luxury Hotel)", "Meals Included: International Breakfast & Private Masterclass Sushi Lunch"]),
            _day(3, "Mt. Fuji Spectacular Landscapes & Hakone Cruise", "Drive to Mt. Fuji Subaru 5th Station. Scenic cruise on Lake Ashi aboard historic pirate ship. TRAGUIN luggage forwarding to Kyoto.", ["Sightseeing Included: Mt. Fuji 5th Station, Lake Ashi cruise, Hakone Komagatake Ropeway", "Logistics Highlight: Hotel-to-hotel luggage forwarding to Kyoto", "Overnight Stay: Hakone Onsen Resort (Premium Ryokan with Private Hot Springs)", "Meals Included: International Breakfast & Traditional Kaiseki Dinner"]),
            _day(4, "Bullet Train Shinkansen Transit to Timeless Kyoto", "First-class Shinkansen bullet train to Kyoto. Afternoon walk through historic Gion district wooden tea houses.", ["Sightseeing Included: First-class Shinkansen ticket, Gion heritage district guided walk", "Overnight Stay: Kyoto Heritage Centre (Premium Luxury Hotel)", "Meals Included: International Breakfast & Gourmet Kyoto Bento Lunch"]),
            _day(5, "Kyoto Red Torii Gates & Golden Pavilion", "Early visit to Fushimi Inari Shrine's vermilion torii gates. Afternoon at Kinkaku-ji Golden Pavilion and Arashiyama Bamboo Grove.", ["Sightseeing Included: Fushimi Inari torii trail, Kinkaku-ji Golden Pavilion, Arashiyama Bamboo Grove", "Overnight Stay: Kyoto Heritage Centre (Premium Luxury Hotel)", "Meals Included: International Breakfast & Traditional Kyoto Cuisine Dinner"]),
            _day(6, "Osaka Castle Majesty & Dotonbori Street Gala", "Private van transfer to Osaka. Tour Osaka Castle. Evening street-food exploration through neon-lit Dotonbori with grand farewell dinner.", ["Sightseeing Included: Osaka Castle guided entry, Dotonbori culinary walking tour", "Evening Experience: Grand farewell family celebration dinner", "Overnight Stay: Osaka Bay / Centre (Premium Luxury Hotel)", "Meals Included: International Breakfast & Dotonbori Street-Food Farewell Feast"]),
            _day(7, "Seamless Airport Transit & Departure", "Final breakfast at premium hotel. Private luxury van to Kansai International Airport with luggage coordination.", ["Transfers Included: Private luxury van airport departure, luggage coordination", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Keio Plaza Hotel Tokyo / similar", location="Tokyo", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Hakone Yumoto Onsen / similar", location="Hakone", nights_label="01 Night", category_label="Deluxe", meal_plan="Breakfast & Kaiseki Dinner", stars=4, sort_order=2),
            ItineraryHotelNested(name="The Thousand Kyoto / Cross Osaka / similar", location="Kyoto / Osaka", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Cerulean Tower Tokyu Hotel", location="Tokyo", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="Hakone Kowakien Ten-yu", location="Hakone", nights_label="01 Night", category_label="Premium", meal_plan="Breakfast & Kaiseki Dinner", stars=5, sort_order=5),
            ItineraryHotelNested(name="Kyoto Tokyu Hotel / Swissotel Nankai", location="Kyoto / Osaka", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="The Capitol Hotel Tokyu", location="Tokyo", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Gora Kadan Ryokan", location="Hakone", nights_label="01 Night", category_label="Luxury", meal_plan="Breakfast & Kaiseki Dinner", stars=5, sort_order=8),
            ItineraryHotelNested(name="The Ritz-Carlton Kyoto / W Osaka", location="Kyoto / Osaka", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
            ItineraryHotelNested(name="Aman Tokyo / Palace Hotel", location="Tokyo", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
            ItineraryHotelNested(name="Hoshinoya Fuji / Gora Kadan", location="Hakone", nights_label="01 Night", category_label="Ultra Luxury", meal_plan="Breakfast & Kaiseki Dinner", stars=5, sort_order=11),
            ItineraryHotelNested(name="Aman Kyoto / St. Regis Osaka", location="Kyoto / Osaka", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=12),
        ],
        inclusions=_jp001_inclusions(),
    )
    return package, itinerary


def _jp001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="06 Nights in family-friendly premium luxury hotels or traditional Ryokan", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Daily breakfasts, traditional Kaiseki feast, and curated specialty dinners", sort_order=2),
        ItineraryInclusionNested(kind="included", text="First-class Shinkansen bullet train tickets from Hakone/Tokyo to Kyoto", sort_order=3),
        ItineraryInclusionNested(kind="included", text="TRAGUIN seamless hotel-to-hotel luggage forwarding (1 bag per person)", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Skip-the-line entries to TeamLab Planets, Kinkaku-ji, and major landmarks", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Private family sushi-making masterclass with expert Japanese chef", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 bilingual destination managers and guest assistance hotline", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International flight tickets and Japan entry visa processing fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar billing", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, or optional sightseeing not mentioned", sort_order=10),
    ]


def build_jp_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="jp-002-japan-family-expedition",
        destination_id=destination_id,
        title="Japan Family Expedition",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=49,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Tokyo (3N) → Osaka (2N) → Kyoto (2N) Golden Route explorer", sort_order=1),
            PackageHighlightNested(text="Universal Studios Japan express passes & Super Nintendo World", sort_order=2),
            PackageHighlightNested(text="Private sushi masterclass & Mt. Fuji Lake Ashi cruise", sort_order=3),
            PackageHighlightNested(text="First-class Shinkansen with TRAGUIN luggage forwarding", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 bilingual family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-JPN-FAMILY-2026 | Serial JP-002", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Adventure", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="jp-002-japan-family-expedition-itinerary",
        destination_id=destination_id,
        title="Japan Family Expedition",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Japan Family Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Tokyo • Mt. Fuji • Osaka Universal • Kyoto Shrines",
        overview=(
            "The ultimate multigenerational family journey through the Land of the Rising Sun. Connecting Tokyo's "
            "neon horizons, Osaka's Universal Studios thrills, and Kyoto's UNESCO heritage forests — with private "
            "luxury vans, first-class Shinkansen, luggage forwarding, and 24/7 bilingual support."
        ),
        seo_title="JP-002 | Japan Family Expedition | TRAGUIN",
        seo_description=(
            "Luxury 07 Nights / 08 Days Japan family package (JP-002): Tokyo, Mt. Fuji, Universal Studios Osaka, "
            "Kyoto shrines, sushi masterclass, and Shinkansen."
        ),
        is_featured=True,
        featured_sort_order=49,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Shibuya Scramble & Senso-ji Temple", sort_order=1),
            ItineraryHighlightNested(text="Private Sushi Masterclass & TeamLab Planets", sort_order=2),
            ItineraryHighlightNested(text="Mt. Fuji & Lake Ashi Pirate Ship Cruise", sort_order=3),
            ItineraryHighlightNested(text="Universal Studios Japan Express Passes", sort_order=4),
            ItineraryHighlightNested(text="Golden Pavilion & Fushimi Inari", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Tokyo & Shibuya Neon Cruise", "Premium airport reception. Private executive van to central hotel. Evening exploration of Shibuya neon pathways and Shibuya Scramble.", ["Sightseeing Included: VIP airport reception, private luxury van transit, Shibuya Scramble trail", "Evening Experience: Family welcome dinner at upscale traditional Japanese restaurant", "Overnight Stay: Tokyo City Centre (Premium Family Hotel)", "Meals Included: Traditional Japanese Welcome Dinner"]),
            _day(2, "Historic Asakusa & Private Sushi Masterclass", "Senso-ji Temple and Nakamise craft street. Private family sushi-making masterclass. Priority entry to teamLab Planets digital art maze.", ["Sightseeing Included: Senso-ji Temple guided tour, TeamLab Planets priority entry", "Special Curation: Private family sushi-making masterclass", "Overnight Stay: Tokyo City Centre (Premium Family Hotel)", "Meals Included: International Breakfast & Masterclass Sushi Lunch"]),
            _day(3, "Mt. Fuji Panoramic Landscapes & Lake Ashi Cruise", "Drive to Mt. Fuji Subaru 5th Station. Scenic Lake Ashi pirate ship cruise. TRAGUIN luggage forwarding from Tokyo to Osaka.", ["Sightseeing Included: Mt. Fuji 5th Station access, Lake Ashi pirate ship cruise", "Logistics Highlight: Luggage forwarding from Tokyo to Osaka", "Overnight Stay: Tokyo City Centre (Premium Family Hotel)", "Meals Included: International Breakfast & Casual Fuji-view Lunch"]),
            _day(4, "First-Class Bullet Train to Osaka", "First-class Shinkansen to Osaka. Evening exploration of Dotonbori neon canal walkways and Glico Man banner.", ["Sightseeing Included: First-class Shinkansen ticket, Dotonbori orientation walk", "Overnight Stay: Osaka Centre (Premium Family Hotel)", "Meals Included: International Breakfast & Dotonbori Street-Food Dinner"]),
            _day(5, "Universal Studios Japan Full-Day Immersion", "Full day at Universal Studios Japan with express passes. Super Nintendo World, Mario Kart, and Wizarding World of Harry Potter.", ["Sightseeing Included: Universal Studios Japan admission, express priority passes", "Overnight Stay: Osaka Centre (Premium Family Hotel)", "Meals Included: International Breakfast & Theme Park Dine-around Vouchers"]),
            _day(6, "Osaka Castle to the Bamboo Forests of Kyoto", "Osaka Castle park tour. Transfer to Kyoto. Walk through Arashiyama Bamboo Grove.", ["Sightseeing Included: Osaka Castle guided tour, Arashiyama Bamboo Grove trail", "Overnight Stay: Kyoto Heritage Centre (Premium Luxury Hotel)", "Meals Included: International Breakfast & Traditional Kyoto Cuisine Dinner"]),
            _day(7, "Golden Pavilion & Red Torii Pathways Gala", "Kinkaku-ji Golden Pavilion. Fushimi Inari Shrine torii gate trail. Grand farewell dinner with cultural performances.", ["Sightseeing Included: Kinkaku-ji entry, Fushimi Inari torii trail", "Evening Experience: Grand farewell family feast with cultural performances", "Overnight Stay: Kyoto Heritage Centre (Premium Luxury Hotel)", "Meals Included: International Breakfast & Grand Farewell Gala Dinner"]),
            _day(8, "High-End Transit & Kansai Departure", "Final luxurious breakfast. Private luxury van to Osaka Kansai International Airport with luggage coordination.", ["Transfers Included: Private luxury van airport departure, priority luggage coordination", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Keio Plaza Hotel Tokyo / similar", location="Tokyo", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Cross Hotel Osaka / similar", location="Osaka", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="The Thousand Kyoto / similar", location="Kyoto", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Cerulean Tower Tokyu", location="Tokyo", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="Swissotel Nankai Osaka", location="Osaka", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Kyoto Tokyu Hotel", location="Kyoto", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="The Capitol Hotel Tokyu", location="Tokyo", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="W Osaka", location="Osaka", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
            ItineraryHotelNested(name="The Ritz-Carlton Kyoto", location="Kyoto", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
            ItineraryHotelNested(name="Aman Tokyo / Palace Hotel", location="Tokyo", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
            ItineraryHotelNested(name="St. Regis Osaka", location="Osaka", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=11),
            ItineraryHotelNested(name="Aman Kyoto / Suiran Luxury Collection", location="Kyoto", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=12),
        ],
        inclusions=_jp002_inclusions(),
    )
    return package, itinerary


def _jp002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights in family-friendly premium luxury hotel rooms or suites", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Daily breakfast spreads and curated specialty fine dinners", sort_order=2),
        ItineraryInclusionNested(kind="included", text="First-class Shinkansen bullet train tickets from Tokyo to Osaka", sort_order=3),
        ItineraryInclusionNested(kind="included", text="TRAGUIN seamless hotel-to-hotel luggage forwarding (1 bag per person)", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Skip-the-line Universal Studios express, TeamLab Planets, and Golden Pavilion", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Private family sushi-making masterclass with expert Japanese chef", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 bilingual destination managers and guest assistance", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International flight tickets and Japan entry visa processing fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar billing", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, or optional sightseeing not mentioned", sort_order=10),
    ]


def build_jp_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="jp-003-romantic-japan-honeymoon",
        destination_id=destination_id,
        title="Romantic Japan Honeymoon",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=50,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Tokyo (2N) → Hakone Onsen (1N) → Kyoto (3N) → Osaka (1N) romantic circuit", sort_order=1),
            PackageHighlightNested(text="Private helicopter skyline cruise over Tokyo at sunset", sort_order=2),
            PackageHighlightNested(text="Luxury Ryokan private onsen & first-class Shinkansen", sort_order=3),
            PackageHighlightNested(text="Private tea ceremony, rickshaw & bamboo grove serenade", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 honeymoon concierge desk support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-JPN-ROMANCE-2026 | Serial JP-003", sort_order=6),
        ],
        moods=["Romantic", "Luxury", "Cultural", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="jp-003-romantic-japan-itinerary",
        destination_id=destination_id,
        title="Romantic Japan Honeymoon",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Honeymoon Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Tokyo • Mt. Fuji • Kyoto Bamboo • Osaka Twilight",
        overview=(
            "Begin your life together where timeless elegance meets the edge of tomorrow. TRAGUIN's romantic Japan "
            "escape weaves Michelin-tier dining, intimate volcanic hot-spring encounters, first-class Shinkansen, "
            "and quiet strolls through historical geisha districts — with private luxury vans and 24/7 bilingual support."
        ),
        seo_title="JP-003 | Romantic Japan Honeymoon | TRAGUIN",
        seo_description=(
            "Ultra-luxury 07 Nights / 08 Days Japan honeymoon (JP-003): Tokyo helicopter cruise, Hakone onsen, "
            "Kyoto tea ceremony, Golden Pavilion, and Dotonbori farewell."
        ),
        is_featured=True,
        featured_sort_order=50,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Private Helicopter Skyline Cruise", sort_order=1),
            ItineraryHighlightNested(text="Hakone Luxury Ryokan Private Onsen", sort_order=2),
            ItineraryHighlightNested(text="Private Rickshaw & Tea Ceremony", sort_order=3),
            ItineraryHighlightNested(text="Golden Pavilion & Fushimi Inari", sort_order=4),
            ItineraryHighlightNested(text="Dotonbori Neon Farewell Gala", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Tokyo & Helicopter Skyline Cruise", "Elite airport meet-and-greet. Private executive van to ultra-luxury hotel. Private helicopter flight over Tokyo at sunset with Tokyo Tower and Skytree views.", ["Sightseeing Included: VIP airport reception, private luxury van, private helicopter skyline cruise", "Honeymoon Touch: Chilled champagne and seasonal strawberries in suite", "Overnight Stay: Tokyo Center (Ultra-Luxury Sky-high Property)", "Meals Included: Waterfront Candlelight Welcome Dinner"]),
            _day(2, "Tokyo Art Insights & The TeamLab Maze", "Morning exploring Ginza boutiques. Priority skip-the-line entry to teamLab Planets immersive digital art experience.", ["Sightseeing Included: TeamLab Planets priority admission, Ginza fashion boulevard walk", "Overnight Stay: Tokyo Center (Ultra-Luxury Sky-high Property)", "Meals Included: International Breakfast & Intimate Sushi Fine-Dining Lunch"]),
            _day(3, "Mount Fuji Hideaway & Rejuvenating Hot Springs", "Scenic drive toward Mt. Fuji. Check into luxury Ryokan in Hakone with private outdoor onsen hot-spring bath. TRAGUIN luggage forwarding to Kyoto.", ["Sightseeing Included: Mt. Fuji scenic valley trail, private hot spring relaxation", "Logistics Highlight: Luggage forwarding from Tokyo to Kyoto", "Overnight Stay: Hakone (Elite Luxury Onsen Ryokan Resort)", "Meals Included: International Breakfast & Multi-course Kaiseki Feast"]),
            _day(4, "First-Class Bullet Train to Poetic Kyoto", "First-class Shinkansen to Kyoto. Intimate private guided evening walk through Gion geisha lanes and Shirakawa canal.", ["Sightseeing Included: First-class Shinkansen ticket, Gion heritage district evening walk", "Overnight Stay: Kyoto Riverside (Ultra-Luxury Boutique Palace Resort)", "Meals Included: International Breakfast & Traditional Kyoto Bistro Dinner"]),
            _day(5, "Private Temple Tea Ceremony & Bamboo Serenade", "Private rickshaw through Arashiyama Bamboo Grove at sunrise. Private Matcha Tea Ceremony hosted by expert master at hidden temple pavilion.", ["Sightseeing Included: Arashiyama Bamboo Grove rickshaw ride, private zen tea ceremony", "Overnight Stay: Kyoto Riverside (Ultra-Luxury Boutique Palace Resort)", "Meals Included: International Breakfast & Fine Dining Kaiseki Lunch"]),
            _day(6, "The Golden Pavilion & Crimson Torii Pathways", "Kinkaku-ji Golden Pavilion reflecting across mirror pond. Fushimi Inari Shrine vermilion torii gate mountain trail.", ["Sightseeing Included: Kinkaku-ji Golden Pavilion entry, Fushimi Inari torii trail", "Overnight Stay: Kyoto Riverside (Ultra-Luxury Boutique Palace Resort)", "Meals Included: International Breakfast & Premium Wagyu Beef Dinner"]),
            _day(7, "Transit to Dynamic Osaka & Neon Farewell Gala", "Osaka Castle park tour. Intimate culinary walking tour through Dotonbori neon canals. Grand honeymoon finale candlelight dinner.", ["Sightseeing Included: Osaka Castle guided tour, Dotonbori culinary trail", "Evening Experience: Grand honeymoon finale candlelight dinner", "Overnight Stay: Osaka Centre (Ultra-Luxury Modern Property)", "Meals Included: International Breakfast & Riverfront Gastronomy Farewell Dinner"]),
            _day(8, "High-End Resort Farewell & Departure", "Luxurious final breakfast. Private van to Osaka Kansai International Airport with luggage coordination.", ["Transfers Included: Private luxury van airport departure, priority luggage coordination", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Keio Plaza Hotel Tokyo / similar", location="Tokyo", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Hakone Yumoto Onsen / similar", location="Hakone", nights_label="01 Night", category_label="Deluxe", meal_plan="Breakfast & Kaiseki Dinner", stars=4, sort_order=2),
            ItineraryHotelNested(name="The Thousand Kyoto / Cross Osaka / similar", location="Kyoto / Osaka", nights_label="04 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Cerulean Tower Tokyu", location="Tokyo", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="Hakone Kowakien Ten-yu", location="Hakone", nights_label="01 Night", category_label="Premium", meal_plan="Breakfast & Kaiseki Dinner", stars=5, sort_order=5),
            ItineraryHotelNested(name="Kyoto Tokyu Hotel / Swissotel Nankai", location="Kyoto / Osaka", nights_label="04 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="The Capitol Hotel Tokyu", location="Tokyo", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Gora Kadan Ryokan", location="Hakone", nights_label="01 Night", category_label="Luxury", meal_plan="Breakfast & Kaiseki Dinner", stars=5, sort_order=8),
            ItineraryHotelNested(name="The Ritz-Carlton Kyoto / W Osaka", location="Kyoto / Osaka", nights_label="04 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
            ItineraryHotelNested(name="Aman Tokyo / Palace Hotel", location="Tokyo", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
            ItineraryHotelNested(name="Hoshinoya Fuji / Gora Kadan", location="Hakone", nights_label="01 Night", category_label="Ultra Luxury", meal_plan="Breakfast & Kaiseki Dinner", stars=5, sort_order=11),
            ItineraryHotelNested(name="Aman Kyoto / St. Regis Osaka", location="Kyoto / Osaka", nights_label="04 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=12),
        ],
        inclusions=_jp003_inclusions(),
    )
    return package, itinerary


def _jp003_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights in ultra-luxury honeymoon suites across Tokyo, Hakone, Kyoto, and Osaka", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Complimentary chilled champagne, seasonal strawberries, and floral arrangements on arrival", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private helicopter skyline cruise over Tokyo landmarks", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Private luxury executive van and first-class Shinkansen transits", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN seamless hotel-to-hotel luggage forwarding (1 bag per person)", sort_order=5),
        ItineraryInclusionNested(kind="included", text="VIP skip-the-line entries and private tea ceremony with zen master", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 honeymoon concierge desk support", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International flight tickets and Japan entry visa processing fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar billing", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, or extra sightseeing not specified", sort_order=10),
    ]


JP_BUILDERS = [
    build_jp_001,
    build_jp_002,
    build_jp_003,
]
