# test_cryptofusion.py
"""
Tests for CryptoFusion module.
"""

import unittest
from cryptofusion import CryptoFusion

class TestCryptoFusion(unittest.TestCase):
    """Test cases for CryptoFusion class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoFusion()
        self.assertIsInstance(instance, CryptoFusion)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoFusion()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
