def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        current_sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_sequence:
                    sequences.append(current_sequence)
                current_sequence = ''
            else:
                current_sequence += line
        sequences.append(current_sequence)
    return sequences

def generate_consensus_string(profile_matrix):
    consensus = ''
    nucleotides = ['A', 'C', 'G', 'T']
    for column in zip(*profile_matrix):
        max_count = max(column)
        max_indices = [i for i, count in enumerate(column) if count == max_count]
        consensus += nucleotides[max_indices[0]]
    return consensus

def generate_profile_matrix(sequences):
    profile_matrix = [[0] * len(sequences[0]) for _ in range(4)]
    nucleotides = ['A', 'C', 'G', 'T']
    for sequence in sequences:
        for i, nucleotide in enumerate(sequence):
            row_index = nucleotides.index(nucleotide)
            profile_matrix[row_index][i] += 1
    return profile_matrix

def format_profile_matrix(profile_matrix):
    nucleotides = ['A', 'C', 'G', 'T']
    formatted_profile = ''
    for nucleotide, counts in zip(nucleotides, profile_matrix):
        formatted_profile += nucleotide + ': ' + ' '.join(str(count) for count in counts) + '\n'
    return formatted_profile

def generate_consensus_and_profile(file_path):
    sequences = read_fasta(file_path)
    profile_matrix = generate_profile_matrix(sequences)
    consensus = generate_consensus_string(profile_matrix)
    formatted_profile = format_profile_matrix(profile_matrix)
    return consensus, formatted_profile

# Example usage
file_path = 'consensus.txt'
consensus, profile = generate_consensus_and_profile(file_path)
print(consensus)
print(profile)
