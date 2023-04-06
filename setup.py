from setuptools import setup

setup(
    name='youtube-up',
    version='0.1',
    packages=['youtube-up'],
    install_requires=[
        'google-api-python-client',
        'google-auth-oauthlib',
        'google-auth-httplib2',
    ],
    author='Arnaud Kayonga',
    author_email='arnauldkayonga1@gmail.com',
    description='A tool to directly upload media from Google drive to Youtube using google colab',
    keywords='Youtube Google-Colab',
    url='https://github.com/agent87/youtube-up',
    project_urls={
        'Bug Reports': 'https://github.com/agent87/youtube-up/issues',
        'Source': 'https://github.com/agent87/youtube-up',
    },
)
