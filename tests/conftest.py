#!/usr/bin/python3

import pytest


@pytest.fixture(scope="session")
def Router(project):
    return project.router.at("0x99a58482BD75cbab83b27EC03CA68fF489b5788f")


@pytest.fixture(scope="session")
def USDT(project):
    return project.usdt.at("0xdAC17F958D2ee523a2206206994597C13D831ec7")
