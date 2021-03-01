from setuptools import setup

setup(
    name="sendgrify",
    version="1.0.0",
    url="https://github.com/sdelquin/sendgrify.git",
    author="Sergio Delgado Quintero",
    author_email="sdelquin@gmail.com",
    description="SendGrid for Humans",
    packages=["sendgrify"],
    install_requires=["sendgrid"],
)
