from setuptools import setup, find_packages

setup(name="domextract",
      version="0.0.1",
      description="Web article extractor",
      author="Shun Sugiyama",
      url="https://github.com/sugiyamath/domextract",
      packages=find_packages(),
      package_data={
          'domextract':["*"]
      }
)
