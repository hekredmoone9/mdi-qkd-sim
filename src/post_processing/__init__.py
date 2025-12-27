"""
Post-processing modules for MDI-QKD simulation.
Includes error correction, privacy amplification, etc.
"""

from .cascade_lite import correct_errors

__all__ = ['correct_errors']