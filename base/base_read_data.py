import os
import yaml


class ReadLoginYaml():
    def __init__(self, failname):
        self.failname = os.getcwd()+os.sep+"data"+os.sep+failname
        # self.failname =failname
    def read_login_yaml(self):
        with open(self.failname, "r", encoding="utf-8") as f:
            return yaml.load(f)

# if __name__ == '__main__':
#     ReadLoginYaml().read_login_yaml()
# print(ReadLoginYaml("../data/data_login.yaml").read_login_yaml().values())