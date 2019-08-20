"""Data loading code for DataLearn prep night workshop."""

import pip
import pandas as pd

try:
    import google.colab
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

def in_notebook():
    try:
        from IPython import get_ipython
        if 'IPKernelApp' not in get_ipython().config:  # pragma: no cover
            return False
    except ImportError:
        return False
    return True


def pipinstall(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


GDRIVE_AUTHENICATED = False

def gdrive_authenticate():
    global GDRIVE_AUTHENICATED
    if GDRIVE_AUTHENICATED:
        return
    pipinstall('PyDrive')
    # !pip install -U -q PyDrive
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    from google.colab import auth
    from oauth2client.client import GoogleCredentials
    # Authenticate and create the PyDrive client.GDRIVE_AUTHENICATED# This only
    # needs to be done once per notebook.
    auth.authenticate_user()
    gauth = GoogleAuth()
    gauth.credentials = GoogleCredentials.get_application_default()
    drive = GoogleDrive(gauth)
