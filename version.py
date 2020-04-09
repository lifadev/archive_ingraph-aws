# Copyright 2020 Farzad Senart and Lionel Suss. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("setup.cfg")
    version = config['metadata']['version']
    parts = version.split(".")

    if len(sys.argv) == 2:
        idx = ["major", "minor", "patch"].index(sys.argv[1])
        parts[idx] = str(int(parts[idx]) + 1)
        version = '.'.join(parts)
        config['metadata']['version'] = version
        with open("setup.cfg", "w+") as file:
            config.write(file)

    print(version)
