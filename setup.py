from setuptools import setup, find_packages

setup(
	name = "django-buildout-starter",
	version = "0.0.1",
	license = 'MIT',
	description = 'Sample project to use to get started quickly with Django and' +
        ' buildout.',
	author = 'TK Kocheran',
	packages = find_packages('src'),
	package_dir = {'': 'src'},
	install_requires = [
		'docutils',
		'setuptools'
	],
)
