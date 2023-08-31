def performReversal(sequence, start_index, end_index):
    prefix = sequence[:start_index]
    reversed_subsequence = sequence[start_index:end_index][::-1]
    suffix = sequence[end_index:]
    return prefix + reversed_subsequence + suffix

def findBreakpoints(sequence, target_sequence):
    breakpoints = []
    for index in range(len(sequence)-1):
        current_element = sequence[index]
        adjacent_element = sequence[index+1]
        if abs(target_sequence.index(current_element) - target_sequence.index(adjacent_element)) != 1:
            breakpoints.append(index+1)
    return breakpoints

def findMinimumBreakpointReversals(sequences, target_sequence):
    reversals = []
    for sequence in sequences:
        breakpoints = findBreakpoints(sequence[0], target_sequence)
        for start_index_i in range(len(breakpoints)-1):
            for end_index_i in range(start_index_i+1, len(breakpoints)):
                reversals.append((performReversal(sequence[0], breakpoints[start_index_i], breakpoints[end_index_i]), sequence[1] + [(breakpoints[start_index_i]-1, breakpoints[end_index_i]-1)]))
    min_bp = len(target_sequence)
    minimum_reversals = []
    for reversal in reversals:
        num_breakpoints = len(findBreakpoints(reversal[0], target_sequence))
        if num_breakpoints < min_bp:
            min_bp = num_breakpoints
            minimum_reversals = [reversal]
        elif num_breakpoints == min_bp:
            minimum_reversals.append(reversal)
    return minimum_reversals

def getReversalDistanceWithHistories(sequence, target_sequence):
    sequence = ["-"] + sequence + ["+"]
    target_sequence = ["-"] + target_sequence + ["+"]
    reversals = 0
    current_sequences = [(sequence, [])]
    while target_sequence not in [current_sequence[0] for current_sequence in current_sequences]:
        current_sequences = findMinimumBreakpointReversals(current_sequences, target_sequence)
        reversals += 1
    return reversals, current_sequences

def buildSequencesFromHistory(sequence, reversal_history):
    sequence_history = [sequence]
    for reversal_start, reversal_end in reversal_history:
        sequence_history.append(performReversal(sequence_history[-1], reversal_start, reversal_end))
    return sequence_history

if __name__ == "__main__":

    sequence = [8, 6, 7, 9, 4, 1, 3, 10, 2, 5]

    target_sequence = [8, 2, 7, 6, 9, 1, 5, 3, 10, 4]
        
        
        
        
    
    rev_distance, histories = getReversalDistanceWithHistories(sequence, target_sequence)
    for history in histories:
        sequences_from_history = buildSequencesFromHistory(sequence, history[1])
        print("Sequence:", sequence)
        print("Target:", target_sequence)
        print("Distance:", rev_distance)
        for s in sequences_from_history:
            print(s)
        print("\n")