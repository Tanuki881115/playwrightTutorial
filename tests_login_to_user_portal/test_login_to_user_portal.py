import login_to_user_portal
import pytest


class TestLoginToUserPortal:
    def test_login_to_user_portal(self):
        login_to_user_portal.run_login_to_user_portal()

    @pytest.mark.skip(reason="Not Ready!!!")
    def test_login_to_user_portal_2(self):
        # This test will be skipped by pytest
        login_to_user_portal.run_login_to_user_portal()

    @pytest.mark.xfail(reason="URL not READY!!!")
    def test_login_to_user_portal_3(self):
        # This test will be expected to be fail
        login_to_user_portal.run_login_to_user_portal()

    def test_login_to_user_portal_4(self):
        login_to_user_portal.run_login_to_user_portal()
