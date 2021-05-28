# Copyright 2021 Øyvind Bratne

# This file is part of Git-pr
#
# Git-pr is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Git-pr is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Git-pr.  If not, see <https://www.gnu.org/licenses/>.


import argparse
import logging
import subprocess
import unittest
import os
import sys


def runcmd(cmd):
    try:
        ret = subprocess.run(cmd.split(), capture_output=True)
        return (ret.stdout, ret.stderr, ret.returncode)
    except Exception as ex:
        # logging.warning("Error: %s" % (ex))
        raise ex
        # return [None]*3


class TestFunctions(unittest.TestCase):
    def test_errorcmd(self):
        # Working command
        ret = runcmd("zsh --version")
        self.assertTrue(ret[0] is not None)

    def test_erroneousflags(self):
        # LS command with erroneous flags
        ret = runcmd("ls -atert")
        logging.debug(ret)
        self.assertTrue(ret[2] > 0)

    def test_nonexisting(self):
        # non-existing command
        with self.assertRaises(Exception):
            runcmd("iouerhfi iuwf")

    def test_initlogging(self):
        initlogging()
        logger = logging.getLogger()
        self.assertTrue(logger.level == logging.WARNING)

    def test_initlogging_debug(self):
        initlogging(True)
        logger = logging.getLogger()
        self.assertTrue(logger.level == logging.DEBUG)

    def test_checkdeps(self):
        checkdeps()
        self.assertTrue(True)

    def test_checkdeps_raise(self):
        with self.assertRaises(Exception):
            checkdeps(["awefw asodiuf"])

    def test_pr(self):
        # TODO: assert pr function is working properly
        pr()

    def test_test(self):
        # TODO: assert pr function is working properly
        test()


def checkdeps(apps=["gh version", "az version"]):
    for app in apps:
        try:
            (sout, serr, scode) = runcmd(app)
        except Exception as ex:
            raise("Command doesn't exist on the system: %s. Quitting" % (app))

        logging.debug("Status: %s" % (sout.decode("utf-8")))
        logging.debug("Res: %s" % (serr.decode("utf-8")))
        logging.debug("Rcode: %s" % (scode))


def initlogging(enabledebug=False):
    logger = logging.getLogger()
    if(enabledebug):
        logger.setLevel(logging.DEBUG)

    loghandler = logging.StreamHandler()
    loghandler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    if(enabledebug):
        loghandler.setLevel(logging.DEBUG)

    logger.addHandler(loghandler)


def pr():
    None


def test():
    None


if __name__ == "__main__":
    # Determine current folder git repository
    try:
        parser = argparse.ArgumentParser(description="")
        sparser = parser.add_subparsers(dest="command", required=True)
        sparser.add_parser("bootstrap")
        sparser.add_parser("test")
        parser.add_argument("-d",
                            "--debug",
                            help="Enable debugging",
                            action="store_true")
        sspartser = sparser.add_parser("pr")
        args = parser.parse_args()
        initlogging(args.debug)
        commandmap = {"bootstrap": "checkdeps()",
                      "test": "test()",
                      "pr": "pr()"}
        if args.command:
            logging.debug("Command being called: %s" % (args.command))
            eval(commandmap[args.command])
    except Exception as ex:
        logging.error(ex)
        sys.exit(1)
