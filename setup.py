from setuptools import setup


setup(
    name='flask-gemoji',
    version='0.1.0',
    py_modules=['flask_gemoji'],
    author="Mark Steve Samson",
    author_email='hello@marksteve.com',
    description="Add gemojis to your Jinja templates",
    long_description=open('README.md').read(),
    url='https://github.com/marksteve/flask-gemoji',
    include_package_data=True,
    zip_safe=False,
)
