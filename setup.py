import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"

REPO_NAME = "ml_github_issue_classifier"
AUTHOR_NAME = "MusaddiqueHussain Jahagirdar"
AUTHOR_USER_NAME = "MusaddiqueHussainLabs"
SRC_REPO = "github_labeler"
AUTHOR_EMAIL = "musaddiquehussainlabs@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="ml_github_issue_classifier is an automated system for categorizing GitHub issues into multiple classes using machine learning.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)