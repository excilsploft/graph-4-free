image := $(shell basename $$(pwd))
src := $(addsuffix .mmd, $(image))
svg := $(addsuffix .svg, $(image))
png := $(addsuffix .png, $(image))
readme := README.md
template := README.m4

default: build

.PHONY: build
build: node_modules $(svg) $(png)

$(svg): $(src) node_modules
	@node_modules/.bin/mmdc -i $< -o $@

$(png): $(src)
	@node_modules/.bin/mmdc -i $< -o $@

node_modules:
	npm install

.PHONY: readme
readme: $(readme)

$(readme): $(template) img
	m4 $< > $@

img: $(svg)
	@test -d img || mkdir img
	@cp $(svg) img/$(svg)

.PHONY: clean
clean:
	-rm -r node_modules
	-rm $(svg)
	-rm $(png)
	-rm -rf node_modules
