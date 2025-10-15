# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import unittest
from unittest.mock import patch, MagicMock
from white_box.mockup_exercises import (
    fetch_data_from_api,
    read_data_from_file,
    execute_command,
    perform_action_based_on_time,
)
import subprocess


class TestDataFetcher(unittest.TestCase):
    """
    Data fetcher unittest class.
    """

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case.
        """
        # Crear respuesta simulada
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        }
        mock_get.return_value = mock_response

        # Llamar a la función bajo prueba
        result = fetch_data_from_api("https://jsonplaceholder.typicode.com/todos/1")

        # Verificar resultado esperado
        self.assertEqual(result, {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        })

        # Verificar que se llamó correctamente requests.get
        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/todos/1",
            timeout=10
        )


class TestReadDataFromFile(unittest.TestCase):
    """
    Read data from a file
    """
    def test_read_data_from_file_success(self):
        """
        Success case.
        """
        with patch("builtins.open", unittest.mock.mock_open(read_data="file content")) as mock_file:
            result = read_data_from_file("dummy.txt")
            self.assertEqual(result, "file content")
            mock_file.assert_called_once_with("dummy.txt", encoding="utf-8")

    def test_read_data_from_file_not_found(self):
        """
        FileNotFound case.
        """
        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                read_data_from_file("missing.txt")


class TestExecuteCommand(unittest.TestCase):
    """
    Execute command in subprocess
    """
    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Success case.
        """
        mock_result = MagicMock()
        mock_result.stdout = "command output"
        mock_run.return_value = mock_result

        result = execute_command(["echo", "hello"])
        self.assertEqual(result, "command output")
        mock_run.assert_called_once_with(
            ["echo", "hello"],
            capture_output=True,
            check=False,
            text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run", side_effect=subprocess.CalledProcessError(1, "cmd"))
    def test_execute_command_error(self, mock_run):
        """
        Error case.
        """
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["bad", "command"])


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Perform action based on time
    """
    @patch("white_box.mockup_exercises.time.time", return_value=5)
    def test_perform_action_before_10(self, mock_time):
        """
        current_time < 10 -> Action A
        """
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")

    @patch("white_box.mockup_exercises.time.time", return_value=15)
    def test_perform_action_after_10(self, mock_time):
        """
        current_time >= 10 -> Action B
        """
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")


if __name__ == "__main__":
    unittest.main()
