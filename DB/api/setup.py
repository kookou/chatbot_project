import setuptools
# root directory 에서 pip install .
with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='chatbot_api',
    version='1.0',
    description='Python Distribution Utilities',
    long_description=long_description,
    author='park',
    author_email='nnaangee@gmail.com',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=setuptools.find_packages(),
    python_requires='>=3.7'
)