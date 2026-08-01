import os
import sys
import subprocess
import time

import pytest

ROOT = os.path.dirname(os.path.abspath(__file__))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

@pytest.fixture
def notepad():
    process = subprocess.Popen("notepad.exe")

    time.sleep(2)

    yield process

    process.terminate()
    process.wait(timeout=5)
