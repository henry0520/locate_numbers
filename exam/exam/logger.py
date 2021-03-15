"""
********************************************************

© YYYY - 2021 Exam. All Rights Reserved.

********************************************************

API logger
"""

import logging
import logging.handlers

def get_logger(name=None, base='exam'):
    """
    get logger
    """
    if not name:
        return logging.getLogger(base)
    return logging.getLogger("%s.%s" % (base, name))
