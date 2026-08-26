# Example 3

In this simple graphviz example we use the `dot` language to make a simplified diagram of a CI/CD system with product logos.

We utilize the [image](https://graphviz.org/docs/attrs/image/) attribute of the `dot` language to embed product logos that might be associated with a conventional ci/cd system.

## Instructions

1. `brew install graphviz`
2. `make build`

Will turn this:

```
digraph BuildEnv {
    label="Single Box Jenkins";
    labelloc="t"

    compound=true;
    ranksep=1.25;
    rankdir=LR;
    node [shape=plaintext, fontsize=10, label=""];

    subgraph cluster_server {
        label="Server";
        labelloc="t"
        fontsize=20;
        server [image="./logofiles/server.png";]
        jenkins [
            label="Jenkins";
            labelloc="b";
            image="./logofiles/jenkins.png";
            imagepos="tc";
            imagescale=false;
        ]
        docker [
            label="Docker Daemon";
            labelloc="t";
            image="./logofiles/docker.png";
        ]
        grafana [
            label="Grafana";
            labelloc="t";
            image="./logofiles/grafana.png";
        ]

        docker -> jenkins [dir=both];
        docker -> grafana [dir=both];
    }


    subgraph cluster_github {
        label="Github";
        labelloc="t"
        fontsize=20;
        Github [
            image="./logofiles/github.png";
        ]
    }

    Github -> jenkins [dir=both];
}
```

Into:
![image](./img/example_03.png)

