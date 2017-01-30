from distutils.core import setup

setup(
    name='virtualenv-manager',
    version='1.0',
    author="Joshua Coady",
    author_email='',
    url='https://github.com/jcoady9/virtualenv-manager',
    scripts=['bin/virtualenv-manager.py'],
    packages=['virtualenv_manager'],
    install_requires=[
        'virtualenv',
    ],
    description='Simple GUI application to manage and run virtual environments made with virtualenv.',
)
