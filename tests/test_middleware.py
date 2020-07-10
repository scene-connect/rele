from unittest.mock import patch

import pytest

import rele


class TestMiddleware:
    @pytest.fixture
    def mock_init_global_publisher(self):
        with patch("rele.config.init_global_publisher", autospec=True) as m:
            yield m

    @pytest.mark.usefixtures("mock_init_global_publisher")
    @patch("rele.contrib.FlaskMiddleware.setup", autospec=True)
    def test_setup_fn_is_called_with_kwargs(self, mock_middleware_setup, project_id):

        settings = {
            "GC_PROJECT_ID": project_id,
            "MIDDLEWARE": ["rele.contrib.FlaskMiddleware"],
        }

        rele.setup(settings, foo="bar")
        assert mock_middleware_setup.called
        mock_middleware_setup.call_args_list[0][-1] == {"foo": "bar"}
