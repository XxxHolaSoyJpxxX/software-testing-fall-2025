# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import subprocess
import unittest
from unittest.mock import MagicMock, patch

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestDataFetcher(unittest.TestCase):
    """Testea la función fetch_data_from_api."""

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """Verifica que fetch_data_from_api retorne los datos correctamente."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False,
        }
        mock_get.return_value = mock_response

        result = fetch_data_from_api("https://jsonplaceholder.typicode.com/todos/1")
        self.assertEqual(
            result,
            {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False},
        )
        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/todos/1", timeout=10
        )


class TestReadDataFromFile(unittest.TestCase):
    """Testea la función read_data_from_file."""

    def test_read_data_from_file_success(self):
        """Verifica lectura correcta de un archivo existente."""
        with patch(
            "builtins.open", unittest.mock.mock_open(read_data="file content")
        ) as mock_file:
            result = read_data_from_file("dummy.txt")
            self.assertEqual(result, "file content")
            mock_file.assert_called_once_with("dummy.txt", encoding="utf-8")

    def test_read_data_from_file_not_found(self):
        """Verifica que se lance FileNotFoundError si el archivo no existe."""
        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                read_data_from_file("missing.txt")


class TestExecuteCommand(unittest.TestCase):
    """Testea la función execute_command."""

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """Verifica ejecución correcta de un comando válido."""
        mock_result = MagicMock()
        mock_result.stdout = "command output"
        mock_run.return_value = mock_result

        result = execute_command(["echo", "hello"])
        self.assertEqual(result, "command output")
        mock_run.assert_called_once_with(
            ["echo", "hello"], capture_output=True, check=False, text=True
        )

    @patch(
        "white_box.mockup_exercises.subprocess.run",
        side_effect=subprocess.CalledProcessError(1, "cmd"),
    )
    def test_execute_command_error(self, _mock_run):
        """Verifica que se lance CalledProcessError en comando inválido."""
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["bad", "command"])


class TestPerformActionBasedOnTime(unittest.TestCase):
    """Testea la función perform_action_based_on_time."""

    @patch("white_box.mockup_exercises.time.time", return_value=5)
    def test_perform_action_before_10(self, _mock_time):
        """current_time < 10 -> retorna Action A."""
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")

    @patch("white_box.mockup_exercises.time.time", return_value=15)
    def test_perform_action_after_10(self, _mock_time):
        """current_time >= 10 -> retorna Action B."""
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")


if __name__ == "__main__":
    unittest.main()
