import re, glob, os
labels = set()
refs = set()
for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.tex'):
            content = open(os.path.join(root, file), encoding='utf-8', errors='ignore').read()
            labels.update(re.findall(r'\\label\{([^}]+)\}', content))
            refs.update(re.findall(r'\\ref\{([^}]+)\}', content))
missing = refs - labels
for m in sorted(missing):
    print(m)

