-m manifest location in excel format, it might work with csv, but I haven't tested

-r1: read 1 location, gzipped

-r2: read 2 location, gzipped

-o: optional, what folder to put things into

-H: optional, if your file doesn't have a header

-t: optional, trim barcode and random-mer

-r: optional, length of random-mer 10 or 11

You'll need to install biopython

`pip install biopython`

or

`conda install biopython`

This will not remove the barcode from read2 if the read is short enough to get that far. It shouldn't matter 
for what we're doing though. Unless I'm wrong. Which happens frequently.