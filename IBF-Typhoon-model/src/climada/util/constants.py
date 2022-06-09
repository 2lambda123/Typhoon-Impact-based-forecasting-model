"""
This file is part of CLIMADA.

Copyright (C) 2017 ETH Zurich, CLIMADA contributors listed in AUTHORS.

CLIMADA is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free
Software Foundation, version 3.

CLIMADA is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with CLIMADA. If not, see <https://www.gnu.org/licenses/>.

---

Define constants.
"""

__all__ = ['SYSTEM_DIR',
           'DEMO_DIR',
           'ENT_DEMO_TODAY',
           'ENT_DEMO_FUTURE',
           'HAZ_DEMO_MAT',
           'HAZ_DEMO_FL',
           'HAZ_DEMO_FLDDPH',
           'HAZ_DEMO_FLDFRC',
           'ENT_TEMPLATE_XLS',
           'HAZ_TEMPLATE_XLS',
           'ONE_LAT_KM',
           'EARTH_RADIUS_KM',
           'GLB_CENTROIDS_MAT',
           'GLB_CENTROIDS_NC',
           'ISIMIP_GPWV3_NATID_150AS',
           'NATEARTH_CENTROIDS',
           'DEMO_GDP2ASSET',
           'RIVER_FLOOD_REGIONS_CSV',
           'TC_ANDREW_FL',
           'HAZ_DEMO_H5',
           'EXP_DEMO_H5',
           'WS_DEMO_NC']

# pylint: disable=unused-import
# without importing numpy ahead of fiona the debugger may run into an error
import numpy
from fiona.crs import from_epsg
import matplotlib as mpl
from .config import CONFIG
from pathlib import Path
#SYSTEM_DIR = CONFIG.local_data.system.dir(create=False)
SYSTEM_DIR = Path("./src/climada/data/system/") #CONFIG.local_data.system.dir(create=False)
"""Folder containing the data used internally"""

#DEMO_DIR = CONFIG.local_data.demo.dir(create=False)
DEMO_DIR =  Path("./src/climada/data/demo/") #CONFIG.local_data.demo.dir(create=False)
"""Folder containing the data used for tutorials"""

ISIMIP_GPWV3_NATID_150AS = SYSTEM_DIR.joinpath('NatID_grid_0150as.nc')
"""
Compressed version of National Identifier Grid in 150 arc-seconds from
ISIMIP project, based on GPWv3. Location in ISIMIP repository:

`ISIMIP2a/InputData/landuse_humaninfluences/population/ID_GRID/Nat_id_grid_ISIMIP.nc`

More references:

* https://www.isimip.org/gettingstarted/input-data-bias-correction/details/13/
* https://sedac.ciesin.columbia.edu/data/set/gpw-v3-national-identifier-grid
"""

GLB_CENTROIDS_NC = ISIMIP_GPWV3_NATID_150AS
"""For backwards compatibility, it remains available under its old name."""

GLB_CENTROIDS_MAT = SYSTEM_DIR.joinpath('GLB_NatID_grid_0360as_adv_2.mat')
"""Global centroids"""

NATEARTH_CENTROIDS = {
    150: SYSTEM_DIR.joinpath('NatEarth_Centroids_150as.hdf5'),
    360: SYSTEM_DIR.joinpath('NatEarth_Centroids_360as.hdf5'),
}
"""
Global centroids at XXX arc-seconds resolution,
including region ids from Natural Earth. The 360 AS file includes distance to
coast from NASA.
"""

ENT_TEMPLATE_XLS = SYSTEM_DIR.joinpath('entity_template.xlsx')
"""Entity template in xls format."""

HAZ_TEMPLATE_XLS = SYSTEM_DIR.joinpath('hazard_template.xlsx')
"""Hazard template in xls format."""

RIVER_FLOOD_REGIONS_CSV = SYSTEM_DIR.joinpath('NatRegIDs.csv')
"""Look-up table for river flood module"""

HAZ_DEMO_FL = DEMO_DIR.joinpath('SC22000_VE__M1.grd.gz')
"""Raster file of flood over Venezuela. Model from GAR2015"""

HAZ_DEMO_FLDDPH = DEMO_DIR.joinpath('flddph_2000_DEMO.nc')
"""NetCDF4 Flood depth from isimip simulations"""

HAZ_DEMO_FLDFRC = DEMO_DIR.joinpath('fldfrc_2000_DEMO.nc')
"""NetCDF4 Flood fraction from isimip simulations"""

HAZ_DEMO_MAT = DEMO_DIR.joinpath('atl_prob_nonames.mat')
"""
Hazard demo from climada in MATLAB: hurricanes from 1851 to 2011 over Florida with 100 centroids.
"""

HAZ_DEMO_H5 = DEMO_DIR.joinpath('tc_fl_1990_2004.h5')
"""
Hazard demo in hdf5 format: IBTrACS from 1990 to 2004 over Florida with 2500 centroids.
"""

DEMO_GDP2ASSET = DEMO_DIR.joinpath('gdp2asset_CHE_exposure.nc')
"""Exposure demo file for GDP2Asset"""

WS_DEMO_NC = [DEMO_DIR.joinpath('fp_lothar_crop-test.nc'),
              DEMO_DIR.joinpath('fp_xynthia_crop-test.nc')]
"""
Winter storm in Europe files. These test files have been generated using
the netCDF kitchen sink:

>>> ncks -d latitude,50.5,54.0 -d longitude,3.0,7.5 ./file_in.nc ./file_out.nc
"""


ENT_DEMO_TODAY = DEMO_DIR.joinpath('demo_today.xlsx')
"""Entity demo present in xslx format."""

ENT_DEMO_FUTURE = DEMO_DIR.joinpath('demo_future_TEST.xlsx')
"""Entity demo future in xslx format."""

EXP_DEMO_H5 = DEMO_DIR.joinpath('exp_demo_today.h5')
"""Exposures over Florida"""


TC_ANDREW_FL = DEMO_DIR.joinpath('ibtracs_global_intp-None_1992230N11325.csv')
"""Tropical cyclone Andrew in Florida"""


ISIMIP_NATID_TO_ISO = [
    '', 'ABW', 'AFG', 'AGO', 'AIA', 'ALB', 'AND', 'ANT', 'ARE', 'ARG', 'ARM',
    'ASM', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BFA', 'BGD', 'BGR',
    'BHR', 'BHS', 'BIH', 'BLR', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN',
    'BWA', 'CAF', 'CAN', 'CHE', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COK',
    'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CYM', 'CYP', 'CZE', 'DEU', 'DJI', 'DMA',
    'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ESP', 'EST', 'ETH', 'FIN', 'FJI',
    'FLK', 'FRA', 'FRO', 'FSM', 'GAB', 'GBR', 'GEO', 'GGY', 'GHA', 'GIB', 'GIN',
    'GLP', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRD', 'GTM', 'GUF', 'GUM', 'GUY', 'HKG',
    'HND', 'HRV', 'HTI', 'HUN', 'IDN', 'IMN', 'IND', 'IRL', 'IRN', 'IRQ', 'ISL',
    'ISR', 'ITA', 'JAM', 'JEY', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KHM', 'KIR',
    'KNA', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR', 'LBY', 'LCA', 'LIE', 'LKA', 'LSO',
    'LTU', 'LUX', 'LVA', 'MAC', 'MAR', 'MCO', 'MDA', 'MDG', 'MDV', 'MEX', 'MHL',
    'MKD', 'MLI', 'MLT', 'MMR', 'MNG', 'MNP', 'MOZ', 'MRT', 'MSR', 'MTQ', 'MUS',
    'MWI', 'MYS', 'MYT', 'NAM', 'NCL', 'NER', 'NFK', 'NGA', 'NIC', 'NIU', 'NLD',
    'NOR', 'NPL', 'NRU', 'NZL', 'OMN', 'PAK', 'PAN', 'PCN', 'PER', 'PHL', 'PLW',
    'PNG', 'POL', 'PRI', 'PRK', 'PRT', 'PRY', 'PSE', 'PYF', 'QAT', 'REU', 'ROU',
    'RUS', 'RWA', 'SAU', 'SCG', 'SDN', 'SEN', 'SGP', 'SHN', 'SJM', 'SLB', 'SLE',
    'SLV', 'SMR', 'SOM', 'SPM', 'STP', 'SUR', 'SVK', 'SVN', 'SWE', 'SWZ', 'SYC',
    'SYR', 'TCA', 'TCD', 'TGO', 'THA', 'TJK', 'TKL', 'TKM', 'TLS', 'TON', 'TTO',
    'TUN', 'TUR', 'TUV', 'TWN', 'TZA', 'UGA', 'UKR', 'URY', 'USA', 'UZB', 'VCT',
    'VEN', 'VGB', 'VIR', 'VNM', 'VUT', 'WLF', 'WSM', 'YEM', 'ZAF', 'ZMB', 'ZWE',
]
"""ISO 3166 alpha-3 codes of countries used in ISIMIP_GPWV3_NATID_150AS"""

NONISO_REGIONS = [
    # Dummy region for numeric 0 (or empty string), sometimes used for oceans
    dict(name="", alpha_2="", alpha_3="", numeric="000"),
    dict(name="Akrotiri", alpha_2="XA", alpha_3="XXA", numeric="901"),
    dict(name="Baikonur", alpha_2="XB", alpha_3="XXB", numeric="902"),
    dict(name="Bajo Nuevo Bank", alpha_2="XJ", alpha_3="XXJ", numeric="903"),
    dict(name="Clipperton I.", alpha_2="XC", alpha_3="XXC", numeric="904"),
    dict(name="Coral Sea Is.", alpha_2="XO", alpha_3="XXO", numeric="905"),
    dict(name="Cyprus U.N. Buffer Zone", alpha_2="XU", alpha_3="XXU", numeric="906"),
    dict(name="Dhekelia", alpha_2="XD", alpha_3="XXD", numeric="907"),
    dict(name="Indian Ocean Ter.", alpha_2="XI", alpha_3="XXI", numeric="908"),
    # For Kosovo, we follow the iso3166 package and the statistical office of Canada:
    # https://www.statcan.gc.ca/eng/subjects/standard/sccai/2011/scountry-desc
    dict(name="Kosovo", alpha_2="XK", alpha_3="XKO", numeric="983"),
    dict(name="N. Cyprus", alpha_2="XY", alpha_3="XXY", numeric="910"),
    dict(name="Scarborough Reef", alpha_2="XS", alpha_3="XXS", numeric="912"),
    dict(name="Serranilla Bank", alpha_2="XR", alpha_3="XXR", numeric="913"),
    dict(name="Siachen Glacier", alpha_2="XH", alpha_3="XXH", numeric="914"),
    dict(name="Somaliland", alpha_2="XM", alpha_3="XXM", numeric="915"),
    dict(name="Spratly Is.", alpha_2="XP", alpha_3="XXP", numeric="916"),
    dict(name="USNB Guantanamo Bay", alpha_2="XG", alpha_3="XXG", numeric="917"),
]
"""Geopolitical areas that are not listed in the ISO 3166 standard, but might be relevant when
working, e.g. with Natural Earth shape files. The alpha-2, alpha-3 and numeric representations are
unofficial and for internal use only."""

ONE_LAT_KM = 111.12
"""Mean one latitude (in degrees) to km"""

EARTH_RADIUS_KM = 6371
"""Earth radius in km"""

DEF_EPSG = 4326
"""Default EPSG code"""

DEF_CRS = f'EPSG:{DEF_EPSG}'
"""Default coordinate reference system WGS 84, str, for pyproj and rasterio CRS.from_string()"""

DEF_CRS_FIONA = from_epsg(DEF_EPSG)
"""Default coordinate reference system WGS 84, dict, for fiona interface"""

cm_data1 = [[0.00000000, 0.00000000, 0.00000000],
           [0.00032031, 0.00020876, 0.00015576],
           [0.00115213, 0.00071222, 0.00050933],
           [0.00246632, 0.00145292, 0.00099932],
           [0.00426111, 0.00240248, 0.00159470],
           [0.00654129, 0.00354149, 0.00227479],
           [0.00931453, 0.00485497, 0.00302435],
           [0.01259008, 0.00633067, 0.00383153],
           [0.01637810, 0.00795809, 0.00468676],
           [0.02068947, 0.00972796, 0.00558214],
           [0.02553552, 0.01163194, 0.00651101],
           [0.03092793, 0.01366243, 0.00746771],
           [0.03687870, 0.01581232, 0.00844736],
           [0.04329108, 0.01807499, 0.00944575],
           [0.04970018, 0.02044415, 0.01045917],
           [0.05607744, 0.02291381, 0.01148441],
           [0.06242826, 0.02547822, 0.01251862],
           [0.06875727, 0.02813185, 0.01355932],
           [0.07506844, 0.03086930, 0.01460431],
           [0.08136524, 0.03368535, 0.01565167],
           [0.08765071, 0.03657489, 0.01669973],
           [0.09392754, 0.03953289, 0.01774700],
           [0.10019812, 0.04248851, 0.01879222],
           [0.10646459, 0.04536893, 0.01983431],
           [0.11272888, 0.04818555, 0.02087234],
           [0.11899272, 0.05094021, 0.02190555],
           [0.12525770, 0.05363453, 0.02293331],
           [0.13152527, 0.05626994, 0.02395516],
           [0.13779673, 0.05884770, 0.02497073],
           [0.14407332, 0.06136894, 0.02597979],
           [0.15035614, 0.06383462, 0.02698225],
           [0.15664624, 0.06624561, 0.02797810],
           [0.16294457, 0.06860266, 0.02896747],
           [0.16925203, 0.07090640, 0.02995057],
           [0.17556946, 0.07315739, 0.03092776],
           [0.18189762, 0.07535608, 0.03189947],
           [0.18823726, 0.07750287, 0.03286623],
           [0.19458905, 0.07959805, 0.03382870],
           [0.20095364, 0.08164185, 0.03478764],
           [0.20733163, 0.08363445, 0.03574389],
           [0.21372359, 0.08557593, 0.03669841],
           [0.22013006, 0.08746634, 0.03765228],
           [0.22655154, 0.08930565, 0.03860667],
           [0.23298852, 0.09109380, 0.03956286],
           [0.23944144, 0.09283065, 0.04052097],
           [0.24591073, 0.09451600, 0.04146142],
           [0.25239679, 0.09614964, 0.04239527],
           [0.25890000, 0.09773126, 0.04332440],
           [0.26542072, 0.09926052, 0.04425071],
           [0.27195929, 0.10073705, 0.04517610],
           [0.27851612, 0.10216029, 0.04610242],
           [0.28509144, 0.10352983, 0.04703172],
           [0.29168551, 0.10484515, 0.04796603],
           [0.29829858, 0.10610566, 0.04890741],
           [0.30493089, 0.10731073, 0.04985793],
           [0.31158270, 0.10845962, 0.05081968],
           [0.31825437, 0.10955144, 0.05179469],
           [0.32494588, 0.11058558, 0.05278533],
           [0.33165741, 0.11156121, 0.05379388],
           [0.33838918, 0.11247734, 0.05482253],
           [0.34514146, 0.11333282, 0.05587349],
           [0.35191413, 0.11412692, 0.05694939],
           [0.35870733, 0.11485850, 0.05805261],
           [0.36552140, 0.11552606, 0.05918537],
           [0.37235602, 0.11612887, 0.06035055],
           [0.37921149, 0.11666531, 0.06155047],
           [0.38608774, 0.11713411, 0.06278785],
           [0.39298465, 0.11753398, 0.06406542],
           [0.39990243, 0.11786308, 0.06538571],
           [0.40684070, 0.11812026, 0.06675174],
           [0.41379968, 0.11830340, 0.06816610],
           [0.42077900, 0.11841110, 0.06963182],
           [0.42777857, 0.11844140, 0.07115178],
           [0.43479835, 0.11839213, 0.07272887],
           [0.44183779, 0.11826176, 0.07436631],
           [0.44889692, 0.11804763, 0.07606698],
           [0.45597537, 0.11774759, 0.07783407],
           [0.46307262, 0.11735955, 0.07967086],
           [0.47018828, 0.11688094, 0.08158056],
           [0.47732206, 0.11630887, 0.08356643],
           [0.48447342, 0.11564059, 0.08563184],
           [0.49164167, 0.11487339, 0.08778027],
           [0.49882616, 0.11400421, 0.09001524],
           [0.50602619, 0.11302981, 0.09234030],
           [0.51324096, 0.11194681, 0.09475911],
           [0.52046957, 0.11075165, 0.09727541],
           [0.52771103, 0.10944063, 0.09989300],
           [0.53496423, 0.10800987, 0.10261578],
           [0.54222828, 0.10645458, 0.10544773],
           [0.54950158, 0.10477099, 0.10839295],
           [0.55678265, 0.10295467, 0.11145561],
           [0.56407005, 0.10100050, 0.11463998],
           [0.57136221, 0.09890294, 0.11795046],
           [0.57865683, 0.09665778, 0.12139144],
           [0.58595251, 0.09425758, 0.12496762],
           [0.59324637, 0.09169820, 0.12868351],
           [0.60053647, 0.08897198, 0.13254399],
           [0.60781996, 0.08607290, 0.13655381],
           [0.61509391, 0.08299424, 0.14071783],
           [0.62235528, 0.07972847, 0.14504098],
           [0.62960086, 0.07626735, 0.14952833],
           [0.63682690, 0.07260321, 0.15418475],
           [0.64402945, 0.06872768, 0.15901515],
           [0.65120429, 0.06463189, 0.16402435],
           [0.65834703, 0.06030595, 0.16921717],
           [0.66545273, 0.05574060, 0.17459807],
           [0.67251615, 0.05092618, 0.18017123],
           [0.67953179, 0.04585268, 0.18594053],
           [0.68649408, 0.04050791, 0.19190990],
           [0.69339656, 0.03501827, 0.19808181],
           [0.70023310, 0.02974032, 0.20445918],
           [0.70699677, 0.02473108, 0.21104325],
           [0.71368081, 0.02004735, 0.21783521],
           [0.72027805, 0.01575128, 0.22483488],
           [0.72678121, 0.01190847, 0.23204104],
           [0.73318299, 0.00858729, 0.23945145],
           [0.73947609, 0.00585900, 0.24706262],
           [0.74565328, 0.00379723, 0.25486974],
           [0.75170751, 0.00247734, 0.26286660],
           [0.75763201, 0.00197573, 0.27104565],
           [0.76342035, 0.00236912, 0.27939796],
           [0.76906659, 0.00373375, 0.28791328],
           [0.77456531, 0.00614457, 0.29658016],
           [0.77991170, 0.00967453, 0.30538600],
           [0.78510166, 0.01439382, 0.31431727],
           [0.79013176, 0.02036922, 0.32335963],
           [0.79499936, 0.02766356, 0.33249813],
           [0.79970258, 0.03633527, 0.34171740],
           [0.80424028, 0.04610137, 0.35100187],
           [0.80861206, 0.05593074, 0.36033595],
           [0.81281824, 0.06575513, 0.36970423],
           [0.81685977, 0.07556701, 0.37909164],
           [0.82073820, 0.08536045, 0.38848361],
           [0.82445563, 0.09513050, 0.39786621],
           [0.82801462, 0.10487292, 0.40722623],
           [0.83141814, 0.11458394, 0.41655122],
           [0.83466964, 0.12426002, 0.42582926],
           [0.83777258, 0.13389850, 0.43505012],
           [0.84073089, 0.14349659, 0.44420371],
           [0.84354864, 0.15305194, 0.45328109],
           [0.84622995, 0.16256264, 0.46227431],
           [0.84877908, 0.17202698, 0.47117623],
           [0.85120054, 0.18144313, 0.47998013],
           [0.85349849, 0.19081025, 0.48868085],
           [0.85567734, 0.20012720, 0.49727347],
           [0.85774150, 0.20939307, 0.50575378],
           [0.85969539, 0.21860703, 0.51411817],
           [0.86154321, 0.22776871, 0.52236389],
           [0.86328918, 0.23687774, 0.53048865],
           [0.86493759, 0.24593368, 0.53849050],
           [0.86649243, 0.25493655, 0.54636825],
           [0.86795766, 0.26388635, 0.55412108],
           [0.86933714, 0.27278325, 0.56174857],
           [0.87063488, 0.28162708, 0.56925039],
           [0.87185473, 0.29041795, 0.57662667],
           [0.87299987, 0.29915672, 0.58387836],
           [0.87407470, 0.30784267, 0.59100548],
           [0.87508176, 0.31647731, 0.59800984],
           [0.87602545, 0.32505984, 0.60489185],
           [0.87690829, 0.33359164, 0.61165350],
           [0.87773379, 0.34207284, 0.61829617],
           [0.87850545, 0.35050356, 0.62482133],
           [0.87922592, 0.35888478, 0.63123109],
           [0.87989827, 0.36721697, 0.63752735],
           [0.88052548, 0.37550059, 0.64371209],
           [0.88111058, 0.38373605, 0.64978738],
           [0.88165635, 0.39192396, 0.65575540],
           [0.88216538, 0.40006502, 0.66161845],
           [0.88264034, 0.40815983, 0.66737883],
           [0.88308383, 0.41620898, 0.67303885],
           [0.88349837, 0.42421311, 0.67860087],
           [0.88388658, 0.43217272, 0.68406723],
           [0.88425089, 0.44008842, 0.68944031],
           [0.88459352, 0.44796098, 0.69472256],
           [0.88491674, 0.45579107, 0.69991638],
           [0.88522277, 0.46357936, 0.70502418],
           [0.88551386, 0.47132645, 0.71004831],
           [0.88579260, 0.47903263, 0.71499109],
           [0.88606054, 0.48669904, 0.71985498],
           [0.88631967, 0.49432634, 0.72464230],
           [0.88657273, 0.50191463, 0.72935531],
           [0.88682100, 0.50946512, 0.73399636],
           [0.88706656, 0.51697833, 0.73856771],
           [0.88731166, 0.52445464, 0.74307157],
           [0.88755748, 0.53189523, 0.74751019],
           [0.88780677, 0.53930002, 0.75188571],
           [0.88806029, 0.54667042, 0.75620029],
           [0.88832077, 0.55400637, 0.76045604],
           [0.88858898, 0.56130917, 0.76465503],
           [0.88886751, 0.56857881, 0.76879932],
           [0.88915723, 0.57581648, 0.77289087],
           [0.88946027, 0.58302245, 0.77693169],
           [0.88977801, 0.59019749, 0.78092369],
           [0.89011184, 0.59734231, 0.78486874],
           [0.89046385, 0.60445719, 0.78876876],
           [0.89083498, 0.61154309, 0.79262552],
           [0.89122688, 0.61860051, 0.79644080],
           [0.89164127, 0.62562987, 0.80021639],
           [0.89207922, 0.63263202, 0.80395396],
           [0.89254218, 0.63960749, 0.80765517],
           [0.89303193, 0.64655664, 0.81132175],
           [0.89354946, 0.65348027, 0.81495521],
           [0.89409613, 0.66037894, 0.81855714],
           [0.89467341, 0.66725312, 0.82212908],
           [0.89528268, 0.67410333, 0.82567258],
           [0.89592507, 0.68093022, 0.82918904],
           [0.89660188, 0.68773430, 0.83267991],
           [0.89731440, 0.69451609, 0.83614660],
           [0.89806405, 0.70127602, 0.83959053],
           [0.89885189, 0.70801470, 0.84301299],
           [0.89967918, 0.71473262, 0.84641529],
           [0.90054714, 0.72143026, 0.84979872],
           [0.90145701, 0.72810810, 0.85316454],
           [0.90241007, 0.73476657, 0.85651399],
           [0.90340743, 0.74140617, 0.85984825],
           [0.90445031, 0.74802735, 0.86316849],
           [0.90553992, 0.75463054, 0.86647585],
           [0.90667746, 0.76121615, 0.86977146],
           [0.90786415, 0.76778459, 0.87305641],
           [0.90910120, 0.77433626, 0.87633178],
           [0.91038981, 0.78087154, 0.87959861],
           [0.91173124, 0.78739078, 0.88285793],
           [0.91312673, 0.79389433, 0.88611074],
           [0.91457758, 0.80038249, 0.88935803],
           [0.91608500, 0.80685562, 0.89260074],
           [0.91765039, 0.81331396, 0.89583983],
           [0.91927511, 0.81975775, 0.89907623],
           [0.92096059, 0.82618722, 0.90231088],
           [0.92270830, 0.83260254, 0.90554466],
           [0.92451964, 0.83900395, 0.90877841],
           [0.92639632, 0.84539150, 0.91201305],
           [0.92834008, 0.85176524, 0.91524947],
           [0.93035272, 0.85812518, 0.91848857],
           [0.93243609, 0.86447132, 0.92173117],
           [0.93459223, 0.87080356, 0.92497815],
           [0.93682359, 0.87712161, 0.92823055],
           [0.93913266, 0.88342515, 0.93148937],
           [0.94152187, 0.88971391, 0.93475546],
           [0.94399458, 0.89598719, 0.93803021],
           [0.94655427, 0.90224421, 0.94131502],
           [0.94920436, 0.90848425, 0.94461125],
           ]

cm_data2 = [[0.00000000, 0.00000000, 0.00000000],
           [0.00028691, 0.00020835, 0.00028279],
           [0.00102421, 0.00070903, 0.00101021],
           [0.00218033, 0.00144242, 0.00214845],
           [0.00375280, 0.00237790, 0.00368891],
           [0.00574727, 0.00349371, 0.00562841],
           [0.00817359, 0.00477242, 0.00796563],
           [0.01104432, 0.00619914, 0.01069976],
           [0.01437378, 0.00776073, 0.01382970],
           [0.01817764, 0.00944524, 0.01735364],
           [0.02247277, 0.01124162, 0.02126897],
           [0.02727694, 0.01313949, 0.02557207],
           [0.03260869, 0.01512908, 0.03025819],
           [0.03848721, 0.01720107, 0.03532137],
           [0.04472223, 0.01934661, 0.04074862],
           [0.05095008, 0.02155723, 0.04620189],
           [0.05718085, 0.02382484, 0.05156892],
           [0.06341877, 0.02614168, 0.05685075],
           [0.06966727, 0.02850036, 0.06204782],
           [0.07592916, 0.03089381, 0.06716019],
           [0.08220666, 0.03331529, 0.07218757],
           [0.08850155, 0.03575837, 0.07712945],
           [0.09481532, 0.03821687, 0.08198520],
           [0.10114895, 0.04068063, 0.08675399],
           [0.10750319, 0.04306161, 0.09143498],
           [0.11387855, 0.04536332, 0.09602729],
           [0.12027537, 0.04758808, 0.10053004],
           [0.12669388, 0.04973801, 0.10494242],
           [0.13313410, 0.05181515, 0.10926361],
           [0.13959587, 0.05382147, 0.11349284],
           [0.14607903, 0.05575879, 0.11762946],
           [0.15258333, 0.05762879, 0.12167284],
           [0.15910850, 0.05943303, 0.12562246],
           [0.16565413, 0.06117310, 0.12947786],
           [0.17221981, 0.06285040, 0.13323866],
           [0.17880518, 0.06446624, 0.13690456],
           [0.18540980, 0.06602187, 0.14047531],
           [0.19203321, 0.06751848, 0.14395075],
           [0.19867499, 0.06895715, 0.14733079],
           [0.20533472, 0.07033887, 0.15061537],
           [0.21201197, 0.07166460, 0.15380450],
           [0.21870632, 0.07293518, 0.15689824],
           [0.22541736, 0.07415142, 0.15989669],
           [0.23214472, 0.07531401, 0.16279996],
           [0.23888802, 0.07642364, 0.16560823],
           [0.24564687, 0.07748088, 0.16832171],
           [0.25242097, 0.07848626, 0.17094058],
           [0.25920996, 0.07944023, 0.17346508],
           [0.26601352, 0.08034324, 0.17589547],
           [0.27283134, 0.08119562, 0.17823199],
           [0.27966317, 0.08199764, 0.18047489],
           [0.28650868, 0.08274959, 0.18262446],
           [0.29336760, 0.08345167, 0.18468096],
           [0.30023971, 0.08410396, 0.18664460],
           [0.30712474, 0.08470663, 0.18851568],
           [0.31402240, 0.08525975, 0.19029445],
           [0.32093251, 0.08576327, 0.19198110],
           [0.32785482, 0.08621717, 0.19357587],
           [0.33478905, 0.08662148, 0.19507899],
           [0.34173503, 0.08697601, 0.19649062],
           [0.34869254, 0.08728060, 0.19781092],
           [0.35566125, 0.08753522, 0.19904011],
           [0.36264104, 0.08773953, 0.20017823],
           [0.36963165, 0.08789334, 0.20122542],
           [0.37663272, 0.08799656, 0.20218186],
           [0.38364424, 0.08804859, 0.20304740],
           [0.39066574, 0.08804944, 0.20382227],
           [0.39769703, 0.08799872, 0.20450641],
           [0.40473792, 0.08789596, 0.20509971],
           [0.41178790, 0.08774121, 0.20560237],
           [0.41884704, 0.08753353, 0.20601388],
           [0.42591463, 0.08727325, 0.20633459],
           [0.43299069, 0.08695948, 0.20656394],
           [0.44007455, 0.08659242, 0.20670212],
           [0.44716616, 0.08617128, 0.20674851],
           [0.45426479, 0.08569637, 0.20670331],
           [0.46137042, 0.08516677, 0.20656566],
           [0.46848219, 0.08458313, 0.20633582],
           [0.47560004, 0.08394454, 0.20601280],
           [0.48272316, 0.08325159, 0.20559662],
           [0.48985104, 0.08250434, 0.20508677],
           [0.49698340, 0.08170242, 0.20448225],
           [0.50411927, 0.08084690, 0.20378304],
           [0.51125803, 0.07993830, 0.20298844],
           [0.51839929, 0.07897664, 0.20209721],
           [0.52554202, 0.07796358, 0.20110904],
           [0.53268538, 0.07690049, 0.20002312],
           [0.53982852, 0.07578902, 0.19883855],
           [0.54697049, 0.07463129, 0.19755431],
           [0.55411028, 0.07342990, 0.19616934],
           [0.56124678, 0.07218810, 0.19468248],
           [0.56837880, 0.07090985, 0.19309253],
           [0.57550502, 0.06959997, 0.19139818],
           [0.58262400, 0.06826431, 0.18959809],
           [0.58973418, 0.06690989, 0.18769083],
           [0.59683382, 0.06554515, 0.18567490],
           [0.60392106, 0.06418012, 0.18354875],
           [0.61099403, 0.06282598, 0.18131023],
           [0.61805061, 0.06149625, 0.17895730],
           [0.62508803, 0.06020822, 0.17648890],
           [0.63210426, 0.05897851, 0.17390136],
           [0.63909578, 0.05783082, 0.17119418],
           [0.64606007, 0.05678752, 0.16836327],
           [0.65299326, 0.05587785, 0.16540731],
           [0.65989160, 0.05513269, 0.16232365],
           [0.66675096, 0.05458598, 0.15910942],
           [0.67356680, 0.05427454, 0.15576179],
           [0.68033403, 0.05423761, 0.15227799],
           [0.68704706, 0.05451589, 0.14865546],
           [0.69369969, 0.05515040, 0.14489185],
           [0.70028509, 0.05618108, 0.14098519],
           [0.70679624, 0.05764355, 0.13693176],
           [0.71322465, 0.05957213, 0.13273203],
           [0.71956187, 0.06199294, 0.12838347],
           [0.72579832, 0.06492701, 0.12388673],
           [0.73192387, 0.06838759, 0.11924309],
           [0.73792785, 0.07238015, 0.11445523],
           [0.74379911, 0.07690258, 0.10952793],
           [0.74952631, 0.08194530, 0.10446780],
           [0.75509807, 0.08749192, 0.09928513],
           [0.76050344, 0.09351949, 0.09399345],
           [0.76573234, 0.09999923, 0.08860931],
           [0.77077595, 0.10689714, 0.08315390],
           [0.77562724, 0.11417469, 0.07765262],
           [0.78028137, 0.12178994, 0.07213493],
           [0.78473594, 0.12969861, 0.06663478],
           [0.78899120, 0.13785534, 0.06119075],
           [0.79304987, 0.14621526, 0.05584590],
           [0.79691698, 0.15473527, 0.05064835],
           [0.80059949, 0.16337512, 0.04565234],
           [0.80410578, 0.17209842, 0.04091877],
           [0.80744502, 0.18087354, 0.03656330],
           [0.81062721, 0.18967261, 0.03284897],
           [0.81366202, 0.19847328, 0.02978095],
           [0.81655911, 0.20725703, 0.02735425],
           [0.81932773, 0.21600901, 0.02556368],
           [0.82197656, 0.22471783, 0.02440445],
           [0.82451354, 0.23337504, 0.02387282],
           [0.82694588, 0.24197470, 0.02396658],
           [0.82928000, 0.25051291, 0.02468537],
           [0.83152234, 0.25898625, 0.02603161],
           [0.83367755, 0.26739445, 0.02800850],
           [0.83575119, 0.27573587, 0.03062270],
           [0.83774693, 0.28401176, 0.03388176],
           [0.83966871, 0.29222281, 0.03779577],
           [0.84152000, 0.30037020, 0.04231855],
           [0.84330390, 0.30845547, 0.04718171],
           [0.84502314, 0.31648042, 0.05232334],
           [0.84668012, 0.32444703, 0.05769850],
           [0.84827700, 0.33235739, 0.06327080],
           [0.84981598, 0.34021329, 0.06901096],
           [0.85129899, 0.34801660, 0.07489554],
           [0.85272715, 0.35576999, 0.08090629],
           [0.85410285, 0.36347441, 0.08702799],
           [0.85542653, 0.37113285, 0.09324952],
           [0.85670046, 0.37874607, 0.09956104],
           [0.85792511, 0.38631664, 0.10595570],
           [0.85910167, 0.39384615, 0.11242769],
           [0.86023184, 0.40133560, 0.11897200],
           [0.86131603, 0.40878710, 0.12558544],
           [0.86235527, 0.41620202, 0.13226519],
           [0.86335049, 0.42358173, 0.13900904],
           [0.86430261, 0.43092748, 0.14581530],
           [0.86521249, 0.43824051, 0.15268270],
           [0.86608094, 0.44552198, 0.15961030],
           [0.86690878, 0.45277298, 0.16659744],
           [0.86769678, 0.45999455, 0.17364368],
           [0.86844571, 0.46718767, 0.18074877],
           [0.86915633, 0.47435325, 0.18791261],
           [0.86982940, 0.48149217, 0.19513520],
           [0.87046566, 0.48860521, 0.20241667],
           [0.87106589, 0.49569313, 0.20975721],
           [0.87163086, 0.50275663, 0.21715708],
           [0.87216162, 0.50979614, 0.22461634],
           [0.87265881, 0.51681240, 0.23213553],
           [0.87312317, 0.52380600, 0.23971510],
           [0.87355555, 0.53077744, 0.24735548],
           [0.87395712, 0.53772697, 0.25505684],
           [0.87432861, 0.54465512, 0.26281981],
           [0.87467085, 0.55156232, 0.27064498],
           [0.87498503, 0.55844876, 0.27853263],
           [0.87527217, 0.56531471, 0.28648326],
           [0.87553313, 0.57216055, 0.29449756],
           [0.87576930, 0.57898630, 0.30257577],
           [0.87598171, 0.58579221, 0.31071851],
           [0.87617147, 0.59257844, 0.31892638],
           [0.87634020, 0.59934489, 0.32719953],
           [0.87648888, 0.60609181, 0.33553878],
           [0.87661914, 0.61281908, 0.34394439],
           [0.87673240, 0.61952670, 0.35241687],
           [0.87683016, 0.62621463, 0.36095669],
           [0.87691421, 0.63288268, 0.36956410],
           [0.87698607, 0.63953083, 0.37823972],
           [0.87704779, 0.64615877, 0.38698363],
           [0.87710104, 0.65276640, 0.39579639],
           [0.87714801, 0.65935338, 0.40467811],
           [0.87719069, 0.66591948, 0.41362916],
           [0.87723137, 0.67246435, 0.42264965],
           [0.87727233, 0.67898764, 0.43173978],
           [0.87731605, 0.68548896, 0.44089961],
           [0.87736509, 0.69196788, 0.45012917],
           [0.87742214, 0.69842394, 0.45942844],
           [0.87749005, 0.70485663, 0.46879727],
           [0.87757175, 0.71126545, 0.47823549],
           [0.87767038, 0.71764981, 0.48774277],
           [0.87778914, 0.72400915, 0.49731878],
           [0.87793145, 0.73034282, 0.50696296],
           [0.87810081, 0.73665020, 0.51667477],
           [0.87830092, 0.74293060, 0.52645341],
           [0.87853556, 0.74918334, 0.53629808],
           [0.87880873, 0.75540769, 0.54620771],
           [0.87912449, 0.76160293, 0.55618122],
           [0.87948712, 0.76776830, 0.56621720],
           [0.87990092, 0.77390307, 0.57631429],
           [0.88037047, 0.78000643, 0.58647070],
           [0.88090027, 0.78607767, 0.59668473],
           [0.88149514, 0.79211598, 0.60695418],
           [0.88215974, 0.79812065, 0.61727700],
           [0.88289909, 0.80409090, 0.62765056],
           [0.88371798, 0.81002606, 0.63807240],
           [0.88462153, 0.81592540, 0.64853946],
           [0.88561459, 0.82178829, 0.65904886],
           [0.88670229, 0.82761408, 0.66959711],
           [0.88788952, 0.83340224, 0.68018083],
           [0.88918122, 0.83915225, 0.69079625],
           [0.89058234, 0.84486362, 0.70143930],
           [0.89209744, 0.85053601, 0.71210615],
           [0.89373153, 0.85616903, 0.72279183],
           [0.89548875, 0.86176252, 0.73349245],
           [0.89737373, 0.86731625, 0.74420272],
           [0.89939058, 0.87283016, 0.75491787],
           [0.90154313, 0.87830429, 0.76563309],
           [0.90383561, 0.88373862, 0.77634217],
           [0.90627132, 0.88913338, 0.78704028],
           [0.90885368, 0.89448881, 0.79772179],
           [0.91158625, 0.89980515, 0.80838000],
           [0.91447204, 0.90508277, 0.81900898],
           [0.91751403, 0.91032207, 0.82960244],
           [0.92071527, 0.91552347, 0.84015333],
           [0.92407894, 0.92068737, 0.85065379],
           [0.92760832, 0.92581419, 0.86109531],
           [0.93130674, 0.93090430, 0.87146916],
           [0.93517804, 0.93595804, 0.88176475],
           [0.93922654, 0.94097572, 0.89196965],
           [0.94345707, 0.94595767, 0.90206897],
           [0.94787482, 0.95090438, 0.91204440],
           ]

CMAP_EXPOSURES = mpl.colors.LinearSegmentedColormap.from_list('cmr.sunburst', cm_data1, N=256).reversed()
CMAP_EXPOSURES.set_under('lightgray')
CMAP_IMPACT = mpl.colors.LinearSegmentedColormap.from_list('cmr.flamingo', cm_data2, N=256).reversed()
CMAP_IMPACT.set_under('lightgray')
"""Default sequential colormaps, taken from https://cmasher.readthedocs.io/index.html"""

CMAP_RASTER = 'viridis'

CMAP_CAT = 'Dark2'