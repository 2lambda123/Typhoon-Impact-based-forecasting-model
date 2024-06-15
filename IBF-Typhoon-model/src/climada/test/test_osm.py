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

Integration Test for open_street_map.py and 3 time consuming unit tests
"""

import math
import unittest
import geopandas

from climada import CONFIG
from climada.entity import Exposures
from climada.entity.exposures import open_street_map as OSM
import secrets

DATA_DIR = CONFIG.test_data.dir()

class TestOpenStreetMapModule(unittest.TestCase):
    def test_get_features_osm(self):
        """        Test the function get_features_osm.

        This function tests the get_features_osm function by providing a
        bounding box, tags, data directory, and check_plot parameter. It asserts
        the instance type of the returned GeoDataFrame, checks for specific
        geometry types, and verifies the presence of certain items in the
        GeoDataFrame. Finally, it asserts the number of columns in the
        GeoDataFrame.
        """
        Low_Value_gdf_47_8 = OSM.get_features_OSM([47.2, 8.0, 47.3, 8.07],
                                                  {'waterway', 'landuse=forest'},
                                                  DATA_DIR, check_plot=0)
        self.assertIsInstance(Low_Value_gdf_47_8, geopandas.GeoDataFrame)
        self.assertNotIn('LineString', Low_Value_gdf_47_8.geometry.type)
        self.assertTrue('waterway' in Low_Value_gdf_47_8.Item.unique())
        self.assertTrue('landuse=forest' in Low_Value_gdf_47_8.Item.unique())
        self.assertEqual(len(Low_Value_gdf_47_8.columns), 6)

    def test_get_highValueArea(self):
        """        Test the function get_highValueArea.

        This function tests the get_highValueArea function by providing a
        bounding box coordinates, a data directory path, a shapefile path, and a
        check_plot parameter. It then asserts if the returned GeoDataFrame has
        the expected minimum y and maximum x values within a certain tolerance,
        and if the returned object is an instance of GeoDataFrame.
        """
        High_Value_gdf_47_8 = OSM.get_highValueArea([47.2, 8.0, 47.3, 8.07], DATA_DIR,
                                                    DATA_DIR.joinpath('OSM_features_47_8.shp'),
                                                    check_plot=0)
        self.assertTrue(math.isclose(47.2, High_Value_gdf_47_8.bounds.miny, rel_tol=0.05))
        self.assertTrue(math.isclose(8.07, High_Value_gdf_47_8.bounds.maxx, rel_tol=0.05))
        self.assertIsInstance(High_Value_gdf_47_8, geopandas.GeoDataFrame)

    def test_get_osmstencil_litpop(self):
        """        Test the function get_osmstencil_litpop.

        This function tests the get_osmstencil_litpop function for different
        modes of operation. It calls the function with specific parameters and
        asserts the expected outcomes.
        """
        for mode in ['proportional', 'nearest', 'even']:
            exposure_high_47_8 = OSM.get_osmstencil_litpop(
                [47.2, 8.0, 47.3, 8.07], 'CHE', mode,
                DATA_DIR.joinpath('High_Value_Area_47_8.shp'),
                DATA_DIR, check_plot=0, reference_year=2016)
            self.assertIsInstance(exposure_high_47_8, Exposures)
            self.assertEqual(len(exposure_high_47_8.gdf.columns), 8)
            self.assertGreater(
                exposure_high_47_8.gdf.iloc[secrets.SystemRandom().randint(0, len(exposure_high_47_8.gdf))].value,
                0)

    def test_make_osmexposure(self):
        """        Test the functionality of the make_osmexposure method in the OSM class.

        This test function checks the output of the make_osmexposure method for
        two different modes: 1. Default mode with CHF 5400/m2 values. 2. LitPop
        mode with specific country and reference year.

        Args:
            self: Instance of the test class.
        """
        # With default 5400 Chf / m2 values
        buildings_47_8_default = OSM.make_osmexposure(
            DATA_DIR.joinpath('buildings_47_8.shp'),
            mode='default', save_path=DATA_DIR, check_plot=0)
        self.assertIsInstance(buildings_47_8_default, Exposures)
        self.assertEqual(len(buildings_47_8_default.gdf.columns), 12)
        self.assertEqual(
            buildings_47_8_default.gdf.loc[
                secrets.SystemRandom().randint(0, len(buildings_47_8_default.gdf))].geometry.type,
            "Point")
        self.assertGreater(
            buildings_47_8_default.gdf.loc[secrets.SystemRandom().randint(0, len(buildings_47_8_default.gdf))].value,
            0)
        self.assertGreater(
            buildings_47_8_default.gdf.loc[
                secrets.SystemRandom().randint(0, len(buildings_47_8_default.gdf))].projected_area,
            0)

        # With LitPop values
        buildings_47_8_LitPop = OSM.make_osmexposure(DATA_DIR.joinpath('buildings_47_8.shp'),
                                                     country='CHE', mode="LitPop",
                                                     save_path=DATA_DIR, check_plot=0,
                                                     reference_year=2016)
        self.assertIsInstance(buildings_47_8_LitPop, Exposures)
        self.assertEqual(len(buildings_47_8_LitPop.gdf.columns), 12)
        self.assertEqual(
            buildings_47_8_LitPop.gdf.loc[secrets.SystemRandom().randint(0, len(buildings_47_8_LitPop.gdf))].geometry.type,
            "Point")
        self.assertGreater(
            buildings_47_8_LitPop.gdf.loc[secrets.SystemRandom().randint(0, len(buildings_47_8_LitPop.gdf))].value,
            0)
        self.assertGreater(
            buildings_47_8_LitPop.gdf.loc[
                secrets.SystemRandom().randint(0, len(buildings_47_8_LitPop.gdf))].projected_area,
            0)

        for mode in ['default', 'LitPop']:
            DATA_DIR.joinpath('exposure_buildings_' + mode + '_47_7.h5').unlink()


class TestOSMlongUnitTests(unittest.TestCase):

    def test_get_litpop_bbox(self):
        """        Test the _get_litpop_bbox function within the get_osmstencil_litpop
        function.

        This function tests the _get_litpop_bbox function by providing a country
        code, a GeoDataFrame representing high value areas, and a reference
        year. It then asserts that the latitude and longitude values of the
        resulting GeoDataFrame subset are close to the bounds of the high value
        area GeoDataFrame.
        """
        # Define and load parameters
        country = 'CHE'
        highValueArea = geopandas.read_file(DATA_DIR.joinpath('High_Value_Area_47_8.shp'))
        # Execute function
        exp_sub = OSM._get_litpop_bbox(country, highValueArea, reference_year=2016)
        self.assertTrue(
            math.isclose(min(exp_sub.gdf.latitude), highValueArea.bounds.miny, rel_tol=1e-2))
        self.assertTrue(
            math.isclose(max(exp_sub.gdf.longitude), highValueArea.bounds.maxx, rel_tol=1e-2))

    def test_split_exposure_highlow(self):
        """        Test the _split_exposure_highlow function within the
        get_osmstencil_litpop function.

        This function tests the _split_exposure_highlow function by executing it
        with different modes and checking the results against the expected
        values.
        """
        # Define and load parameters:
        country = 'CHE'  # this takes too long for unit test probably
        highValueArea = geopandas.read_file(DATA_DIR.joinpath('High_Value_Area_47_8.shp'))
        exp_sub = OSM._get_litpop_bbox(country, highValueArea, reference_year=2016)
        High_Value_Area_gdf = geopandas.read_file(DATA_DIR.joinpath('High_Value_Area_47_8.shp'))
        # execute function
        for mode in {'proportional', 'even'}:
            print('testing mode %s' % mode)
            exp_sub_high = OSM._split_exposure_highlow(exp_sub, mode, High_Value_Area_gdf)
            self.assertTrue(math.isclose(sum(exp_sub_high.gdf.value),
                                         sum(exp_sub.gdf.value),
                                         rel_tol=0.01))
            exp_sub_high.check()
        print('testing mode nearest neighbour')
        exp_sub_high = OSM._split_exposure_highlow(exp_sub, "nearest", High_Value_Area_gdf)
        self.assertTrue(math.isclose(sum(exp_sub_high.gdf.value), sum(exp_sub.gdf.value), rel_tol=0.1))
        exp_sub_high.check()

    def test_assign_values_exposure(self):
        """        Test the _assign_values_exposure function within the make_osmexposure
        function.

        This function tests the _assign_values_exposure function by providing
        input parameters and checking the output High_Value_Area_gdf for values
        greater than 0.

        Args:
            self: Instance of the test class.
        """
        # Define and load parameters:
        # function tested previously
        building_gdf = OSM._get_midpoints(DATA_DIR.joinpath('buildings_47_8.shp'))
        mode = 'LitPop'     # mode LitPop takes too long for unit test, moved to integration test
        country = 'CHE'
        # Execute function
        High_Value_Area_gdf = OSM._assign_values_exposure(building_gdf, mode,
                                                          country, reference_year=2016)
        self.assertGreater(
            High_Value_Area_gdf.loc[secrets.SystemRandom().randint(0, len(High_Value_Area_gdf))].value,
            0)

# Execute Tests
if __name__ == "__main__":
    TESTS = unittest.TestLoader().loadTestsFromTestCase(TestOpenStreetMapModule)
    TESTS.addTests(unittest.TestLoader().loadTestsFromTestCase(TestOSMlongUnitTests))
    unittest.TextTestRunner(verbosity=2).run(TESTS)
