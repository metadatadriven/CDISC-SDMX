# SDMX Data Model

The intension is to create a DSL created with the [Python TextX meta-language](http://textx.github.io/textX/stable/)

## Getting started with xtextX

See the [textX Hello World](http://textx.github.io/textX/stable/tutorials/hello_world/) is a good place to start.

The `hello.tx` file contains the hello world textX grammer which can be viewed as a graphic:

```
$ textx generate hello.tx --target dot
# convert to png with..
$ dot -Tpng -O hello.dot
```

![hello.dot diagran](https://github.com/metadatadriven/CDISC-SDMX/blob/main/script/model/hello.dot.png)

