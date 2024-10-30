# Classes / functions imported with logomaker
from .Logo import Logo
from .Glyph import Glyph
from .Glyph import list_font_names
from .matrix import transform_matrix
from .matrix import sequence_to_matrix
from .matrix import alignment_to_matrix
from .matrix import saliency_to_matrix
from .validate import validate_matrix
from .colors import list_color_schemes
from .examples import list_example_matrices
from .examples import get_example_matrix
from .examples import list_example_datafiles
from .examples import open_example_datafile
from .tests.functional_tests_logomaker import run_tests

# demo functions for logomaker
import matplotlib.pyplot as plt
import os
import re
from .error_handling import check, handle_errors

# Rest of the file stays the same...
