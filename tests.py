
import unittest
from pysenbug import pysenbug


class TestPysenbug(unittest.TestCase):
    """ Due to the intentionally unpredictable nature of some of pysenbug's
    use cases, there is no simple deterministic test that will always
    conclusively prove that the function worked as intended in a finite number
    of steps; though for sufficiently large test cases, it is exceedingly
    unlikely the results would fall outside of calculable probability
    distributions.

    In the interest of making dependable tests, all default tests have been
    designed to be deterministic in nature.

    It is possible to create tests that determine if pysenbug is working as
    expected even when random functions are used using scary, highly invasive code inspection.
    (This feature will be implemented pending ethics committee review.)
    """

    def test_unparameterized_decorator(self):
        """ Use the shotgun approach to check for random exceptions. """

        for each_iteration in range(0, 100):

            @pysenbug
            def open_box():
                return 'meow'

            for each_iteration in range(0, 1000):
                open_box()

    def test_chance_parameter(self):
        """ Test whether or not the `chance` parameter works as expected when
        given values of 0 or 1. """

        for each_iteration in range(0, 100):

            @pysenbug(chance=1)
            def lead_box():
                return 'miao'

            for each_iteration in range(0, 1000):
                self.assertEqual(lead_box(), 'miao')

        for each_iteration in range(0, 100):

            @pysenbug(chance=0)
            def polonium_box():
                return 'miao'

            for each_iteration in range(0, 1000):
                self.assertEqual(polonium_box(), None)

    def test_return_value_parameter(self):
        """ Test that the `return_value` parameter works as expected. """

        for each_iteration in range(0, 100):

            @pysenbug(return_value='bark', chance=0)
            def uranium_box():
                return 'miow'

            for each_iteration in range(0, 1000):
                self.assertEqual(uranium_box(), 'bark')

        for each_iteration in range(0, 100):

            @pysenbug(return_value='bark', chance=1)
            def lead_lined_uranium_box():
                return 'miow'

            for each_iteration in range(0, 1000):
                self.assertEqual(lead_lined_uranium_box(), 'miow')

    def test_probability_function_parameter(self):
        """ Test whether or not the `probability_function` parameter works as
        expected. """

        def hidden_variable():
            while True:
                yield False
                yield True

        for each_iteration in range(0, 100):

            bohm_interpretation = hidden_variable()

            @pysenbug(probability_function=bohm_interpretation.next)
            def bismuth_box():
                return 'miau'

            for each_iteration in range(0, 1000):
                if each_iteration % 2 == 0:
                    self.assertEqual(bismuth_box(), 'miau')
                else:
                    self.assertEqual(bismuth_box(), None)


if __name__ == '__main__':
    # Not Yet Implemented:
    # Add command line argument support for optional nondeterministic testing!
    unittest.main()
