import time

with open("aquila2.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    print(stripped_line)
    time.sleep(.05)

print("""\n""")
totd="""Thought of the Day: Heresy grows from idleness."""
totd_centered = totd.center(150)
print(totd_centered)
