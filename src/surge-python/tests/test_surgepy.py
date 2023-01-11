"""
Tests for Surge XT Python bindings.
"""

import numpy as np
import surgepy


def test_getVersion():
    version = surgepy.getVersion()
    assert isinstance(version, str)


def test_createSurge():
    surgepy.createSurge(44100)


def test_render_note():
    """
    Test rendering a note into a buffer.
    """
    s = surgepy.createSurge(44100)
    n_blocks = int(2 * s.getSampleRate() / s.getBlockSize())
    buf = s.createMultiBlock(n_blocks)
    s.playNote(0, 60, 127, 0)
    s.processMultiBlock(buf)
    assert not np.all(buf == 0.0)