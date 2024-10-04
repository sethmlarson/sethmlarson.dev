# PyCon Taiwan 2024 Keynote

[Here are my slides](https://storage.googleapis.com/sethmlarson-dev-static-assets/PyCon-Taiwan-Keynote-Bytes-Pipes-and-People.pdf) and overview of my PyCon Taiwan 2024 Keynote
titled "Bytes, Pipes, and People". The video will be [published to YouTube](https://www.youtube.com/@PyConTaiwanVideo),
subscribe to the [PyCon Taiwan YouTube channel](https://www.youtube.com/@PyConTaiwanVideo) to be notified when available.

> Software security has historically been treated as extra or "nice-to-have",
> not a core feature that users expect. This means we have accumulated
> plenty of tech debt. Now there are growing incentives and requirements
> for producing secure software to meet user expectations.
>
> Luckily for us, many of the tools, data, and systems already exist to
> help us **build a culture of security for Python**. These tools help relay messages
> between software creators and users so we can collaborate on this shared goal.
>
> By actively participating you are starting the positive feedback loop of software security, making users safer faster!

Below is a list of items that actions can implement to build a culture of security for Python:

#### Maintainers

* Adopt [Trusted Publishers](https://docs.pypi.org/trusted-publishers/using-a-publisher/) if you use GitHub Actions, GitLab CI/CD, Google Cloud Build, or ActiveState to publish Python packages.
* Use lock files for the build and publish workflow, such as pip-tools, Poetry, or PDM.
* Adopt a lightweight security policy. Do not stress about CVEs: fix, release, publish a CVE.
* Contribute new insecure code detections to [Bandit](https://bandit.readthedocs.io/en/latest/).

#### Users

* Update dependencies that have vulnerabilities. Prioritize projects that are connected to the internet.
* Update software on a semi-regular basis to avoid out-of-date and end-of-life software. Staying up-to-date helps you being able to upgrade to fixed versions in the future.
* Run tests with `PYTHONWARNINGS` with `DeprecationWarning` and `PendingDeprecationWarning` set to errors to avoid missing deprecated features.
* Create a secure open source usage policy, using verified data to evaluate open source projects. Do not install new projects without checking your policy first.
* If you need a Software Bill-of-Materials document there are tools available to generate one. Those tools will improve over time from new Python package SBOM standards.
* Add a vulnerability scanner like pip-audit, Grype, or Trivy.

#### Tools and Links

* [What is Software Bill-of-Materials ("SBOM")?](https://www.synopsys.com/blogs/software-security/software-bill-of-materials-bom.html)
* [Trusted Publishers](https://docs.pypi.org/trusted-publishers/using-a-publisher/)
* [PyPI blog](https://blog.pypi.org/)
* [Bandit](https://bandit.readthedocs.io/en/latest/)
* [Warnings in Python](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNINGS)
* [pip-audit](https://pypi.org/project/pip-audit/)
* [Scientific Python SPEC-8: "Securing the Release Process"](https://scientific-python.org/specs/spec-0008/)
* [Supply chain security threats (SLSA)](https://slsa.dev/spec/v1.0/threats)
* [Grype](https://github.com/anchore/grype)
* [Trivy](https://trivy.dev)
* [Ecosyste.ms](https://packages.ecosyste.ms)
* [Libraries.io](https://libraries.io)
* [Deps.dev](https://deps.dev)
* [Trusty](https://trustypkg.dev)
* [pip-tools](https://pip-tools.readthedocs.io/en/latest/)
* [Poetry](https://python-poetry.org/)
* [PDM](https://pdm-project.org/latest/)
* [uv](https://docs.astral.sh/uv/)
* [Sigstore Python](https://pypi.org/project/sigstore/)
* [Yanking Python packages](https://pypi.org/help/#yanked)

## References

* [HTTP Archive](httparchive.org)
* [Sonatype 2023 Annual State of Software Supply Chain Report](https://www.sonatype.com/en/press-releases/sonatype-9th-annual-state-of-the-software-supply-chain-report)
* Kushal Das for Python Language Summit photos
* [StackOverflow](https://stackoverflow.com/q/25981703)
