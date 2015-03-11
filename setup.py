from setuptools import setup

setup(name='robotframework-cylon',
      version='0.0.1',
      description='',
      url='https://github.com/gigapixel',
      author='Peerapat S.',
      author_email='gigapixel7@gmail.com',
      license='MIT',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
      ],
      packages=['cylon_robot'],
    #   entry_points={
    #       'console_scripts': [
    #       'cylon=cylon.command:main', 'behack=cylon.behack:main'
    #   ]},
      install_requires=[
          'selenium'
      ],
      zip_safe=False)
