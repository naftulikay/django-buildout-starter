from setuptools import setup, find_packages

setup(
	name = "djangobuildoutstarter",
	version = "0.0.2",
	license = 'MIT',
	description = 'Sample project to use to get started quickly with Django and' +
        ' zc:buildout.',
	author = 'TK Kocheran',
	packages = find_packages('src'),
	package_dir = {'': 'src'},
	install_requires = [
		'docutils',
		'setuptools'
	],
)
