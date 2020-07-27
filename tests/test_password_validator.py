# -*- coding: utf-8 -*-

import unittest
import sys
import pytest

sys.path.append("..")

from main import *

class TestClass(unittest.TestCase):

    def test_minimum_password(self):
        text = "aaa"
        assert min_password_check(text)

    def test_maximum_password(self):
        text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        assert max_password_check(text)

    def test_not_ascii(self):
        text = u'aaa˚'
        assert not_ascii_check(text)

    def test_common_password(self):
        root = Node("*")
        add(root, "weakpassword")
        assert weak_password_check(root, "weakpassword")
        assert not weak_password_check(root, "strongpassword")

    def test_weak_password_file_provided(self):
        root = Node("*")
        with pytest.raises(SystemExit):
            build_trie(root)

   