from pcr import pcr
from assemble import assemble
from digest import digest


def simCF(jsonString):
    inputData = json.loads(jsonString)
    steps = inputData['steps']
    sequences = inputData['sequences']
    products = []

    if not sequences or len(sequences) == 0:
        return 'Error: Sequence data is missing. Please include sequence data in the input JSON.'

    def lookupSequence(key):
        foundProduct = next((product for product in products if product['name'] == key), None)
        if foundProduct:
            return foundProduct['sequence']

        foundSequence = sequences.get(key)
        if foundSequence:
            return foundSequence

        raise ValueError(f'Missing sequence for key: {key}')

    for i in range(len(steps)):
        step = steps[i]

        if step['operation'] == 'PCR':
            forwardOligoSeq = lookupSequence(step['forward_oligo'])
            reverseOligoSeq = lookupSequence(step['reverse_oligo'])
            templateSeq = lookupSequence(step['template'])

            product = pcr(forwardOligoSeq, reverseOligoSeq, templateSeq)
            products.append({
                'name': step['output'],
                'sequence': product
            })

        elif step['operation'] == 'Assemble':
            dnaSequences = [lookupSequence(dnaKey) for dnaKey in step['dnas']]

            product = assemble(dnaSequences, step['enzyme'])
            products.append({
                'name': step['output'],
                'sequence': product
            })

        elif step['operation'] == 'Digest':
            dnaSeq = lookupSequence(step['dna'])
            product = digest(dnaSeq, ','.join(step['enzymes']), step['fragSelect'])

            products.append({
                'name': step['output'],
                'sequence': product
            })

        else:
            raise ValueError(f'Unsupported operation: {step['operation']}')

    outputTable = [[product['name'], product['sequence']] for product in products]
    return outputTable