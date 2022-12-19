# Указываем специфического пользователя

import os
import sys

dirname = os.path.dirname(__file__)
module_path = os.path.join(dirname, "..")
sys.path.append(module_path)

from AbstractTest2 import AbstractTest2, RunCode, process, wrapper

CORRECT_QUERY = """
select
	user_id,
	count(distinct case when is_false = 0 then problem_id end) as cnt
from codesubmit c
group by user_id
"""


class Tests(AbstractTest2):
    def test_1(self):
        self.sql_test(
            correct_query=CORRECT_QUERY,
            ignore_order=True,
            # Добавляем имя пользователя
            user="simulative",
        )
