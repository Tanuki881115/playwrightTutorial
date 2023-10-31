import ba_flow
import pytest


class TestBaFlow:
    def test_ba_flow(self):
        ba_flow.run_ba_flow()

    @pytest.mark.regression
    def test_ba_flow_2(self):
        # Creating custom marker named regression which can be run separately
        # pytest -m regression
        ba_flow.run_ba_flow()