"""Data loading code for DataLearn prep night workshop."""

import pip
import subprocess

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
    subprocess.run(["pip", "install", "-U", "-q", "PyDrive"])
    # pipinstall('PyDrive')
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


def _get_file(fname, id):
    if IN_COLAB:
        gdrive_authenticate()
        # you can see it with "get sherable link"
        print("Downloading {} from Google Drive...".format(fname))
        downloaded = GDRIVE.CreateFile({'id': id})
        downloaded.GetContentFile(fname)
        print("Done.")
        return pd.read_csv(fname)
    else:
        return pd.read_csv('data/{}'.format(fname))


def get_accounts():
    return _get_file('accounts.csv', '1SFFGL_FIq3-l6CP9MTe9ueuLRMz_tvrw')


def get_users():
    return _get_file('users.csv', '1fG6ebyTaWWOVRFHw9svNjgJLYdUcu5th')


def get_events():
    return _get_file(
        'Dynamic events table.csv', '1Gv0Z_IJ1kBwuUnPDkpgFM8mK1dGeTNi4')


def get_subscriptions():
    return _get_file(
        'Dynamic subscription table.csv', '1qC0VOpUkZo4O4lggzp45YcNxC7NXY4VV')
