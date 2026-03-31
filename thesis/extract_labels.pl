while (<>) { while (/\label\{([^}]+)\}/g) { print "$1\n" } }
