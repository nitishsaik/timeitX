import asyncio
import time
import unittest
from unittest.mock import patch

from timeitX import timeitX



class TestTimeitXDecorator(unittest.TestCase):
    @patch("timeitX.logging.getLogger")
    def test_sync_function_timeitX(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value
        mock_logger.info.return_value = None

        @timeitX("sync_function", logger=mock_logger)
        def sync_function():
            time.sleep(1)
            return None

        sync_function()

        # Capture log messages and check assertions
        log_messages = [call[0] for call in mock_logger.info.call_args_list]

        assert any("Started execution of sync_function" in log[0] for log in log_messages)
        assert any("Finished execution of sync_function" in log[0] for log in log_messages)

    @patch("timeitX.logging.getLogger")
    def test_async_function_timeitX(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value
        mock_logger.info.return_value = None

        @timeitX("async_function", logger=mock_logger)
        async def async_function():
            time.sleep(1)
            return None

        asyncio.run(async_function())

        # Capture log messages and check assertions
        log_messages = [call[0] for call in mock_logger.info.call_args_list]

        assert any("Started execution of async_function" in log[0] for log in log_messages)
        assert any("Finished execution of async_function" in log[0] for log in log_messages)


if __name__ == "__main__":
    unittest.main()
