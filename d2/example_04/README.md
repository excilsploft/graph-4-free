
# Example 4

This d2 graph utilizes the animated edge and "canned themes" features of d2 to provide a simple data flow diagram.

We set the [numbered theme](https://d2lang.com/tour/themes/) (currently theme 101, "orange creamsicle" ) on the command line of our makefile.

This example also uses an `m4` template to generate this README.md that ensures with one call to `make readme` we ensure that the README.md includes the latest source code from the d2 diagram and it's resultant SVG image.


## Instructions

1. `brew install d2`
2. `make build`

Will turn this:

```
workflow: Data Workflow {
    user: User {
        shape: person
    }

    input: Input {
        shape: document
    }

    validation: Data Validation {
        shape: square
    }

    new: New Data? {
        shape: diamond
    }

    store: Database {
        shape: Cylinder
    }

    user -> input
    input -> validation: To Validation Engine {
        style: {
            stroke-dash: 8
            stroke: blue
            animated: true
        }
    }
    validation -> new: Valid {
        style: {
            stroke-dash: 8
            stroke: green
            animated: true
        }
    }

    validation -> user: Invalid Error Message {
        style: {
            stroke-dash: 8
            stroke: red
            animated: true
        }
    }
    new -> store: Insert {
        style: {
            stroke-dash: 8
            stroke: blue
            animated: true
        }
    }

    new <-> store: Update {
        style: {
            stroke-dash: 8
            stroke: blue
            animated: true
        }
    }

}


```

Into this:

![example_04](./img/example_04.svg)

