from setuptools import setup

setup(
    name='naming_convert',
    version='1.0.0',
    author='Yang Dong',
    author_email='304887750@qq.com',
    url='https://github.com/dong50252409/naming_convert',
    description='Convert variable naming style between underscore, camelCase and dot notation',
    py_modules=['naming_convert'],
    entry_points={
        'console_scripts': [
            'naming-convert=naming_convert:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    long_description=open('README.rst').read(),
    license='MIT',
)
