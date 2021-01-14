from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md') as f:
    readme = f.read()


setup(
    name='BeautifulGuilded',
    author='Smirf123',
    url='https://github.com/Smirf123/BeautifulDiscord',
    version='0.1.1',
    license='MIT',
    description='Adds custom CSS support to Guilded, forked from Beautiful Discord by Leovoel',
    long_description=readme,
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    entry_points={'console_scripts': ['beautifuldiscord=beautifuldiscord.app:main']}
)
