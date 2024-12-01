import unittest
import logging
import rt_with_exceptions as rr


logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest1(unittest.TestCase):


    def test_walk(self):
        try:
            walk_ = rr.Runner('man', -5)
            for _ in range(10):
                walk_.walk()
            self.assertEqual(walk_.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner. \n{e}')

    def test_run(self):
        try:
            run_ = rr.Runner(5)
            for _ in range(10):
                run_.run()
            self.assertEqual(run_.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner. \n{e}')


if __name__ == '__main__':
    unittest.main()