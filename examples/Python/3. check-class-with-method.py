# Проверяем класс с аргументами при инициализации, метод внутри этого класса с аргументами, метод без аргументов и атрибут

import os
import sys

dirname = os.path.dirname(__file__)
module_path = os.path.join(dirname, "..")
sys.path.append(module_path)

from AbstractTest2 import AbstractTest2, RunCode, process, wrapper

CORRECT_CODE = r"""
class Answer:
    just_attr = "I can check it without creating an object"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func_without_args(self):
        print("I dontt need any arguments!")

    def pow(self, x, y):
        return x**y
"""

CORRECT_CODE_LANGUAGE = "Python"


class Tests(AbstractTest2):
    def test_1(self):
        # Проверяем атрибут just_attr, для которого не нужно создание экземпляра класса
        class_name = "Answer"
        class_args = ""
        method_name = ""
        var_name = ""
        attr_name = "just_attr"
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
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
        # Проверяем атрибут name, для которого НУЖНО создание экземпляра класса
        class_name = "Answer"
        class_args = {
            "name": "IT Resume",
            "age": 50,
        }
        method_name = ""
        var_name = ""
        attr_name = "name"
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
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

    def test_3(self):
        # Проверяем атрибут age, для которого НУЖНО создание экземпляра класса
        class_name = "Answer"
        class_args = {
            "name": "IT Resume",
            "age": 50,
        }
        method_name = ""
        var_name = ""
        attr_name = "age"
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
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

    def test_4(self):
        # Проверяем метод func_without_args, для которого НУЖНО создание экземпляра класса
        # Но при этом в него не нужно передавать аргументы
        # К тому же, в нем уже есть print
        class_name = "Answer"
        class_args = {
            "name": "IT Resume",
            "age": 50,
        }
        method_name = "func_without_args"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        # Обратите внимание - поменяли флаг, т.к. уже есть print
        need_print = False
        add_before = ""
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

    def test_5(self):
        # Проверяем метод pow, для которого НУЖНО создание экземпляра класса
        # Но при этом в него НУЖНО передавать аргументы
        # И print для него также НУЖЕН
        class_name = "Answer"
        class_args = {
            "name": "IT Resume",
            "age": 50,
        }
        method_name = "pow"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        # В этом тесте вернули флаг обратно
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            "x": 5,
            "y": 2,
        }

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
