from Bio import SeqIO

def gc_content(sequence):
    """Вычисляет GC-состав последовательности."""
    gc_count = sequence.count('G') + sequence.count('C')
    return gc_count / len(sequence) if len(sequence) > 0 else 0

records_gc = []

with open('combined_species.gb', 'r') as input_handle:
    for record in SeqIO.parse(input_handle, 'genbank'):
        gc = gc_content(str(record.seq))
        records_gc.append((record.id, record.description, gc))

records_gc.sort(key=lambda x: x[2])

for record_id, description, gc in records_gc:
    print(f"{record_id}: {description}, GC = {gc}")
