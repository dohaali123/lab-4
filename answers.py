def fastareader(pathToFasta):
    """
    Read and parse a FASTA file called sequences.fasta, returning a dictionary of sequences.

    Parameters:
        filename (str): The path to the FASTA file to be read.

    Returns:
        dict: A dictionary where the keys are the sequence headers (without '>' symbol) and the values are the sequences.

    This function reads a FASTA file, extracts the sequence headers and their corresponding sequences, and returns them
    in a dictionary. The headers are used as keys, and the sequences are the corresponding values.

    Example:
    >>> fastareader("test.fasta")
    {'seq1': 'ATCG', 'seq2': 'GCTA', 'seq3': 'CGAT'}
    """
    sequences = {}  # Initialize an empty dictionary to store the sequences
    current_header = None

    with open(pathToFasta, 'r') as fasta_file:
        for line in fasta_file:
            line = line.strip()  # Remove leading and trailing whitespace

            if line.startswith('>'):
                # If the line starts with '>', it's a header line
                current_header = line[1:]  # Remove the '>' symbol and store the header
                sequences[current_header] = ""  # Initialize an empty sequence for this header
            else:
                # If it's not a header line, it's part of the sequence
                sequences[current_header] += line

    return sequences


def getGCpercentage(inputDNA):
    """
    Calculate the GC content percentage of a given DNA sequence.

    This function takes a DNA sequence as input and calculates the GC content percentage by counting the number of
    Guanine (G) and Cytosine (C) bases and dividing it by the total sequence length.

    Parameters:
    inputDNA (str): A DNA sequence for which the GC content percentage needs to be calculated.

    Returns:
    float: The GC content percentage as a floating-point number.

    Example:
    >>> getGCpercentage("ATGATGGCGAGCTAGCATACGCTTCAGACTG")
    0.52
    """
    # Your code here

def getobsCpGexpCpG(inputDNA):
    """
    Calculate the observed CpG to expected CpG ratio (CpG O/E) of a given DNA sequence.

    This function takes a DNA sequence as input and calculates the observed CpG to expected CpG ratio (CpG O/E).
    The CpG O/E ratio is calculated as the number of observed CpG dinucleotides (CG) divided by the expected
    CpG dinucleotide count based on the formula (C * G) / L, where C is the count of Cytosine (C) bases, G is the count
    of Guanine (G) bases, and L is the length of the sequence.

    Parameters:
    inputDNA (str): A DNA sequence for which the CpG O/E ratio needs to be calculated.

    Returns:
    float: The observed CpG to expected CpG ratio (CpG O/E) as a floating-point number.

    Example:
    >>> getobsCpGexpCpG("ATGATGGCGAGCTAGCATACGCTTCAGACTG")
    0.98
    """
    # Your code here

def getCpGislands(inputDNAs):
    """
    Identify CpG islands in a collection of DNA sequences.

    This function takes a dictionary of DNA sequences as input, where the dictionary keys are sequence headers and
    the values are the DNA sequences themselves. It identifies and returns a list of sequence headers that are
    potential CpG islands based on certain criteria.

    Args:
    inputDNAs (dict): A dictionary containing DNA sequences, with headers as keys and sequences as values.

    Returns:
    list: A list of sequence headers that are potential CpG islands.

    The function identifies potential CpG islands based on the following criteria:
    1. The observed CpG to expected CpG ratio (CpG O/E) in the sequence is greater than or equal to 0.65.
    2. The GC content of the sequence is greater than or equal to 50%.
    3. The length of the sequence is greater than or equal to 500 bases.

    Example:
    >>> getCpGislands(inputDNAs)
    ['seq3', 'seq4', 'seq5', 'seq7']
    """
    # Your code here

        
