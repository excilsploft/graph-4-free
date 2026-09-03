image := example_04
src := $(addsuffix .d2, $(image))
svg := $(addsuffix .svg, $(image))
png := $(addsuffix .png, $(image))
readme := README.md
template := README.m4

default: build

.PHONY: build
build: $(svg) $(png)

$(svg): $(src)
	@d2 -t 101 --layout=dagre $< $@

$(png): $(src)
	@d2 -t 101 --layout=dagre $< $@

.PHONY: readme
readme: $(readme)

$(readme): $(template) img
	m4 $< > $@

.PHONY: img
img: $(svg)
	@test -d img || mkdir img
	@cp $(svg) img/$(svg)

.PHONY: clean
clean:
	-rm $(svg)
	-rm $(png)
