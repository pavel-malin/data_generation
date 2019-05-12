from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Returns for a given country its Pygal code,
     consisting of 2 letters."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If no country is found, return None.
    return None
