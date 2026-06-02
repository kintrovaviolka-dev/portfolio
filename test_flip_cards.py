import re

with open('portfolio.html', 'r') as f:
    content = f.read()

if 'onclick="this.classList.toggle(\'flipped\')"' in content:
    print("Found inline onclick on flip cards.")
