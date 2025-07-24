from unittest.mock import Mock
from loginsystem import LoginSystem

def test_service():
    mock_system = Mock()
    login_system = LoginSystem(system=mock_system)
    assert login_system.system is mock_system
