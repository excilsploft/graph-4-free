from diagrams import Diagram
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.compute import Nomad
from diagrams.onprem.container import Docker
from diagrams.onprem.vcs import Github
from diagrams.programming.language import Nodejs

# Constant to specify the output file prefix
OUPUT_FILE = "example_01"

# Very Simple diagram using the bitshift operator for edges
with Diagram("Simple Worfklow", show=False, filename=OUPUT_FILE, direction="TB", outformat=["svg", "png"]):
    Nodejs("Astro") >> Github("Enterprise") >> GithubActions("GHA Runner") >> Nomad("Nomad") >> Docker("Preview Site")
