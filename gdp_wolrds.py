import json

import pygal.maps.world
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from country_codes import get_country_code

filename = 'gdp_json.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_gdp = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        gdp = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp

cc_pops_1, cc_pops_2, cc_pops_3, cc_pops_4 = {}, {}, {}, {}
for cc, pop in cc_gdp.items():
    if pop < 1000000000:
        cc_pops_1[cc] = pop
    elif pop < 10000000000:
        cc_pops_2[cc] = pop
    elif pop < 100000000000:
        cc_pops_3[cc] = pop
    else:
        cc_pops_4[cc] = pop

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3), len(cc_pops_4))

wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(slice=wm_style)
wm.title = 'Country, Regional and World GDP (Gross Domestic Product)'
wm.add('0-1bn', cc_pops_1)
wm.add('1bn-10bn', cc_pops_2)
wm.add('10bn-100bn', cc_pops_3)
wm.add('>100bn', cc_pops_4)

wm.render_to_file('gdp_wolrds.svg')
