from setuptools import setup, find_packages

setup(
    name='qtapi2',
    version='1.0',
    description='Cross-implementation and version support for PyQt(4|5) and PySide(|2).',
    url='https://github.com/vfxetc/qtapi2',
    
    packages=find_packages(exclude=['build*', 'tests*']),
    include_package_data=True,
    
    author='Mike Boers',
    author_email='floss+qtapi2@vfxetc.com',
    license='BSD-3',

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
