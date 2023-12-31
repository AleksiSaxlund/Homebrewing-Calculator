import unittest
from services.calculations_services import CalculationsService
from entities.recipe import Recipe
from entities.all_ingredients import Malt, Hop, Yeast


class TestCalculationsService(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipe()

        self.recipe.ingredients["malts"] = [
            Malt("test malt 1", 37.0, 10), Malt("test malt 2", 12.4, 5)]

        self.recipe.ingredients["hops"] = [
            Hop("test hop 1", 5.5), Hop("test hop 2", 2.1)]

        self.recipe.ingredients["yeasts"] = [
            Yeast("test yeast", 0.75, "12-50")]

        self.recipe.volume = 5
        self.recipe.ingredients["malts"][0].amount = 5
        self.recipe.ingredients["malts"][1].amount = 2
        self.recipe.ingredients["hops"][0].amount = 1
        self.recipe.ingredients["hops"][1].amount = 5.5
        self.calculator = CalculationsService(self.recipe)

    def test_original_gravity_calculations(self):
        og = self.calculator.calculate_original_gravity()

        self.assertAlmostEqual(og, 29.372)

    def test_original_gravity_calculations_with_no_malts(self):
        self.recipe.ingredients["malts"] = []
        og = self.calculator.calculate_original_gravity()

        self.assertAlmostEqual(og, 1.0)

    def test_color_calculations(self):
        srm = self.calculator.calculate_color()

        self.assertAlmostEqual(srm, 8.20)

    def test_color_calculations_with_no_malts(self):
        self.recipe.ingredients["malts"] = []
        srm = self.calculator.calculate_color()

        self.assertAlmostEqual(srm, 0.00)

    def test_color_calculation_with_no_volume(self):
        self.recipe.volume = 0
        srm = self.calculator.calculate_color()

        self.assertAlmostEqual(srm, 0.00)

    def test_final_gravity_calculations(self):
        fg = self.calculator.calculate_final_gravity()

        self.assertAlmostEqual(fg, 6.497075)

    def test_final_gravity_calculation_with_no_malts(self):
        self.recipe.ingredients["malts"] = []
        fg = self.calculator.calculate_final_gravity()

        self.assertAlmostEqual(fg, 1.000)

    def test_final_gravity_calculation_with_no_yeasts(self):
        self.recipe.ingredients["yeasts"] = []
        fg = self.calculator.calculate_final_gravity()

        self.assertAlmostEqual(fg, 29.372)

    def test_abv_calculations(self):
        abv = self.calculator.calculate_abv()

        self.assertAlmostEqual(abv, 3.0)

    def test_ibu_calculations(self):
        ibu = self.calculator.calculate_ibu()

        self.assertAlmostEqual(ibu, 70.4834724)

    def test_ibu_calculation_with_no_hops(self):
        self.recipe.ingredients["hops"] = []
        ibu = self.calculator.calculate_ibu()

        self.assertAlmostEqual(ibu, 0)

    def test_get_all_calculations(self):
        results = []
        expected_results = [29.372, 6.497075, 3.0, 8.20, 70.4834724]
        original_gravity, final_gravity, abv, color, ibu = self.calculator.get_all_calculations()
        results.append(float(original_gravity))
        results.append(float(final_gravity))
        results.append(float(abv))
        results.append(float(color))
        results.append(float(ibu))

        for i in range(len(results)):
            self.assertAlmostEqual(results[i], expected_results[i])
