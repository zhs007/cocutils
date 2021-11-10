# -*- coding:utf-8 -*-
import pytest
from utils import loadVersion


def test_loadVersion():
    ver = loadVersion()

    assert ver == 'v0.1.3'
