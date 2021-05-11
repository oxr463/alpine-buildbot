import urllib.request

class Repology(object):
    def __init__(self, maintainer_name, package_repository):
        self.package_url = 'https://repology.org/api/v1/projects/?maintainer=' + maintainer_name + '&inrepo=' + package_repository + '&status=outdated'

    def get_packages(self):
        with urllib.request.urlopen(self.package_url) as response:
            self.packages = response.read()
        return self.packages

