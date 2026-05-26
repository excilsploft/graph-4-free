# Example 2

This graph is much more in line with the [py-diagram example 1](../../py-diagram/exampl_01/) diagram.

We are using the [D2 Icon](https://d2lang.com/tour/icons/) along with local images and icons from https://icons.terrastruct.com/ to display simple workflow.


## Instructions

`make build`

Will turn this:
```
node: "Node.js" {
	icon: https://icons.terrastruct.com/dev%2Fnodejs.svg
    shape: image
}

gh: "Github Enterprise" {
	icon: https://icons.terrastruct.com/dev%2Fgithub.svg
    shape: image
}

gha: "Github Actions" {
	icon: ./img/github-actions.png
    shape: image
}

nomad: "Nomad" {
	icon: ./img/nomad.png
    shape: image
}

docker: "Preview"{
	icon: https://icons.terrastruct.com/dev%2Fdocker.svg
    shape: image
}

node -> gh -> gha -> nomad -> docker
```

Into:

[image](./img/example_02.svg)
