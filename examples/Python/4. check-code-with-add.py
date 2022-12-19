# Напишем тест для кода, в который нужно добавлять что-то в начало и в конец

import os
import sys

dirname = os.path.dirname(__file__)
module_path = os.path.join(dirname, "..")
sys.path.append(module_path)

from AbstractTest2 import AbstractTest2, RunCode, process, wrapper

CORRECT_CODE = r"""
# создаем переменную var и записываем в нее длину массива users
# предполагается, что массив users определен нами заранее
# а проверить нам в итоге надо результат, а также тип переменной var
var = len(users)
"""

CORRECT_CODE_LANGUAGE = "Python"


class Tests(AbstractTest2):
    def test_1(self):
        # проверяем результат
        class_name = ""
        class_args = ""
        method_name = ""
        var_name = "var"
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = """
        users = [1, 2, 3]
        """
        add_after = ""

        arguments = {}

        fake_arguments = {}

        self.default_test(
            class_name=class_name,
            class_args=class_args,
            method_name=method_name,
            attr_name=attr_name,
            need_to_eval=need_to_eval,
            arguments=arguments,
            fake_arguments=fake_arguments,
            correct_code=CORRECT_CODE,
            correct_code_language=CORRECT_CODE_LANGUAGE,
            var_name=var_name,
            formulation=formulation,
            need_print=need_print,
            add_before=add_before,
            add_after=add_after,
        )

    def test_2(self):
        # проверяем тип переменной var
        class_name = ""
        class_args = ""
        method_name = ""
        # var_name ссылается на var_type, который мы определили в add_after
        var_name = "var_type"
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = """
        users = [1, 2, 3]
        """
        add_after = """
        var_type = type(var)
        """

        arguments = {}

        fake_arguments = {}

        self.default_test(
            class_name=class_name,
            class_args=class_args,
            method_name=method_name,
            attr_name=attr_name,
            need_to_eval=need_to_eval,
            arguments=arguments,
            fake_arguments=fake_arguments,
            correct_code=CORRECT_CODE,
            correct_code_language=CORRECT_CODE_LANGUAGE,
            var_name=var_name,
            formulation=formulation,
            need_print=need_print,
            add_before=add_before,
            add_after=add_after,
        )
