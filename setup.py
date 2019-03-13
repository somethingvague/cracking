from setuptools import setup, find_packages

setup(
    name='cracking',
    version='0.0.1dev',
    packages=find_packages(),
    test_suite='nose.collector',
    tests_require=['nose'],
    url='https://github.com/somethingvague/cracking',
    license='',
    author='somethingvague',
    author_email='phil.j.regan@gmail.com',
    description="""A repository of solutions to the exercises in 'Cracking the Coding Interview' 
                     to sharpen my CS skills and learn Python"""
)
