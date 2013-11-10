from distutils.core import setup

setup(
    name='mal',
    version='0.0.1',
    url='https://github.com/thiderman/mal',
    author='Lowe Thiderman',
    author_email='lowe.thiderman@gmail.com',
    description=('GitHub in your terminal'),
    license='MIT',
    packages=['mal'],
    install_requires=[
        'requests==2.0.1'
    ],
    scripts=[
        'bin/mal'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha'
        'Environment :: Console',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],
)
