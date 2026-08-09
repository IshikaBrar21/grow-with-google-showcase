MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


def sunlight_matches(user_sunlight: str, plant_sunlight: str) -> bool:
    user_sunlight = user_sunlight.lower()
    plant_sunlight = plant_sunlight.lower()

    if user_sunlight == plant_sunlight:
        return True

    return False


def bloom_duration(bloom_start: str, bloom_end: str) -> int:
    start = MONTHS.get(bloom_start.lower())
    end = MONTHS.get(bloom_end.lower())

    if start is None or end is None:
        return 0

    if end >= start:
        return end - start + 1

    # Handles a bloom period crossing December
    return (12 - start + 1) + end


def calculate_score(plant, user_sunlight: str) -> int:
    score = 0

    if sunlight_matches(user_sunlight, plant["sun_needs"]):
        score += 40

    pollinators = [
        p.strip()
        for p in str(plant["pollinators_supported"]).split(",")
        if p.strip()
    ]

    # Plants with larger support for pollinators should be scored higher
    # The maximum score for pollinator support is capped at 30 points
    score += min(len(pollinators) * 10, 30)

    # Longer bloom periods are beneficial for pollinators and should be scored higher
    duration = bloom_duration(
        str(plant["bloom_start"]),
        str(plant["bloom_end"])
    )
    score += min(duration * 3, 30)

    return score


def recommend_plants(plants, user_sunlight: str, limit: int = 5):

    # Our dataset is specifically scoped to the Maryland Piedmont.
    # Plants outside that native range should not be recommended.
    native_plants = plants[
        plants["native_range"].str.lower() == "maryland piedmont"
    ]

    recommendations = []

    for _,plant in native_plants.iterrows():

        score = calculate_score(
            plant,
            user_sunlight
        )

        pollinators = [
            p.strip()
            for p in str(
                plant["pollinators_supported"]
            ).split(",")
            if p.strip()
        ]

        recommendations.append({
            "species_id": str(plant["species_id"]),
            "common_name": str(plant["common_name"]),
            "scientific_name": str(plant["scientific_name"]),
            "native_range": str(plant["native_range"]),
            "bloom_start": str(plant["bloom_start"]),
            "bloom_end": str(plant["bloom_end"]),
            "sun_needs": str(plant["sun_needs"]),
            "soil_type": str(plant["soil_type"]),
            "moisture": str(plant["moisture"]),
            "pollinators_supported": pollinators,
            "hardiness_zones": str(plant["hardiness_zones"]),
            "source": str(plant["source"]),
            "source_url": str(plant["source_url"]),
            "score": score,
        })

    recommendations.sort(
        key=lambda plant: plant["score"],
        reverse=True
    )

    return recommendations[:limit]