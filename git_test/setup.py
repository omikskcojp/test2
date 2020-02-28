from setuptools import setup, find_packages
from pathlib import Path


def read_requirements():
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        requirements = [line.strip() for line in f.readlines() if line.strip()]
    return requirements


def read_readme():
    with open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


def get_data_files():
    data_dir = Path('./aaa/data')
    data_paths = [str(path).replace('\\', '/').replace('aaaa/', '')
                  for path in data_dir.glob('**/*') if path.is_file()]
    return data_paths



setup(
    name='git_test',
    version='1.0.0',
    author='omi',
    author_email='omi@ksk.co.jp',
    url='https://github.com/kskomi/gittest',
    description='Git-Pip test.',
    long_description='bbbbb',
    license='MIT',
    include_package_data=True,
    #package_data={
    #    'aaa:aaaaa'
    #}
)
