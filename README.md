# Brian's Blueprints

Brian's Blueprints for Factorio

Don't just look at the latest release shown on the left. Each book is released separately so to see them you have to go to the [all-releases page](https://github.com/bcwhite-code/brians-blueprints/releases).

Blueprints include:

- [Brian's Bootstrap](./brians-bootstrap/)
- [Brian's Trains](./brians-trains/)
- [Brian's Trains Auxiliary](./brians-trains-auxiliary/)
- [Finite State Machine](./finite-state-machine/)
- [SBF Big Blocks](./sbf-big-blocks/)
- [Self Building Angel Bob](./self-building-angelbob/)
- [Self Building Factory](./self-building-factory/)
- [Self Building Rocket](./self-building-rocket/)
- [Self Building Space Exploration](./self-building-spacex/)
- [Tileable Reactor](./tileable-reactor/)

## Commands

The "fbp.py" script can be used to split books into a directory structure and later build them back into a single entity as well as to unpack/pack single blueprints from their encoded form into json. The latter allows working with single blueprints within a book.

### Split a Book

```sh
rm -rf book-directory
tools/fbp.py split --outdir=book-directory/book --infile=my-exported-book.txt
```

It's important to completely remove the old directory before splitting otherwise removed/renamed blueprints will remain in the previous form and be re-introduced when the book is next built.

### Build a Book

```sh
tools/fbp.py build --outfile=my-book.txt --indir=book-directory/book
```

OR

```sh
tools/fatul.py encode -v book-dir/book my-book.txt
```

### Unpack a Single Blueprint

```sh
tools/fbp.py unpack --outfile=book-directory/book/blueprint.json --infile=my-exported-blueprint.txt
```

OR

```sh
tools/fatul.py decode my-exported-blueprint.txt blueprint.json
```

### Pack a Single Blueprint

```sh
tools/fbp.py pack --outfile=my-blueprint.txt --infile=book-directory/book/blueprint.json
```

OR

```sh
tools/fatul.py encode book-directory/book/blueprint.json my-exported-blueprint.txt
```
