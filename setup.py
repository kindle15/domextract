from setuptools import setup, find_packages

setup(name="domextract",
      version="0.0.2rc3",
      description="Web article extractor",
      author="Shun Sugiyama",
      url="https://github.com/sugiyamath/domextract",
      packages=find_packages(),
      install_requires=[
          "numpy",
          "scikit-learn",
          "pandas",
          "bs4",
          "mecab-python3"
      ],
      package_data={
          'domextract':["*"]
      }
)
