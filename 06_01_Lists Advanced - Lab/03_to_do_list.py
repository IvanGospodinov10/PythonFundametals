notes = []

while True:
    line_import = input()
    if line_import == "End":
        break
    priority, note = line_import.split("-")
    notes.append((int(priority), note))
sorted_note = [note for priority, note in sorted(notes)]
print(sorted_note)