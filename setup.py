from setuptools import setup

setup(
    name="youtube-uploader",
    version="0.1",
    packages=["youtube-uploader"],
    install_requires=[
        "google-api-python-client",
        "google-auth-oauthlib",
        "google-auth-httplib2",
    ],
    author="Arnaud Kayonga",
    author_email="arnauldkayonga1@gmail.com",
    description="A command-line to upload videos to Youtube via Youtube API",
    keywords="Youtube CLI API",
    url="https://github.com/agent87/youtube-uploader",
    project_urls={
        "Bug Reports": "https://github.com/agent87/youtube-uploader/issues",
        "Source": "https://github.com/agent87/youtube-uploader",
    },
)
