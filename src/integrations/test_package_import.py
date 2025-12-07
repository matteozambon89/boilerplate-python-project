#!/usr/bin/env python3  # noqa: CPY001
"""Test script to verify package functionality."""

try:
    # Test imports
    from yeeti.module import example

    print(f'✓ Successfully imported example: {example.__name__}')

    # Test main functionality
    example()
    print('✓ Example executed')

    print('✓ All tests passed!')

except ImportError as e:
    print(f'✗ Import error: {e}')
except Exception as e:
    print(f'✗ Runtime error: {e}')
