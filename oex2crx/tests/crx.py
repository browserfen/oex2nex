#!/usr/bin/env python

import unittest
import os
import zipfile
import subprocess


class TestCRX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.call("python convertor.py -x tests/fixtures/manifest-test.oex tests/fixtures/converted/manifest-test",
                        shell=True)
        subprocess.call("python convertor.py -x tests/fixtures/manifest-test-dir tests/fixtures/converted/manifest-test-dir",
                        shell=True)

    @classmethod
    def tearDownClass(cls):
        subprocess.call("rm -r tests/fixtures/converted/*", shell=True)

    def test_crx_exists(self):
        self.assertTrue(os.path.isfile("tests/fixtures/converted/manifest-test.crx"))

    def test_crx_exists_from_dir(self):
        self.assertTrue(os.path.isfile("tests/fixtures/converted/manifest-test-dir.crx"))

    def test_crx_files(self):
        crx = zipfile.ZipFile("tests/fixtures/converted/manifest-test.crx", "r")
        # we expect these files to get copied over
        expected = ["manifest.json", "hello.png", "popup.html", "index.html",
                    "oex_shim/operaextensions_popup.js",
                    "oex_shim/popup_resourceloader.html",
                    "oex_shim/popup_resourceloader.js",
                    "oex_shim/operaextensions_background.js",
                    "inline_script_index_1.js"]
        for file in expected:
            self.assertIn(file, crx.namelist())
        #config.xml shouldn't get copied over
        self.assertNotIn("config.xml", crx.namelist())

    def test_crx_files_from_dir(self):
        crx = zipfile.ZipFile("tests/fixtures/converted/manifest-test-dir.crx", "r")
        # we expect these files to get copied over
        expected = ["manifest.json", "hello.png", "popup.html", "index.html",
                    "oex_shim/operaextensions_popup.js",
                    "oex_shim/popup_resourceloader.html",
                    "oex_shim/popup_resourceloader.js",
                    "oex_shim/operaextensions_background.js",
                    "inline_script_index_1.js"]
        for file in expected:
            self.assertIn(file, crx.namelist())
        #config.xml shouldn't get copied over
        self.assertNotIn("config.xml", crx.namelist())