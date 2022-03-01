#!/usr/bin/env python
# -*- coding: utf-8 -*-
from uhash import uhash


def test_encode():
    assert uhash.encode("8400486893347242") == "pjsEpbWSrltOP25F9ws4GjnoZHZ3lper"


def test_decode():
    assert uhash.decode("pjsEpbWSrltOP25F9ws4GjnoZHZ3lper") == "8400486893347242"
