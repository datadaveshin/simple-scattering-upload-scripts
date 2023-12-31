class MacroMolecule:
    def __init__(self, name, type, sequence, amount, units, database, database_id):
        self.name = name
        self.type = type
        self.sequence = sequence
        self.amount = amount
        self.units = units
        self.database = database
        self.database_id = database_id

    def __str__(self):
        return f"{self.name}, {self.type}, {self.sequence}, {self.amount}, {self.units}, {self.database}, {self.database_id}"


class SmallMolecule:
    def __init__(self, name, formula, amount, units, database, database_id):
        self.name = name
        self.formula = formula
        self.amount = amount
        self.units = units
        self.database = database
        self.database_id = database_id

    def __str__(self):
        return f"{self.name}, {self.formula}, {self.amount}, {self.units}, {self.database}, {self.database_id}"


filename_correct = True
filename = input("Enter dataset code: ")
while filename_correct:
    correct = input(f"\nYou entered:\n{filename}\nIs this correct?(y/n): ")
    if correct == "y":
        filename_correct = False

print()
filerange_correct = True
while filerange_correct:
    file_prefix = input("Enter file prefix: ")
    file_extension = input("Enter file extension: ")
    file_start = input("Enter file start: ")
    file_end = input("Enter file end: ")
    file_start_num = int(file_start.lstrip("0"))
    file_end_num = int(file_end.lstrip("0"))
    num_samples = file_end_num - file_start_num + 1
    num_samples_magnitude = len(file_start)
    correct = input(
        f"\nYou entered:\n{file_prefix}.{file_start}{file_extension} to {file_prefix}.{file_end}{file_extension}\nIs this correct?(y/n): "
    )
    if correct == "y":
        filerange_correct = False

print()
solvent_correct = True
while solvent_correct:
    solvent = input("Enter solvent: ")
    correct = input(f"\nYou entered:\n{solvent}\nIs this correct?(y/n): ")
    if correct == "y":
        solvent_correct = False

print()
ph_correct = True
while ph_correct:
    ph = input("Enter pH: ")
    correct = input(f"\nYou entered:\n{ph}\nIs this correct?(y/n): ")
    if correct == "y":
        ph_correct = False

print()
macromolecules = []
macromolecule_running = True
while macromolecule_running:
    macromolecule_name = input("Enter macromolecule name: ")
    macromolecule_type = input("Enter macromolecule type (protein, DNA, RNA, LNP): ")
    macromolecule_sequence = input("Enter macromolecule sequence or formula: ")
    macromolecule_amount = input("Enter macromolecule amount: ")
    macromolecule_units = input("Enter macromolecule units: ")
    macromolecule_database = input("Enter macromolecule database: ")
    macromolecule_database_id = input("Enter macromolecule database ID: ")
    correct = input(
        f"\nYou entered:\n{macromolecule_name}, {macromolecule_type}, {macromolecule_sequence}, {macromolecule_amount}, {macromolecule_units}, {macromolecule_database}, {macromolecule_database_id}\nIs this correct?(y/n): "
    )
    if correct == "y":
        macromolecule = MacroMolecule(
            macromolecule_name,
            macromolecule_type,
            macromolecule_sequence,
            macromolecule_amount,
            macromolecule_units,
            macromolecule_database,
            macromolecule_database_id,
        )
        macromolecules.append(macromolecule)
    done = input("Done? (y/n): ")
    if done == "y":
        macromolecule_running = False

print()
small_molecules = []
small_molecule_running = True
while small_molecule_running:
    small_molecule_name = input("Enter small molecule name: ")
    small_molecule_formula = input("Enter small molecule formula: ")
    small_molecule_amount = input("Enter small molecule amount: ")
    small_molecule_units = input("Enter small molecule units: ")
    small_molecule_database = input("Enter small molecule database: ")
    small_molecule_database_id = input("Enter small molecule database ID: ")
    correct = input(
        f"\nYou entered:\n{small_molecule_name}, {small_molecule_formula}, {small_molecule_amount}, {small_molecule_units}, {small_molecule_database}, {small_molecule_database_id}\nIs this correct?(y/n): "
    )
    if correct == "y":
        small_molecule = SmallMolecule(
            small_molecule_name,
            small_molecule_formula,
            small_molecule_amount,
            small_molecule_units,
            small_molecule_database,
            small_molecule_database_id,
        )
        small_molecules.append(small_molecule)
    done = input("Done? (y/n): ")
    if done == "y":
        small_molecule_running = False

# Make a .csv file using the filename
output = open(f"{filename}.csv", "w")
# Write the header
header = ""
header += "Filename,"
header += "Solvent,"
header += "pH,"
for macromolecule in macromolecules:
    header += f"macromolecule_name,macromolecule_type,macromolecule_sequence,macromolecule_amount,macromolecule_units,macromolecule_database,macromolecule_database_id,"
for small_molecule in small_molecules:
    header += f"small_molecule_name,small_molecule_formula,small_molecule_amount,small_molecule_units,small_molecule_database,small_molecule_database_id,"
header += "\n"
output.write(header)
# Write the data
for i in range(int(num_samples)):
    row = ""
    row += f"{file_prefix}.{str(i+1).zfill(num_samples_magnitude)}{file_extension},"
    row += f"{solvent},"
    row += f"{ph},"
    for macromolecule in macromolecules:
        row += f"{macromolecule.name},{macromolecule.type},{macromolecule.sequence},{macromolecule.amount},{macromolecule.units},{macromolecule.database},{macromolecule.database_id},"
    for small_molecule in small_molecules:
        row += f"{small_molecule.name},{small_molecule.formula},{small_molecule.amount},{small_molecule.units},{small_molecule.database},{small_molecule.database_id},"
    row += "\n"
    output.write(row)
