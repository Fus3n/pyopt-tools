from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# setup build: python setup.py sdist bdist_wheel
# upload: twine upload dist/*
#build doc
# pdoc --html pyopt_tools -o docs


VERSION = '0.7'
DESCRIPTION = 'A Python package full of small & useful functions to make your life easier.'

setup(
    name="pyopt-tools",
    version=VERSION,
    author="FUSEN",
    author_email="fus3ngames@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    long_description=long_description,
    install_requires=[],
    keywords=['python', 'pyopt-tools', 'python optimization tools', 'python mirco functions', 'string tools',
              'math_tools', 'list_tool', 'pyvec'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
