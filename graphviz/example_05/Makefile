image := $(shell basename $$(pwd))
dot := $(addsuffix .dot, $(image))
svg := $(addsuffix .svg, $(image))
png := $(addsuffix .png, $(image))
hcl := $(addsuffix .hcl, $(image))
readme := README.md
template := README.m4
init := .terraform
lock := $(addsuffix .lock.hcl, $(init))
prov := providers.tf

default: build

.PHONY: build
build: $(readme)

$(dot): graph

$(svg): $(dot)
	@dot -Tsvg $< -o $@

.PHONY: nop
nop: $(dot)
	dot -Knop2 $<

.PHONY: readme
readme: $(readme)

$(readme): $(template) $(dot) img
	m4 $< > $@

.PHONY: img
img: $(svg)
	@test -d img || mkdir img
	@cp $(svg) img/$(svg)

.PHONY: graph
graph: $(init)
	terraform graph -type=plan > $(dot)

$(init): $(prov)
	terraform init

.PHONY: clean
clean:
	-rm -r $(init)
	-rm $(lock)
	-rm $(dot)
	-rm $(svg)
