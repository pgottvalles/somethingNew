import unittest
import os
import importlib
import sys

import test_stack_after_purchase

CURRENT = os.path.realpath(__file__)
repo_dir = os.path.abspath(os.path.join(CURRENT, os.pardir, os.pardir))
sys.path.append(os.path.normpath(os.path.join(repo_dir, 'vendingmachine')))
sys.path.append(os.path.normpath(os.path.join(repo_dir, 'vendingmachine', 'application')))
sys.path.append(os.path.normpath(repo_dir))


def suite():
    """Add all test cases from Python module in tests-folder that begin with
    test_ prefix."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    modules_to_test = []
    test_dir = os.listdir('tests')
    for test_module_name in test_dir:
        if test_module_name.startswith('test') and test_module_name.endswith('.py'):
            modules_to_test.append('tests.' + test_module_name.rstrip('.py'))

    for module in map(importlib.import_module, modules_to_test):
        suite.addTests(loader.loadTestsFromModule(module))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())