# city_functions.py

def city_country(city, country, population=None, language=None):
    """Return a string like 'City, Country - population xxx, Language'."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# Call the function with the following arguments:
print(city_country('santiago', 'chile')) # Santiago, Chile
print(city_country('minneapolis', 'united states', 423000)) # Minneapolis, United States
print(city_country('tokyo', 'japan', 37100000, 'japanese')) # Tokyo, Japan
print(city_country('london', 'england', language='english')) # London, England