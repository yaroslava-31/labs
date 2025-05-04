from Bio import SeqIO

with open('combined_species.gb', 'r') as handle:
    for record in SeqIO.parse(handle, 'genbank'):
        for feature in record.features:
            if feature.type == 'CDS':
                protein_seq = feature.qualifiers['translation'][0]
                location = feature.location
                coding_location = f"[{location.start}:{location.end}]({location.strand})"
                print(f"{record.id}: {record.description}")
                print(f"Coding sequence location = {coding_location}")
                print("Translation =")
                print(protein_seq)
                print("\n")
