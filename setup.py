from setuptools import setup, find_packages

setup(
    name='hatenablog',
    description="A Python wrapper for HatenaBlog's API.",
    version='0.0.1',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(),
    author='takeshi0406',
    author_email='sci.and.eng@gmail.com',
    url='https://github.com/takeshi0406/',
    keywords='hatenablog api wrapper',
    install_requires=['requests_oauthlib', 'xmltodict']
)
