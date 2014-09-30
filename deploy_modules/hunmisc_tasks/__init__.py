"""Installs the hunmisc module"""
from fabric.api import local, lcd, run
import cliqz
import os

def resource_file(name):
    """Return a resource file relative to the directory of this script"""
    return os.path.join(os.path.dirname(__file__), name)

def install():
    cliqz.log_action('Installing hunmisc')
    path = '/opt/hunmisc'
    cliqz.cli.system_package('build-essential', 'python-dev')
    cliqz.cli.python_package('dawg')
    pkg = cliqz.package.gen_definition()
    pkg['strip'] = 0
    with lcd(resource_file('../../')):
        local("tar cjf {} hunmisc setup.py".format(pkg['local']))
    cliqz.package.install(pkg, path)
    run('pip install --editable {}'.format(path))
