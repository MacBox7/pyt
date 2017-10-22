import os.path

from .base_test_case import BaseTestCase
from pyt.project_handler import get_directory_modules, get_modules_and_packages
from pyt.utils.log import enable_logger, logger
enable_logger(to_file='./pyt.log')


class NestedTest(BaseTestCase):
    def test_nested_user_defined_function_calls(self):

        path = os.path.normpath('example/nested_functions_code/nested_user_defined_function_calls.py')

        project_modules = get_modules_and_packages(os.path.dirname(path))
        local_modules = get_directory_modules(os.path.dirname(path))

        self.cfg_create_from_file(path, project_modules, local_modules)

        EXPECTED = ["Entry module",
                    "foo = 'bar'",
                    "save_1_foo = foo",
                    "save_2_foo = foo",
                    "temp_2_inner_arg = foo",
                    "inner_arg = temp_2_inner_arg",
                    "Function Entry inner",
                    "inner_ret_val = inner_arg + 'hey'",
                    "ret_inner = inner_ret_val",
                    "Exit inner",
                    "foo = save_2_foo",
                    "¤call_2 = ret_inner",
                    "temp_1_outer_arg = ¤call_2",
                    "outer_arg = temp_1_outer_arg",
                    "Function Entry outer",
                    "outer_ret_val = outer_arg + 'hey'",
                    "ret_outer = outer_ret_val",
                    "Exit outer",
                    "foo = save_1_foo",
                    "¤call_1 = ret_outer",
                    "abc = ¤call_1",
                    "Exit module"]

        logger.debug("Nodes are:")
        for node in self.cfg.nodes:
        	logger.debug("%s", node.label)

        for node, expected_label in zip(self.cfg.nodes, EXPECTED):
            self.assertEqual(node.label, expected_label)

    def test_builtin_with_user_defined_inner(self):

        path = os.path.normpath('example/nested_functions_code/builtin_with_user_defined_inner.py')

        project_modules = get_modules_and_packages(os.path.dirname(path))
        local_modules = get_directory_modules(os.path.dirname(path))

        self.cfg_create_from_file(path, project_modules, local_modules)

        EXPECTED = ["TODO"]

        logger.debug("Nodes are:")
        for node in self.cfg.nodes:
            logger.debug("%s", node.label)

        # for node, expected_label in zip(self.cfg.nodes, EXPECTED):
        #     self.assertEqual(node.label, expected_label)
            
    # def test_nested_string_interpolation(self):

    #     path = os.path.normpath('example/nested_functions_code/nested_string_interpolation.py')

    #     project_modules = get_modules_and_packages(os.path.dirname(path))
    #     local_modules = get_directory_modules(os.path.dirname(path))

    #     self.cfg_create_from_file(path, project_modules, local_modules)

    #     EXPECTED = ['Not Yet']

    #     logger.debug("Nodes are:")
    #     for node in self.cfg.nodes:
    #     	logger.debug("%s", node)

    #     for node, expected_label in zip(self.cfg.nodes, EXPECTED):
    #         self.assertEqual(node.label, expected_label)
