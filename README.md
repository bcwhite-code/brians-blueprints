# Brian's Blueprints
Brian's Blueprints for Factorio

# Commands
The "fbp.py" script can be used to split books into a directory structure and later build them back into a single entity as well as to unpack/pack single blueprints from their encoded form into json.  The latter allows working with single blueprints within a book.

#### Split a Book
```
rm -rf book-directory
tools/fbp.py split --outdir=book-directory --infile=my-exported-book.txt
```

It's important to completely remove the old directory before splitting otherwise removed/renamed blueprints will remain in the previous form and be re-introduced when the book is next built.

#### Build a Book
```
tools/fbp.py build --outfile=my-book.txt --indir=book-directory
```

#### Unpack a Single Blueprint
```
tools/fbp.py unpack --outfile=book-directory/blueprint.json --infile=my-exported-blueprint.txt
```

#### Pack a Single Blueprint
```
tools/fbp.py pack --outfile=my-blueprint.txt --infile=book-directory/blueprint.json
```
