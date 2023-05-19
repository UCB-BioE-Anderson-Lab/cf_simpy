from .construction_file import ConstructionFile


def parseCF(*blobs):
    operationRegex = r'^(PCR|pcr|digest|Digest|ligate|Ligate|assemble|Assemble|gibson|Gibson|blunt|Blunt|transform|Transform)'
    sequenceDataRegex = r'^[ACGTRYSWKMBDHVNUacgtryswkmbdhvnu*]+$'

    # Helper function to tokenize construction data
    def preprocessData(data):
        if isinstance(data, list):
            if all(isinstance(item, list) for item in data):
                # Handle 2D array
                return '\n'.join(['\t'.join(map(str, row)) for row in data])
            elif all(isinstance(item, str) or isinstance(item, int) for item in data):
                # Handle 1D array
                return '\t'.join(map(str, data))
            else:
                raise ValueError('Unsupported input type for preprocessData function')
        else:
            # Handle single-cell value
            return str(data)

    def tokenize(text):
        # Split the text into tokens using whitespace, commas, and slashes as separators
        tokens = text.split(r'[\s,/()]+')
        # Remove any punctuation from each token
        tokens = [token.replace(r'[(),]', '') for token in tokens]
        # Remove the words 'on' and 'with' from the tokens
        tokens = [token for token in tokens if token not in ['on', 'with']]
        # Remove any empty tokens resulting from punctuation removal
        tokens = [token for token in tokens if token != '']
        return tokens

    # Preprocess input data into a single text string
    singleblob = ''
    for blob in blobs:
        singleblob += preprocessData(blob) + '\n'

    # Tokenize the singleblob into a 2D array of strings
    preprocessedData = [tokenize(line) for line in singleblob.strip().split('\n')]

    # Helper function to parse construction data
    def parseConstructionData(data):
        def processTokens(tokens):
            operation = tokens[0]

            step = {
                'operation': operation
            }

            if operation.lower() == 'pcr':
                step['output'] = tokens[-1]
                step['forward_oligo'] = tokens[1]
                step['reverse_oligo'] = tokens[2]
                step['template'] = tokens[3]
                if tokens[4]:
                    step['product_size'] = int(tokens[4])
            elif operation.lower() == 'assemble':
                step['output'] = tokens[-1]
                step['dnas'] = tokens[1:-2]
                step['enzyme'] = tokens[-2]
            elif operation.lower() == 'ligate':
                step['output'] = tokens[-1]
                step['dnas'] = tokens[1:-1]
            elif operation.lower() == 'digest':
                step['output'] = tokens[-1]
                step['dna'] = tokens[1]
                step['enzymes'] = tokens[2]
                step['fragselect'] = int(tokens[3])
            elif operation.lower() == 'transform':
                step['output'] = tokens[4]
                step['dna'] = tokens[1]
                step['strain'] = tokens[2]
                step['antibiotics'] = tokens[3]
                step['temperature'] = float(tokens[5])

            return step

        # Check if the input is a range of cells
        if isinstance(data, list) and len(data) > 0 and len(data[0]) > 1:
            return [processTokens(row) for row in data]
        # Check if the input is a series of lines
        if isinstance(data, list) and len(data) > 1 and len(data[0]) == 1:
            # Split each element of the row into tokens and filter out empty tokens
            return [processTokens(tokenize(line)) for line in data if line != '']
        # Check if the input is a string
        if isinstance(data, str):
            # Split the string into lines, remove empty lines and comments
            lines = [line for line in data.split(r'\r?\n') if not line.match(r'^\s*$|//')]
            # Split each line into an array of tokens and filter out empty tokens
            return [processTokens(tokenize(line)) for line in lines if line != '']
        # If none of the above cases match, throw an error
        raise ValueError('Unable to parse construction data')

    # Helper function to parse sequence data
    def parseSequenceData(data):
        sequenceObj = {}

        # Check if the input is a 2D array
        if isinstance(data, list) and len(data) > 0 and len(data[0]) > 1:
            for row in data:
                name = row[0]
                sequence = ''.join(row[1:])
                sequenceObj[name] = sequence
        # Check if the input is a string (tab-separated or FASTA format)
        elif isinstance(data, str):
            # Check if the input is in FASTA format
            if data.startswith('>'):
                import re
                fastaRegex = re.compile(r'>\(\S+).*\n([ACGTRYSWKMBDHVNUacgtryswkmbdhvnu*]+)')
                matches = fastaRegex.findall(data)
                for match in matches:
                    name = match[0]
                    sequence = match[1]
                    sequenceObj[name] = sequence
            # Assume the input is in tab-separated format
            else:
                lines = data.split(r'\r?\n')
                for line in lines:
                    name, sequence = line.split(r'\t')
                    sequenceObj[name] = sequence
        # If none of the above cases match, throw an error
        else:
            raise ValueError('Unable to parse sequence data')

        return sequenceObj

    # Helper function to validate the input data
    def validateData(steps, sequences):
        # Add your implementation here
        pass

    # Initialize construction and sequence data storage
    steps = []
    sequences = {}

    # Iterate over preprocessedData
    for row in preprocessedData:
        if re.match(operationRegex, row[0]):
            parsedConstructionData = parseConstructionData([row])
            steps.extend(parsedConstructionData)
        else:
            name = row[0]
            sequence = ''.join(row[1:])
            if re.match(sequenceDataRegex, sequence):
                sequences[name] = sequence

    # Validate the input data
    validateData(steps, sequences)

    # Bundle all the info together and output an organized object or array
    return ConstructionFile(steps, sequences)