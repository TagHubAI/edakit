from setuptools import setup, find_packages
setup(
    name='eda',
    version='0.0.1',
    author="TagHubAI team",
    author_email="me@patrickphat.com",
    description="Sentiment Analysis tool",
    packages = find_packages(exclude=['docs', 'tests', 'experiments']),
)