image := $(shell basename $$(pwd))
src := $(addsuffix .mmd, $(image))
svg := $(addsuffix .svg, $(image))
png := $(addsuffix .png, $(image))
readme := README.md
template := README.m4

default: build

.PHONY: build
build: $(svg) $(png)

$(svg): $(src)
	@merman-cli -i $< -o $@

$(png): $(src)
	@merman-cli -i $< -o $@

.PHONY: readme
readme: $(readme)

$(readme): $(template) img
	m4 $< > $@

img: $(svg)
	@test -d img || mkdir img
	@cp $(svg) img/$(svg)

.PHONY: clean
clean:
	-rm $(svg)
	-rm $(png)
