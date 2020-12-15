from setuptools import find_packages, setup

setup(
    name='pff_data_management',
    packages=find_packages(),
    version='0.1.0',
    description='Python code to manage the data behind DVRPC\'s PhillyFreightFinder.',
    author='Michael Ruane',
    license='MIT',
    entry_points="""
        [console_scripts]
        shipcalls=marexchange.cli:main
        tradedata=usatrade.cli:main
    """,
)