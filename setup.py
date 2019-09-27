from setuptools import setup, find_packages

setup(name="domextract",
      version="0.0.1d",
      description="Web article extractor",
      author="Shun Sugiyama",
      url="https://github.com/sugiyamath/domextract",
      packages=find_packages(),
      install_requires=[
          "numpy==1.17.1",
          "scikit-learn==0.21.3",
          "pandas==0.25.1",
          "bs4==0.0.1",
          "mecab-python3==0.996.1"
      ],
      package_data={
          'domextract':["*"]
      }
)
