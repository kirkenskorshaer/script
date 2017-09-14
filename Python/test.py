import unittest
import modules.redmine.user_test
import modules.redmine.redmine_handler_test
import modules.util.file_helper_test
import modules.util.password_generator_test

suite = unittest.TestSuite()

suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(modules.redmine.user_test))
suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(modules.redmine.redmine_handler_test))

suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(modules.util.file_helper_test))
suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(modules.util.password_generator_test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
