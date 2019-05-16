from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Returns for a given country its Pygal code,
     consisting of 2 letters."""
    for code, name in COUNTRIES.items():
        if country_name == 'Yemen, Rep':
            return 'ye'
        elif name == country_name:
            return code
    # If no country is found, return None.
    return None

print(get_country_code('United Arab Emirates'))