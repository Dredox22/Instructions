# Проверяем функцию с разными видами аргументов

import os
import sys

dirname = os.path.dirname(__file__)
module_path = os.path.join(dirname, "..")
sys.path.append(module_path)

from AbstractTest2 import AbstractTest2, RunCode, process, wrapper

CORRECT_CODE = r"""
import pandas as pd

# считываем датафрейм в переменную df из файла 1.csv
df = pd.read_csv('1.csv')

# создаем функцию foo, которая принимает на вход произвольную строку датафрейма в аргументе row, число cnt и словарь d. а также позиционный аргумент с произвольным массивом
def foo(row, cnt, d):
    # здесь что-то происходит
    return
"""

CORRECT_CODE_LANGUAGE = "Python"


class Tests(AbstractTest2):
    def test_1(self):
        class_name = ""
        class_args = ""
        method_name = "foo"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            "cnt": 2,
            "d": {1: "a", 2: "b"},
            "__itresume_noname_1": [1, 2, 3],
        }

        fake_arguments = {
            "row": "df.iloc[1, :]",
        }

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
        # А теперь передаем те же самые аргументы, только с другими значениями
        class_name = ""
        class_args = ""
        method_name = "foo"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            "cnt": 100,
            "d": {100: "a", 200: "b"},
            "__itresume_noname_1": [100, 200, 300],
        }

        fake_arguments = {
            "row": "df.iloc[100, :]",
        }

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

    def test_3(self):
        # А теперь передаем те же самые аргументы, только с другими значениями
        class_name = ""
        class_args = ""
        method_name = "foo"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            "cnt": 1000,
            "d": {1000: "a", 2000: "b"},
            "__itresume_noname_1": [1000, 2000, 3000],
        }

        fake_arguments = {
            "row": "df.iloc[1000, :]",
        }

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
