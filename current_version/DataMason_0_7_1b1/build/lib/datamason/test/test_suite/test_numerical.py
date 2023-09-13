#     Copyright (c) 2023, Kevan White (Thyripian)
#     All rights reserved.

#     Redistribution and use in source and binary forms, with or without
#     modification, are permitted provided that the following conditions are met:
#       Compliance with MIT License clauses.

#     THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#     AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#     IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#     DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#     FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#     DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#     SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#     CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#     OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#     OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest
import numpy as np
from datamason.numerics import numerical

class TestFunctions(unittest.TestCase):

    def test_sin(self):
        try:
            result = numerical.sin(0)
            assert result == 0, f"Expected 0, got {{result}}"

        except Exception as e:
            self.fail(f"An unexpected error occurred: {str(e)}")
            
    def test_cos(self):
        try:
            result = numerical.cos(0)
            assert result == 1, f"Expected 1, got {{result}}"

        except Exception as e:
            self.fail(f"An unexpected error occurred: {str(e)}")
            
    def test_tan(self):
        try:
            result = numerical.tan(0)
            assert result == 0, f"Expected 0, got {{result}}"

        except Exception as e:
            self.fail(f"An unexpected error occurred: {str(e)}")