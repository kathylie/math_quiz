import unittest
from unittest.mock import patch
from main_quiz import SimpleMathQuiz  

class TestSimpleMathQuiz(unittest.TestCase):
    def setUp(self):
        self.math_quiz = SimpleMathQuiz()

    @patch('builtins.input', side_effect=['1', '5', '10'])
    def test_run_quiz_correct_answer(self, mock_input):
        self.math_quiz.run_quiz()
        self.assertEqual(self.math_quiz.num_correct, 1)

    @patch('builtins.input', side_effect=['1', '5', '2'])
    def test_run_quiz_wrong_answer(self, mock_input):
        self.math_quiz.run_quiz()
        self.assertEqual(self.math_quiz.num_wrong, 1)

    @patch('builtins.input', side_effect=['2', '3'])
    def test_update_settings(self, mock_input):
        self.math_quiz.update_settings()
        self.assertEqual(self.math_quiz.operator, "Multiplication")

if __name__ == '__main__':
    unittest.main()
