import subprocess
import os

# Delete the old tree in README.md if it exists
if os.path.exists('README.md'):
    with open('README.md', 'r') as f:
        lines = f.readlines()
    with open('README.md', 'w') as f:
        for line in lines:
            if '```' not in line:
                f.write(line)
            else:
                break

# Run the 'tree' command and capture the output, ignoring folder names "venv", ".idea", and "generate_tree.py"
output = subprocess.check_output(
    ['tree', '-I', '__pycache__|db.sqlite3|postgres-data|logs|static|media|.idea|generate_tree.py|venv'],
    text=True)

# Append the output to the README.md file
with open('README.md', 'a') as f:
    f.write('```\n')
    f.write(output)
    f.write('```\n')
