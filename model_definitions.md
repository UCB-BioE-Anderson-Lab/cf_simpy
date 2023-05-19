/**
 * A Construction File (CF) is a structured format for specifying a series of molecular biology operations. CFs are used to plan, simulate, and document experiments.
 *
 * Syntax:
 * A Construction File is represented as a JSON object, containing two main elements: 'steps'
 * and 'sequences'. The 'steps' is an array of objects, where each object represents a construction
 * step with its associated operation, input sequences, and output product. The 'sequences' is an object
 * containing key-value pairs, where each key is a unique identifier for a DNA sequence, and the value is the
 * actual sequence as a Polynucleotide object.
 *
 * Example:
 * Here's a simple example of a Construction File that demonstrates PCR and assembly steps.
 *
 * {
 *   "steps": [
 *     {
 *       "operation": "PCR",
 *       "output": "P6",
 *       "forward_oligo": "P6libF",
 *       "reverse_oligo": "P6libR",
 *       "template": "pTP1",
 *       "product_size": 3583
 *     },
 *     {
 *       "operation": "Assemble",
 *       "output": "pP6",
 *       "dnas": ["P6"],
 *       "enzyme": "BsaI"
 *     }
 *   ],
 *   "sequences": {
 *     "P6libF": {"sequence": "ccaaaggtctcATTATANNNNNNNNNNNNNNNNNTGTCAANNNNGAacccaggactcctcgaagtcgttcttaagacaac", "ext5": null, "ext3": null, "is_double_stranded": false, "is_circular": false, "mod_ext5": "hydroxyl", "mod_ext3": null},
 *     "P6libR": {"sequence": "cagttGGTCTCAATAATNNNNNNANNNNGTtagtatttctcctcgtctacggttaactgatactc", "ext5": null, "ext3": null, "is_double_stranded": false, "is_circular": false, "mod_ext5": "hydroxyl", "mod_ext3": null},
 *     "pTP1": {"sequence": "ATTACCGCCTTTGAGTGG", "ext5": "", "ext3": "", "is_double_stranded": true, "is_circular": true, "mod_ext5": null, "mod_ext3": null}
 *   }
 * }
 *
 * In this example, the 'steps' array has two steps: PCR and Assemble. The PCR step uses forward and
 * reverse oligos "P6libF" and "P6libR", with "pTP1" as the template. The PCR product is named "P6". The Assemble
 * step uses the "P6" PCR product and "BsaI"-based Golden Gate Assembly to create a final output named "pP6". The 'sequences'
 * object contains the sequences for "P6libF", "P6libR", and "pTP1" as Polynucleotide objects.
 *
 * @typedef {Object} ConstructionFile
 * @property {Array.<PCR|Assemble|Transform|Digest|Ligate>} steps - An array of construction steps, where each step is an operation object.
 * @property {Object.<string, Polynucleotide>} sequences - An object containing key-value pairs of sequence names and their corresponding Polynucleotide objects.
 * 
 * @typedef {Object} Polynucleotide
 * @property {string} sequence - The DNA sequence following the regex pattern /^[ATCGNRKYSWBVHD]+$/.
 * @property {string|null} ext5 - The 5' extension, which can be null or a string following the regex pattern /^(-)?[ATCG]+$/.
 * @property {string|null} ext3 - The 3' extension, which can be null or a string following the regex pattern /^(-)?[ATCG]+$/.
 * @property {boolean} is_double_stranded - Indicates if the polynucleotide is double-stranded.
 * @property {boolean} is_circular - Indicates if the polynucleotide is circular.
 * @property {string|null} mod_ext5 - The 5' modification of coding strand.
 * @property {string|null} mod_ext3 - The 5' modification of non-coding strand.
 *
 * @typedef {Object} PCR
 * @property {'PCR'} operation - The type of operation.
 * @property {string} output - The name of the output product of the operation (DNA identifier).
 * @property {string} forward_oligo - The name of the forward primer used in PCR operation (DNA identifier).
 * @property {string} reverse_oligo - The name of the reverse primer used in PCR operation (DNA identifier).
 * @property {string} template - The name of the template DNA used in PCR operation (DNA identifier).
 * @property {number|undefined} [product_size] - The expected product size in PCR operation (optional).
 * 
 * @typedef {Object} Assemble
 * @property {'Assemble'} operation - The type of operation.
 * @property {string} output - The name of the output product of the operation (DNA identifier).
 * @property {Array.<string>} dnas - An array of DNA part identifiers used in the Assemble operation.
 * @property {'AarI'|'BbsI'|'BsaI'|'BsmBI'|'SapI'|'BseRI'|'Gibson'|'Yeast'} enzyme - The enzyme used in the Assemble operation.
 * 
 * @typedef {Object} Transform
 * @property {'Transform'} operation - The type of operation.
 * @property {string} output - The name of the output product of the operation (DNA identifier).
 * @property {string} dna - The identifier of the DNA used in the Transform operation.
 * @property {string} strain - The bacterial strain used in the Transform operation.
 * @property {'Amp'|'Carb'|'Cam'|'Kan'|'Gen'|'Spec'|'Trim'} antibiotics - The antibiotics used in the Transform operation.
 * @property {number} [temperature] - The temperature used in the Transform operation (optional).
 * 
 * @typedef {Object} Digest
 * @property {'Digest'} operation - The type of operation.
 * @property {string} output - The name of the output product of the operation (DNA identifier).
 * @property {string} dna - The identifier of the DNA used in the Digest operation.
 * @property {number} fragSelect - The index, counted from zero, of the output fragment.
 * @property {(Array.<'AarI'|'BbsI'|'BsaI'|'BsmBI'|'SapI'|'BseRI'|'BamHI'|'BglII'|'EcoRI'|'XhoI'|'SpeI'|'XbaI'|'PstI'>|Array.<string>)} enzymes - The enzymes used in the Digest operation.
 * 
 * @typedef {Object} Ligate
 * @property {'Ligate'} operation - The type of operation.
 * @property {string} output - The name of the output product of the operation (DNA identifier).
 * @property {Array.<string>} dnas - An array of DNA part identifiers used in the Ligate operation.
 */

