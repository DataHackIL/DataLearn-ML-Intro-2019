"""Data loading code for DataLearn prep night workshop."""

import pip
import pandas as pd

try:
    import google.colab  # noqa: F401

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


GDRIVE = None


def gdrive_authenticate():
    global GDRIVE
    if GDRIVE is not None:
        return
    print('Installing PyDrive...')
    pipinstall('PyDrive')
    # !pip install -U -q PyDrive
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    from google.colab import auth
    from oauth2client.client import GoogleCredentials

    # Authenticate and create the PyDrive client.GDRIVE_AUTHENICATED# This only
    # needs to be done once per notebook.
    print('Authenticating with Google Drive...')
    auth.authenticate_user()
    gauth = GoogleAuth()
    gauth.credentials = GoogleCredentials.get_application_default()
    GDRIVE = GoogleDrive(gauth)


def get_accounts():
    if IN_COLAB:
        gdrive_authenticate()
        # you can see it with "get sherable link"
        print("Downloading accounts.csv from Google Drive...")
        accounts_file_id = '1SFFGL_FIq3-l6CP9MTe9ueuLRMz_tvrw'
        downloaded = GDRIVE.CreateFile({'id': accounts_file_id})
        downloaded.GetContentFile('accounts.csv')
        print("Done.")
        return pd.read_csv('accounts.csv')
    else:
        return pd.read_csv('data/accounts.csv')
