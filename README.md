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

You will need [fatul](https://github.com/nyurik/fatul) to encode/decode blueprints. It is included in [tools](./tools/) folder.

Replace `book-dir` with the blueprint directory you want to use.

For example, if you want encoded Brian's trains Blueprint book:

```sh
tools/fatul.py encode -v brians-trains/book brians-train.txt
```

### Decode a Blueprint Book

```sh
rm -rf book-dir
tools/fatul.py decode book-dir/book my-exported-book.txt
```

It's important to completely remove the old directory before splitting otherwise removed/renamed blueprints will remain in the previous form and be re-introduced when the book is next built.

### Encode a Blueprint Book

```sh
tools/fatul.py encode -v book-dir/book my-book.txt
```

### Decode a Single Blueprint

```sh
tools/fatul.py decode blueprint.json my-exported-blueprint.txt
```

### Encode a Single Blueprint

```sh
tools/fatul.py encode book-dir/book/blueprint.json my-exported-blueprint.txt
```
