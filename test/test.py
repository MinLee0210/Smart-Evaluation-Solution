import unittest
import os
import random

from controller.task import ses_pipeline
from src.tools import load_image


BASE_DIR = './docs/samples'

class TestCaptureImage(unittest.TestCase): 
    
    def test_capture(self): 
        rand_idx = random.randint(0, range(len(os.listdir(BASE_DIR)))-1)
        sample = os.path.join(BASE_DIR, os.listdir(BASE_DIR)[rand_idx])
        img = load_image(sample)
        test_case = ses_pipeline(image=img)
        self.assertTrue(not isinstance(test_case, None)) # assert true when test_case is not None.