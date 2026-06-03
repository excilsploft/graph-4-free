image := $(shell basename $$(pwd))
dot := $(addsuffix .dot, $(image))
svg := $(addsuffix .svg, $(image))
png := $(addsuffix .png, $(image))

default: build

.PHONY: build
build: $(svg) $(png)

$(dot): Makefile
	find /bin/ -type f -exec ls -l {} \; | \
	head -n 15 | \
	tail -n 5  | \
	sort -rk 5 | \
	awk 'BEGIN {a[0]="bisque";a[1]="lightblue";a[2]="lavender";a[3]="lightcoral";a[4]="lightyellow";print "digraph {\n\tlayout=\"patchwork\"\n\tnode [style=\"filled\"]" }{printf "\t\t%s [ \n\t\tlabel = \"%s\"\n\t\tfillcolor = \"%s\"\n\t\tarea = %s\n\t\t]\n", NR, $$9, a[NR], int(($$5 /1000)) }END{print "}"}' | \
	nop | \
   	tee $@

$(svg): $(dot)
	@dot -Tsvg $< -o $@

$(png): $(dot)
	@dot -Tpng $< -o $@

.PHONY: clean
clean:
	-rm $(dot)
	-rm $(svg)
	-rm $(png)
