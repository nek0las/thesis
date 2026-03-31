while (<>) { while (/\ref\{([^}]+)\}/g) { print "$1\n" } }
