import subprocess
import sqlite3
import shutil
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

    def open_environment(self, position):
        process = subprocess.Popen('Start cmd.exe @cmd /k virtualenv', stdin=subprocess.PIPE, shell=True)
        environment_results = self.db_conn.execute('SELECT * FROM environments WHERE ROWID=?', (position,))
        environment = environment_results.fetchone()
        process.communicate(input="virtualenv --help".encode())

    def create_environment(self, name):
        env_path = os.path.abspath(os.path.join('C:\\', self.home_path, self.env_storage_dir, name))
        try:
            subprocess.check_call(['virtualenv', env_path])
            self.db_conn.execute('INSERT INTO environments(environment_name, activate_path) VALUES (?,?)', (name, env_path,))
            self.db_conn.commit()
        except CalledProcessError as error:
            print("returncode: %s" % error.returncode)
            print('cmd: %s' % error.cmd)
            print(error.output)

    def delete_environment(self, position):
        cursor = self.db_conn.execute('SELECT environment_name FROM environments')
        env = cursor.fetchone()
        env_path = os.path.abspath(os.path.join('C:\\', self.home_path, self.env_storage_dir, env[0]))
        try:
            shutil.rmtree(env_path)
            self.db_conn.execute('DELETE FROM environments WHERE ROWID=?', (position + 1,))
            self.db_conn.commit()
        except OSError as error:
            print('ERROR: Unable to delete virtual environment: %s' % error.filename)
            print(error.strerror)

    def environments(self):
        """returns a list of tuples of python virtual environments."""
        cursor = self.db_conn.execute('SELECT * FROM environments')
        return cursor.fetchall()

# manager = PyEnvManager()
# manager.create_environment('test-env')
# for env in manager.environments():
#    print(env)
# manager.delete_environment(1)
# print('deleted environment')
# for env in manager.environments():
#      print(env)
# print('done!')
