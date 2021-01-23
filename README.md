# [InGraph AWS][github] &middot; [![Version][badge-version]][version] [![CloudFormation][badge-cfn]][specs] [![License][badge-license]][license]

[InGraph][ingraph] is a Declarative Infrastructure Graph DSL for AWS
CloudFormation. This project uses the [AWS CloudFormation Resource
Specification][specs] to provide access to the latest native AWS
CloudFormation resources within InGraph, [automatically][actions].

## Installation

> Prerequisites: [Install InGraph][ingraph-install].

InGraph AWS requires [Python 3.8][python] or newer. Feel free to use
your favorite tool or [`pip`][pip] to install the [`ingraph.aws`
package][version].

```
python3.8 -m pip install --upgrade --user ingraph.aws
```

Note that this project automatically publishes a new version as soon as
AWS updates the AWS CloudFormation Resource Specification. To stay
updated, re-run the above command.

## License

Unless otherwise stated, the source code of the project is released
under the [Apache License Version 2][apachev2].

[github]: https://github.com/lifadev/ingraph-aws
[badge-version]: https://img.shields.io/badge/version-0.0.36-blue?style=flat-square
[version]: https://pypi.org/project/ingraph.aws/0.0.36/
[specs]: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html
[badge-cfn]: https://img.shields.io/badge/cloudformation-25.0.0-blue?style=flat-square
[badge-license]: https://img.shields.io/badge/license-Apache2-blue?style=flat-square
[license]: https://github.com/lifadev/ingraph-aws#license
[ingraph]: https://lifa.dev/ingraph
[ingraph-install]: https://github.com/lifadev/ingraph/blob/master/README.md#installation
[actions]: https://github.com/lifadev/ingraph-aws/actions
[python]: https://www.python.org/downloads/
[pip]: https://pip.pypa.io/en/stable/
[apachev2]: http://www.apache.org/licenses/LICENSE-2.0.txt
