import subprocess
import sqlite3
import sys
import os


class PyEnvManager(object):
    """Manager Object for virtual environments created with virualenv"""

    env_storage_dir = 'pyenvironments'

    def __init__(self):
        if sys.platform == 'win32':
            self.home_path = os.environ['USERPROFILE']
        else:
            self.home_path = '~'
        self.db_conn = sqlite3.connect('pyenv.sqlite3')
        self.db_conn.execute('CREATE TABLE IF NOT EXISTS environments (environment_name TEXT, activate_path TEXT)')
        self.db_conn.commit()

    def __del__(self):
        if self.db_conn:
            self.db_conn.close()

    def run_cmd(self):
        subprocess.Popen('start cmd', stdin=subprocess.PIPE, shell=True)

    def open_environment(self, position):
        process = subprocess.Popen('start cmd', stdin=subprocess.PIP, shell=True)
        environment_results = self.db_conn.execute('SELECT * FROM environments WHERE ROWID=?', (position,))
        environment = environment_results.fetchone()
        process.communicate(input=environment[1])

    def create_environment(self, name):
        env_path = os.path.abspath(os.path.join('C:\\', self.home_path, self.env_storage_dir, name))
        subprocess.call(['virtualenv', env_path])
        self.db_conn.execute('INSERT INTO environments(environment_name, activate_path) VALUES (?,?)', (name, env_path,))
        self.db_conn.commit()

    def delete_environment(self, position):
        pass

    def environments(self):
        """returns a list of tuples of python virtual environments."""
        return None

manager = PyEnvManager()
#manager.run_cmd()
manager.create_environment('test-env')
