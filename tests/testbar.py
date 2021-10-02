import unittest
from charts.bar import draw_figure1

class TestBar(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_demo(self):
        groups = {"group1":5.3, "group2":15}
        draw_figure1(groups=groups)

    def test_figure1(self):
        pass
