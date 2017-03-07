from setuptools import setup

setup(
    name='boxer',
    version='0.1',
    py_modules=['boxer'],
    include_package_data=True,
    url='https://github.com/bradleygolden/boxer',
    download_url='https://github.com/bgolden/boxer/archive/0.1.tar.gz.'
    install_requires=[
        'Click',
        'docker'
    ],
    entry_points='''
        [console_scripts]
        boxer=boxer.boxer:cli
    ''',
)
