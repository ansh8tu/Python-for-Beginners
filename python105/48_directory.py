from pathlib import Path

path = Path('concert')
print(path.exists())

newPath =Path()
patternSearch = newPath.glob('*.py')

for file in patternSearch:
    print(file)