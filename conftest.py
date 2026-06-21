import pytest

@pytest.fixture(scope="session")
def target_port(request):
    """
    Retrieves the serial port from CLI options or pytest.ini.
    Ensures environment parity across different test setups.
    """
    return request.config.getoption("--port")

@pytest.fixture(scope="session")
def current_baud(request):
    """
    Retrieves the baud rate. Used for dynamic hardware configuration.
    """
    return request.config.getoption("--baud")