# Copyright (C) 2025 Yeeti
from .main import example

__all__ = ['example']

__version__ = '0.0.0'  # Placeholder

try:
    from importlib.metadata import version

    __version__ = version(__name__)
except ImportError:
    # Fallback for direct imports during dev
    pass
