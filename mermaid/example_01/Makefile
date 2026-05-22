image := example_01
src := $(addsuffix .mmd, $(image))
svg := $(addsuffix .svg, $(image))
png := $(addsuffix .png, $(image))

default: build

.PHONY: build
build: node_modules $(svg) $(png)

$(svg): $(src) 
	@node_modules/.bin/mmdc -i $< -o $@

$(png): $(src)
	@node_modules/.bin/mmdc -i $< -o $@

node_modules:
	npm install

.PHONY: clean
clean:
	-rm $(svg)
	-rm $(png)
	-rm -rf node_modules
