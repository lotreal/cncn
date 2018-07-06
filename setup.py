from setuptools import setup

setup(
    name='CNCN',
    version='1.0',
    py_modules=['cncn'],
    install_requires=[
        'Click',
        'PyYAML',
    ],
    entry_points='''
    [console_scripts]
    cncn=cncn:cli
    '''
)
