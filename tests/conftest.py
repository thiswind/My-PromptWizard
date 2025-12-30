"""
Pytest configuration and shared fixtures for PromptWizard tests.
"""
import pytest
import os
import sys
from dotenv import load_dotenv

# Load environment variables from my.env
# Get the project root directory (parent of tests/)
project_root = os.path.join(os.path.dirname(__file__), "..")
env_path = os.path.join(project_root, "my.env")
load_dotenv(env_path, override=True)

# Add project root directory to path
sys.path.insert(0, project_root)


@pytest.fixture
def config_paths():
    """
    Return paths to configuration files for scenarios demo.
    
    Returns:
        dict: Dictionary with keys:
            - promptopt: Path to promptopt_config.yaml
            - setup: Path to setup_config.yaml
            - config_dir: Path to configs directory
    """
    base_dir = os.path.join(project_root, "demos", "scenarios")
    return {
        "promptopt": os.path.join(base_dir, "configs", "promptopt_config.yaml"),
        "setup": os.path.join(base_dir, "configs", "setup_config.yaml"),
        "config_dir": os.path.join(base_dir, "configs")
    }

