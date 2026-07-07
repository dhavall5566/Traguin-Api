"""Hand-curated hotel tier data extracted from GA PDF sources."""

from __future__ import annotations


def _h(
    sort_order: int,
    category: str,
    name: str,
    location: str,
    nights_label: str,
    room_type: str,
    meal_plan: str,
    stars: int = 4,
) -> dict:
    desc = (
        f"OPTION {sort_order:02d} – {category.upper()}: "
        f"{name.replace(' | ', ' (') if ' | ' not in name else name} ({location}) | {meal_plan}"
    )
    if " | " in name:
        parts = [p.strip() for p in name.split(" | ")]
        loc_parts = [p.strip() for p in location.split(" / ")]
        desc_parts = []
        for i, part in enumerate(parts):
            loc_bit = loc_parts[i] if i < len(loc_parts) else location
            desc_parts.append(f"{part} ({loc_bit})")
        desc = f"OPTION {sort_order:02d} – {category.upper()}: {' | '.join(desc_parts)} | {meal_plan}"
    return {
        "sort_order": sort_order,
        "category": category,
        "name": name,
        "location": location,
        "nights_label": nights_label,
        "room_type": room_type,
        "meal_plan": meal_plan,
        "stars": stars,
        "description": desc,
    }


GOA_HOTELS: dict[str, list[dict]] = {
    "GA-001": [
        _h(1, "Deluxe", "Lemon Tree Amarante Beach Resort / Similar", "Goa (3 Nights)", "03 Nights", "Superior Room", "CP (Breakfast)"),
        _h(2, "Premium", "Novotel Goa Resort & Spa / Similar", "Goa (3 Nights)", "03 Nights", "Luxury Room", "CP (Breakfast)"),
        _h(3, "Luxury", "Taj Fort Aguada Resort & Spa / Taj Holiday Village", "Goa (3 Nights)", "03 Nights", "Premium Sea View Cottage", "CP (Breakfast)", 5),
        _h(4, "Ultra Luxury", "The Leela Goa / W Goa (Vagator)", "Goa (3 Nights)", "03 Nights", "Luxury Lagoon Suite / Marvelous Chalet", "CP + Welcome Mix", 5),
    ],
    "GA-002": [
        _h(1, "Deluxe", "Lemon Tree Amarante Beach Resort | Heritage Village Resort & Spa", "North Goa (2 Nights) / South Goa (2 Nights)", "04 Nights", "Deluxe Room", "CP (Breakfast)"),
        _h(2, "Premium", "Novotel Goa Resort & Spa | Caravela Beach Resort", "North Goa (2 Nights) / South Goa (2 Nights)", "04 Nights", "Premium Room", "CP (Breakfast)"),
        _h(3, "Luxury", "Taj Holiday Village Resort & Spa | The Leela Goa (Lagoon Suite)", "North Goa (2 Nights) / South Goa (2 Nights)", "04 Nights", "Luxury Villa / Suite", "CP (Breakfast)", 5),
        _h(4, "Ultra Luxury", "W Goa (Marvelous Suite) | Taj Exotica Resort & Spa (Sea Villa)", "North Goa (2 Nights) / South Goa (2 Nights)", "04 Nights", "Ultra Luxury Sea Facing", "CP + Welcome Mix", 5),
    ],
    "GA-003": [
        _h(1, "Deluxe", "Lemon Tree Amarante Beach Resort / Hard Rock Hotel Goa", "North Goa (3 Nights)", "03 Nights", "Superior Deluxe Room", "CP (Includes Breakfast)"),
        _h(2, "Premium", "Novotel Goa Resort & Spa / Fairfield by Marriott Anjuna", "North Goa (3 Nights)", "03 Nights", "Premium Balcony Room", "CP (Includes Breakfast)"),
        _h(3, "Luxury", "W Goa (Vagator) / Taj Holiday Village Resort & Spa", "North Goa (3 Nights)", "03 Nights", "Wonderful Room / Luxury Cottage", "CP (Includes Breakfast)", 5),
        _h(4, "Ultra Luxury", "The Leela Goa (Club Suites) / Taj Exotica Resort & Spa", "North Goa (3 Nights)", "03 Nights", "Private Plunge Pool Villa", "CP + Welcome Champagne", 5),
    ],
    "GA-004": [
        _h(1, "Deluxe", "Caravela Beach Resort / ITC Grand Goa (Garden view)", "South Goa (5 Nights)", "05 Nights", "Superior Garden Room", "CP (Breakfast)"),
        _h(2, "Premium", "The Leela Goa / Alila Diwa Goa", "South Goa (5 Nights)", "05 Nights", "Premier Garden View Room", "CP (Breakfast)"),
        _h(3, "Luxury", "Taj Exotica Resort & Spa, Goa", "South Goa (5 Nights)", "05 Nights", "Luxury Ocean View Room", "CP (Breakfast)", 5),
        _h(4, "Ultra Luxury", "The Leela Goa (The Club Sanctuaries) / Taj Exotica (Plunge Pool Villa)", "South Goa (5 Nights)", "05 Nights", "Exclusive Club Suite / Luxury Villa", "CP + Private Butler", 5),
    ],
    "GA-005": [
        _h(1, "Deluxe", "Heritage Village Resort & Spa, South Goa", "South Goa (4 Nights)", "04 Nights", "Superior Garden View Room", "Breakfast & Dinner (MAP)"),
        _h(2, "Premium", "ITC Grand Goa, a Luxury Collection Resort", "South Goa (4 Nights)", "04 Nights", "Garden View Room with Balcony", "Breakfast & Dinner (MAP)"),
        _h(3, "Luxury", "The Leela Goa, Cavelossim", "South Goa (4 Nights)", "04 Nights", "Lagoon Terrace Suite", "Premium Curated Breakfast & Dinner", 5),
        _h(4, "Ultra Luxury", "Taj Exotica Resort & Spa, Benaulim", "South Goa (4 Nights)", "04 Nights", "Luxury Plunge Pool Villa", "Bespoke Personalized Dining Plan", 5),
    ],
    "GA-006": [
        _h(1, "Deluxe", "Novotel Goa Candolim / Fairfield by Marriott / similar", "North Goa (3 Nights)", "03 Nights", "Superior Garden View Room", "MAPAI (Breakfast & Dinner)"),
        _h(2, "Premium", "DoubleTree by Hilton Panaji / Hyatt Centric Candolim", "North Goa (3 Nights)", "03 Nights", "Premium Pool View Balcony Room", "MAPAI (Breakfast & Dinner)"),
        _h(3, "Luxury", "Taj Fort Aguada Resort & Spa / W Goa (Vagator)", "North Goa (3 Nights)", "03 Nights", "Luxury Sea View Room", "Bespoke MAPAI Plan", 5),
        _h(4, "Ultra Luxury", "The Leela Goa / Taj Exotica Resort & Spa (Benaulim)", "North Goa (3 Nights)", "03 Nights", "Private Luxury Plunge Pool Villa Suite", "VVIP Custom Dining Plan", 5),
    ],
    "GA-007": [
        _h(1, "Deluxe", "Lemon Tree Amarante / Novotel Candolim | Heritage Village Resort / similar", "North Goa (2 Nights) / South Goa (2 Nights)", "04 Nights", "Deluxe Room", "MAPAI (Breakfast & Dinner)"),
        _h(2, "Premium", "Hard Rock Hotel / DoubleTree by Hilton | Kenilworth Resort & Spa / Caravela Beach", "North Goa (2 Nights) / South Goa (2 Nights)", "04 Nights", "Premium Room", "MAPAI (Breakfast & Dinner)"),
        _h(3, "Luxury", "Taj Holiday Village / W Goa | Taj Exotica Resort & Spa / Alila Diwa", "North Goa (2 Nights) / South Goa (2 Nights)", "04 Nights", "Luxury Suite", "MAPAI + Premium Amenities", 5),
        _h(4, "Ultra Luxury", "The St. Regis Goa Resort (Sea View Suite) | The Leela Goa (The Club Pool Suite)", "North Goa (2 Nights) / South Goa (2 Nights)", "04 Nights", "VVIP Suite", "Bespoke Signature VIP Plan", 5),
    ],
    "GA-008": [
        _h(1, "Deluxe", "Novotel Goa Resort & Spa / Lemon Tree Amarante", "Goa (5 Nights)", "05 Nights", "Superior Garden View Room", "MAPAI (Breakfast & Dinner)"),
        _h(2, "Premium", "Grand Hyatt Goa / Caravela Beach Resort", "Goa (5 Nights)", "05 Nights", "Premium Balcony Sea View", "MAPAI (Breakfast & Dinner)"),
        _h(3, "Luxury", "Taj Exotica Resort & Spa / The Leela Goa", "Goa (5 Nights)", "05 Nights", "Luxury Pavilion Room", "MAPAI + Welcome Premium Kit", 5),
        _h(4, "Ultra Luxury", "ITC Grand Goa Resort / W Goa (Villas)", "Goa (5 Nights)", "05 Nights", "Private Plunge Pool VVIP Villa", "Bespoke Gourmet Custom Plan", 5),
    ],
    "GA-009": [
        _h(1, "Deluxe", "Novotel Goa Candolim / similar | Panjim Inn Heritage / similar | Kenilworth Resort & Spa / similar", "North Goa (3 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)", "07 Nights", "Deluxe Room", "MAPAI (Breakfast & Dinner)"),
        _h(2, "Premium", "Taj Holiday Village / Vivanta Candolim | WelcomHeritage Panjim Pousada | The Leela Goa (Lagoon Suite)", "North Goa (3 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)", "07 Nights", "Premium Room", "MAPAI (Breakfast & Dinner)"),
        _h(3, "Luxury", "W Goa (Wonderful Room) / Taj Fort Aguada | Boutique Heritage Villa Mansion | Taj Exotica Resort & Spa (Villa)", "North Goa (3 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)", "07 Nights", "Luxury Villa / Suite", "MAPAI (Breakfast & Dinner)", 5),
        _h(4, "Ultra Luxury", "St. Regis Goa Resort (Presidential) | Private Exclusive VVIP Heritage Estate | The Leela Goa (Royal Villa Suite)", "North Goa (3 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)", "07 Nights", "VVIP Villa Suite", "Elite Custom Luxury Dining Plan", 5),
    ],
    "GA-010": [
        _h(1, "Deluxe", "Novotel Resort & Spa / Lemon Tree Amarante | Kenilworth Resort / Heritage Village", "North Goa (5 Nights) / South Goa (4 Nights)", "09 Nights", "Deluxe Room", "MAPAI (Breakfast & Dinner)"),
        _h(2, "Premium", "Hard Rock Hotel / Vivanta Goa Candolim | Caravela Beach Resort / Radisson Blu", "North Goa (5 Nights) / South Goa (4 Nights)", "09 Nights", "Premium Room", "MAPAI Plan Portfolio"),
        _h(3, "Luxury", "The O Hotel / W Goa (Wonderful Room) | Taj Exotica Resort & Spa (Luxury Room)", "North Goa (5 Nights) / South Goa (4 Nights)", "09 Nights", "Luxury Room", "Bespoke MAPAI Plan Spread", 5),
        _h(4, "Ultra Luxury", "The Leela Goa (Lagoon Suite) | The St. Regis Goa Resort (VVIP Ocean Villa)", "North Goa (5 Nights) / South Goa (4 Nights)", "09 Nights", "VVIP Ocean Villa", "Elite Custom Luxury Dining Plan", 5),
    ],
    "GA-012": [
        _h(1, "Deluxe", "Lemon Tree Amarante / similar | Heritage Village Resort / similar", "North Goa (2 Nights) / South Goa (2 Nights)", "04 Nights", "Deluxe Room", "CP (Breakfast Only)"),
        _h(2, "Premium", "Novotel Goa Resort & Spa / similar | Caravela Beach Resort / similar", "North Goa (2 Nights) / South Goa (2 Nights)", "04 Nights", "Premium Room", "MAPAI (Breakfast & Dinner)"),
        _h(3, "Luxury", "Taj Holiday Village / W Goa | The Leela Goa / Taj Exotica", "North Goa (2 Nights) / South Goa (2 Nights)", "04 Nights", "Luxury Suite", "MAPAI + Honeymoon Kit", 5),
        _h(4, "Ultra Luxury", "Taj Fort Aguada (Hermitage Villa) | The Leela Goa (Royal Villa Suite)", "North Goa (2 Nights) / South Goa (2 Nights)", "04 Nights", "Royal Villa Suite", "VVIP Custom Meal Curator Plan", 5),
    ],
    "GA-013": [
        _h(1, "Deluxe", "Novotel Goa Resort & Spa / similar | Caravela Beach Resort / similar", "North Goa (3 Nights) / South Goa (2 Nights)", "05 Nights", "Superior Garden View Room", "CP (Breakfast)"),
        _h(2, "Premium", "Taj Holiday Village Resort & Spa | Taj Exotica Resort & Spa Goa", "North Goa (3 Nights) / South Goa (2 Nights)", "05 Nights", "Premium Private Balcony Room", "MAPAI (Breakfast & Dinner)"),
        _h(3, "Luxury", "W Goa / Alila Diwa Goa | The Leela Goa (Riverside)", "North Goa (3 Nights) / South Goa (2 Nights)", "05 Nights", "Luxury Ocean Sea-Facing Suite", "MAPAI + Honeymoon Kit", 5),
        _h(4, "Ultra Luxury", "The Cape Goa / Taj Fort Aguada (Villa) | The St. Regis Goa Resort", "North Goa (3 Nights) / South Goa (2 Nights)", "05 Nights", "VVIP Private Plunge Pool Sea Villa", "VVIP Custom Meal Curator Plan", 5),
    ],
    "GA-014": [
        _h(1, "Deluxe", "Novotel Goa Resort & Spa / similar | Kenilworth Resort / similar", "North Goa (3 Nights) / South Goa (1 Night)", "04 Nights", "Superior Garden View Room", "CP (Breakfast)"),
        _h(2, "Premium", "The O Resort & Spa / Hilton Goa | Caravela Beach Resort / similar", "North Goa (3 Nights) / South Goa (1 Night)", "04 Nights", "Premium Pool Access / Balcony Room", "MAPAI (Breakfast & Dinner)"),
        _h(3, "Luxury", "W Goa (Vagator) / Taj Holiday Village | Taj Exotica Resort & Spa Goa", "North Goa (3 Nights) / South Goa (1 Night)", "04 Nights", "Luxury Ocean Sea View Suite", "MAPAI (Breakfast & Dinner)", 5),
        _h(4, "Ultra Luxury", "The Leela Goa (The Club Suites) | Ahilya by the Sea (Private Villa)", "North Goa (3 Nights) / South Goa (1 Night)", "04 Nights", "VVIP Custom Private Luxury Pool Villa", "VVIP Custom Dining Plan", 5),
    ],
    "GA-015": [
        _h(1, "Deluxe", "Fortune Miramar / Vivanta Panaji / similar", "Heritage & Central Goa (4 Nights)", "04 Nights", "Superior Pool View Room", "MAPAI (Breakfast & Dinner)"),
        _h(2, "Premium", "Cidade de Goa - IHCL SeleQtions / similar", "Heritage & Central Goa (4 Nights)", "04 Nights", "Premium Sea View Room", "MAPAI (Breakfast & Dinner)"),
        _h(3, "Luxury", "Taj Resort & Convention Centre Goa / similar", "Heritage & Central Goa (4 Nights)", "04 Nights", "Luxury Heritage Balcony Suite", "MAPAI (Breakfast & Dinner)", 5),
        _h(4, "Ultra Luxury", "The Leela Goa / Taj Exotica Resort & Spa", "Heritage & Central Goa (4 Nights)", "04 Nights", "VVIP Private Royal Lagoon Villa", "Bespoke Personalized Dining Plan", 5),
    ],
    "GA-016": [
        _h(1, "Deluxe", "Novotel Goa Resort & Spa | Welcomheritage Panjim Inn | The Lalit Golf & Beach Resort", "North Goa (4 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)", "08 Nights", "Deluxe Room", "MAPAI (Breakfast & Dinner)"),
        _h(2, "Premium", "W Goa (Wonderful Room) | Cidade de Goa IHCL SeleQtions | Alila Diwa Goa (Heritage Room)", "North Goa (4 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)", "08 Nights", "Premium Room", "MAPAI (Breakfast & Dinner)"),
        _h(3, "Luxury", "Taj Holiday Village / Taj Fort Aguada | The Postcard Hideaway Netravali | The Leela Goa (Lagoon Suite)", "North Goa (4 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)", "08 Nights", "Luxury Suite", "MAPAI + Premium Amenities", 5),
        _h(4, "Ultra Luxury", "Taj Exotica Resort (Plunge Pool Villa) | The Postcard Moira (Royal Suite) | The Leela Goa (Royal Villa)", "North Goa (4 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)", "08 Nights", "Royal Villa", "Bespoke Gourmet Custom Plan", 5),
    ],
    "GA-017": [
        _h(1, "Deluxe", "Novotel Resort & Spa / similar | Dudhsagar Spa Resort / similar | Caravela Beach Resort / similar", "North Goa (2 Nights) / Mollem-Ponda (1 Night) / South Goa (4 Nights)", "07 Nights", "Deluxe Room", "MAPAI (Breakfast & Dinner)"),
        _h(2, "Premium", "Hard Rock Hotel / Vivanta Vagator | Nature's Nest Eco Lodge | Radisson Blu Resort South Goa", "North Goa (2 Nights) / Mollem-Ponda (1 Night) / South Goa (4 Nights)", "07 Nights", "Premium Room", "MAPAI (Breakfast & Dinner)"),
        _h(3, "Luxury", "W Goa / Taj Holiday Village | Stone Water Eco Resort Stay | The Leela Goa / Taj Exotica Goa", "North Goa (2 Nights) / Mollem-Ponda (1 Night) / South Goa (4 Nights)", "07 Nights", "Luxury Suite", "MAPAI + Premium Amenities", 5),
        _h(4, "Ultra Luxury", "The St. Regis Goa Resort (Suite) | Bespoke Wild Eco Luxury Villa | The St. Regis Goa Resort (Pool Villa)", "North Goa (2 Nights) / Mollem-Ponda (1 Night) / South Goa (4 Nights)", "07 Nights", "Pool Villa", "Bespoke Signature VIP Plan", 5),
    ],
    "GA-018": [
        _h(1, "Deluxe", "Taj Fort Aguada Beach Resort | Kenilworth Resort & Spa / similar", "North Goa (3 Nights) / South Goa (3 Nights)", "06 Nights", "Deluxe Room", "CP (Breakfast)"),
        _h(2, "Premium", "Taj Holiday Village Resort & Spa | The Leela Goa (Lagoon Suite)", "North Goa (3 Nights) / South Goa (3 Nights)", "06 Nights", "Premium Room", "CP (Breakfast)"),
        _h(3, "Luxury", "Taj Cidade de Goa Heritage / Resort | Taj Exotica Resort & Spa (Luxury Villa)", "North Goa (3 Nights) / South Goa (3 Nights)", "06 Nights", "Luxury Villa", "CP + Honeymoon Amenities", 5),
        _h(4, "Ultra Luxury", "The St. Regis Goa Resort / Villa Tier | Taj Exotica (Plunge Pool Private Villa)", "North Goa (3 Nights) / South Goa (3 Nights)", "06 Nights", "Plunge Pool Private Villa", "VVIP Concierge & Butler Plan", 5),
    ],
    "GA-019": [
        _h(1, "Deluxe", "Taj Resort & Convention Centre / Cidade de Goa", "Goa (5 Nights)", "05 Nights", "Premium Sea View Room", "MAPAI (Breakfast & Dinner)"),
        _h(2, "Premium", "W Goa (Vagator) / Heritage Village Resort", "Goa (5 Nights)", "05 Nights", "Wonderful Room / Private Chalet", "MAPAI (Breakfast & Dinner)"),
        _h(3, "Luxury", "The Leela Goa / Taj Exotica Resort & Spa", "Goa (5 Nights)", "05 Nights", "Luxury Conservatory Premier Suite", "Bespoke Gourmet MAPAI Plan", 5),
        _h(4, "Ultra Luxury", "TRAGUIN Private Elite Villa Collection (Assagao/Candolim)", "Goa (5 Nights)", "05 Nights", "Exclusive 4/5 BHK Private Pool Villa Estate", "VVIP Private Chef & Dining Plan", 5),
    ],
    "GA-020": [
        _h(1, "Deluxe", "Novotel Goa Resort & Spa / Fairfield by Marriott", "Goa (3 Nights)", "03 Nights", "Superior Garden View Room", "Ultra Luxury All-Inclusive Plan"),
        _h(2, "Premium", "Grand Hyatt Goa / W Goa / similar", "Goa (3 Nights)", "03 Nights", "Premium Pool View Room", "Ultra Luxury All-Inclusive Plan"),
        _h(3, "Luxury", "Taj Exotica Resort & Spa / The Leela Goa", "Goa (3 Nights)", "03 Nights", "Luxury Ocean View Room", "Ultra Luxury All-Inclusive Plan", 5),
        _h(4, "Ultra Luxury", "ITC Grand Goa Resort & Spa (Private Beachfront)", "Goa (3 Nights)", "03 Nights", "VVIP Sea Facing Luxury Suite", "Ultra Luxury All-Inclusive Plan", 5),
    ],
    "GA-021": [
        _h(1, "Deluxe", "Hotel Country Inn & Suites by Radisson / similar", "Panaji / North Goa (4 Nights)", "04 Nights", "Standard Triple Shared Wing", "Full Board (All Meals)"),
        _h(2, "Premium", "Fortune Miramar by ITC Hotel Group / similar", "Panaji / North Goa (4 Nights)", "04 Nights", "Premium Twin Shared Room Wing", "Full Board (All Meals)"),
        _h(3, "Luxury", "The O Hotel / Vivanta Goa Panaji", "Panaji / North Goa (4 Nights)", "04 Nights", "Luxury Executive Double Room Wing", "Full Board + High Tea Service", 5),
        _h(4, "Ultra Luxury", "Taj Cidade de Goa Horizon / Grand Hyatt Goa", "Panaji / North Goa (4 Nights)", "04 Nights", "VVIP Deluxe Oceanfront Institutional Suite", "Elite Custom Luxury Dining Plan", 5),
    ],
    "GA-022": [
        _h(1, "Deluxe", "Panjim Inn Heritage / Fairfield by Marriott Benaulim", "Panaji / South Goa (4 Nights)", "04 Nights", "Premium Heritage / Deluxe Room", "MAPAI (Breakfast & Dinner)"),
        _h(2, "Premium", "Cidade de Goa (IHCL SeleQtions) / Heritage Village Resort", "Panaji / South Goa (4 Nights)", "04 Nights", "Premium Sea Facing Room", "MAPAI Plan"),
        _h(3, "Luxury", "The Leela Goa / Taj Exotica Resort & Spa", "Panaji / South Goa (4 Nights)", "04 Nights", "Luxury Lagoon Suite / Garden Villa", "Bespoke MAPAI Package", 5),
        _h(4, "Ultra Luxury", "ITC Grand Goa Resort & Spa / Alila Diwa (The Club)", "Panaji / South Goa (4 Nights)", "04 Nights", "VVIP Private Pool Villa Stay", "Elite Custom Culinary Plan", 5),
    ],
    "GA-023": [
        _h(1, "Deluxe", "DoubleTree by Hilton / Novotel Candolim | Kenilworth Resort / Heritage Village Resort", "North Goa (2 Nights) / South Goa (3 Nights)", "05 Nights", "Deluxe Room", "MAPAI (Breakfast & Dinner)"),
        _h(2, "Premium", "Hard Rock Hotel / Vivanta Goa Candolim | Caravela Beach Resort / Radisson Blu", "North Goa (2 Nights) / South Goa (3 Nights)", "05 Nights", "Premium Room", "MAPAI Premium Tiers"),
        _h(3, "Luxury", "The Leela Goa (Villas) / W Goa (Vagator) | Taj Exotica Resort & Spa / ITC Grand Goa", "North Goa (2 Nights) / South Goa (3 Nights)", "05 Nights", "Luxury Villa / Suite", "MAPAI Custom Club Class", 5),
        _h(4, "Ultra Luxury", "Taj Fort Aguada Resort (Pres. Suite) | The Leela Goa (The Club Suites)", "North Goa (2 Nights) / South Goa (3 Nights)", "05 Nights", "Presidential / Club Suite", "Bespoke Gourmet Curated Meal Plan", 5),
    ],
    "GA-024": [
        _h(1, "Deluxe", "Novotel Dona Sylvia / Lemon Tree Amarante | Heritage Village Resort & Spa / similar", "North Goa (3 Nights) / South Goa (3 Nights)", "06 Nights", "Deluxe Room", "MAPAI (Breakfast & Dinner)"),
        _h(2, "Premium", "Hard Rock Hotel / DoubleTree by Hilton | Caravela Beach Resort / Kenilworth Resort", "North Goa (3 Nights) / South Goa (3 Nights)", "06 Nights", "Premium Room", "MAPAI (Breakfast & Dinner)"),
        _h(3, "Luxury", "Taj Holiday Village / W Goa (Wonderful Room) | The Leela Goa (Lagoon Terrace) / Taj Exotica", "North Goa (3 Nights) / South Goa (3 Nights)", "06 Nights", "Luxury Suite", "MAPAI + Premium Amenities", 5),
        _h(4, "Ultra Luxury", "Taj Fort Aguada (Premium Sea View Suite) | The St. Regis Goa Resort (Luxury Private Villa)", "North Goa (3 Nights) / South Goa (3 Nights)", "06 Nights", "Luxury Private Villa", "Bespoke Gourmet Custom Plan", 5),
    ],
    "GA-025": [
        _h(1, "Deluxe", "Novotel Goa Resort & Spa / Lemon Tree Amarante | Heritage Village Resort / Kenilworth Resort", "North Goa (4 Nights) / South Goa (3 Nights)", "07 Nights", "Superior Garden View Room", "MAPAI (Breakfast & Dinner)"),
        _h(2, "Premium", "The O Hotel / Hard Rock Hotel Goa / similar | Caravela Beach Resort / Azaya Beach Resort", "North Goa (4 Nights) / South Goa (3 Nights)", "07 Nights", "Premium Balcony / Pool View Room", "MAPAI (Breakfast & Dinner)"),
        _h(3, "Luxury", "Taj Holiday Village / Taj Fort Aguada Resort | The Leela Goa / Taj Exotica Resort & Spa", "North Goa (4 Nights) / South Goa (3 Nights)", "07 Nights", "Luxury Sea-Facing Cottage / Suite", "MAPAI + Premium Amenities", 5),
        _h(4, "Ultra Luxury", "W Goa (Marvelous Chalet) / JW Marriott Vagator | The St. Regis Goa Resort (Private Pool Villa)", "North Goa (4 Nights) / South Goa (3 Nights)", "07 Nights", "VVIP Custom Sea Front Presidential Villa", "Bespoke Signature VIP Plan", 5),
    ],
}
