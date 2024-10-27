# Classes / functions imported with logomaker
from .src.Logo import Logo
from .src.Glyph import Glyph
from .src.Glyph import list_font_names
from .src.matrix import transform_matrix
from .src.matrix import sequence_to_matrix
from .src.matrix import alignment_to_matrix
from .src.matrix import saliency_to_matrix
from .src.validate import validate_matrix
from .src.colors import list_color_schemes
from .src.examples import list_example_matrices
from .src.examples import get_example_matrix
from .src.examples import list_example_datafiles
from .src.examples import open_example_datafile
from .tests.functional_tests_logomaker import run_tests

# demo functions for logomaker
import matplotlib.pyplot as plt
import os
import re
from .src.error_handling import check, handle_errors

@handle_errors
def demo(name='fig1b'):

    """
    Performs a demonstration of the Logomaker software.

    parameters
    -----------

    name: (str)
        Must be one of {'fig1b', 'fig1c', 'fig1d', 'fig1e', 'fig1f', 'logo'}.

    returns
    -------
    None.

    """

    # build list of demo names and corresponding file names
    example_dir = '%s/examples' % os.path.dirname(__file__)
    all_base_file_names = os.listdir(example_dir)
    example_file_names = ['%s/%s' % (example_dir, temp_name)
                     for temp_name in all_base_file_names
                     if re.match('demo_.*\.py', temp_name)]
    examples_dict = {}
    for file_name in example_file_names:
        key = file_name.split('_')[-1][:-3]
        examples_dict[key] = file_name

    # check that name is valid
    check(name in examples_dict.keys(),
          'name = %s is not valid. Must be one of %s'
          % (repr(name), examples_dict.keys()))

    # open and run example file
    file_name = examples_dict[name]
    with open(file_name, 'r') as f:
        content = f.read()
        line = '-------------------------------------------------------------'
        print('Running %s:\n%s\n%s\n%s' % \
              (file_name, line, content, line))
    exec(open(file_name).read())

    # return the current matplotlib Figure object
    return plt.gcf()

