# CF SimPy

CF SimPy is a Python-based molecular biology simulator that uses the Construction File (CF) format to plan, simulate, and document experiments. The CF format is a structured JSON format for specifying a series of molecular biology operations.

## Structure

The project is structured into two main directories:

- `cf_simpy`: This directory contains the Python scripts that make up the simulator. It includes the following files:
  - `polynucleotide.py`: This file defines the `Polynucleotide` class, which represents a DNA or RNA molecule. It includes methods for creating a polynucleotide, getting its reverse complement, and performing PCR.
  - `pcr.py`: This file contains the `pcr` function, which simulates a PCR reaction.
  - `revcomp.py`: This file contains the `revcomp` function, which returns the reverse complement of a given DNA sequence.
- `cf`: This directory contains a JavaScript file, `cf.gs.js`, which provides a detailed description of the CF format and its syntax.

## Usage

To use the simulator, you need to create a CF that specifies the steps of your experiment. Each step is represented as a JSON object with an `operation` property that defines the type of operation (e.g., 'PCR', 'Assemble', 'Transform', 'Digest', 'Ligate'). Other properties depend on the type of operation and may include input sequences, output products, enzymes, and other parameters.

The CF also includes a `sequences` object that contains key-value pairs of sequence names and their corresponding DNA sequences. These sequences are used as inputs in the operations.

Once you have created your CF, you can use the functions in `polynucleotide.py` and `pcr.py` to simulate the steps of your experiment. The simulator will return the expected products of the operations, allowing you to verify the design of your experiment before performing it in the lab.

## Testing

The project includes a set of tests in the `tests` directory. These tests use the pytest framework and cover the main functions of the simulator. You can run the tests using the `pytest` command.

## Future Work

Future work on CF SimPy may include adding more operations to the simulator, improving the accuracy of the simulations, and developing a graphical user interface for creating and editing CFs.# CF SimPy

CF SimPy is a Python-based simulator for molecular biology experiments. The simulator uses a Construction File (CF) to define a series of operations that represent an experiment. The CF is a structured format that can be represented as JSON, XML, or a human-readable format. The simulator currently supports the Polymerase Chain Reaction (PCR) operation, with plans to support more operations in the future.

## Project Structure

The project is organized into two main directories:

- `cf_simpy`: This directory contains the Python scripts that make up the simulator. It includes the following files:
  - `polynucleotide.py`: This file defines the `Polynucleotide` class, which represents a DNA molecule.
  - `pcr.py`: This file contains the `pcr` function, which simulates a PCR reaction.
  - `revcomp.py`: This file contains the `revcomp` function, which returns the reverse complement of a given DNA sequence.

- `cf`: This directory contains a JavaScript file, `cf.gs.js`, which provides a detailed description of the CF format and its syntax. The CF format is a structured format that can be represented as JSON, XML, or a human-readable format. The CF includes a `sequences` object that contains key-value pairs of sequence names and their corresponding DNA sequences. These sequences are used as inputs in the operations.

## Polynucleotide

A `Polynucleotide` is a class that represents a DNA molecule. It has several properties including `sequence`, `ext5`, `ext3`, `is_double_stranded`, `is_circular`, `mod_ext5`, and `mod_ext3`. The `sequence` is the DNA sequence of the molecule. The `ext5` and `ext3` properties represent the 5' and 3' extensions of the molecule, respectively. The `is_double_stranded` and `is_circular` properties are boolean values that indicate whether the molecule is double-stranded and whether it is circular, respectively. The `mod_ext5` and `mod_ext3` properties represent the 5' and 3' modifications of the molecule, respectively.

## Construction File (CF)

A Construction File (CF) is a structured format that defines a series of operations that represent an experiment. Each operation in the CF has a `type` property that specifies the type of operation (e.g., `pcr`). Other properties depend on the type of operation and may include input sequences, output products, enzymes, and other parameters.

## Simulator Usage

Once you have created your CF, you can use the functions in `polynucleotide.py` and `pcr.py` to simulate the steps of your experiment. The simulator currently supports the Polymerase Chain Reaction (PCR) operation, with plans to support more operations in the future.

## PCR Operation

The PCR operation is defined in the CF with the `type` property set to `pcr`. The operation includes the following properties:

- `for_oligo`: The forward oligo used in the PCR reaction.
- `rev_oligo`: The reverse oligo used in the PCR reaction.
- `template`: The template DNA used in the PCR reaction.

The `pcr` function in `pcr.py` takes these inputs and simulates the PCR reaction, returning the resulting DNA product.

## Future Work

Future plans for CF SimPy include adding support for more operations, such as restriction digestion and ligation, and improving the accuracy of the simulation. We also plan to add more features to the `Polynucleotide` class, such as support for RNA molecules and more complex modifications.

## Construction File (CF)

A Construction File (CF) is a structured format that defines a series of operations that represent an experiment. Each operation in the CF has a `type` property that specifies the type of operation (e.g., `pcr`). Other properties depend on the type of operation and may include input sequences, output products, enzymes, and other parameters. The CF also includes a `sequences` object that contains key-value pairs of sequence names and their corresponding DNA sequences. These sequences are used as inputs in the operations.

The CF format is flexible and can be represented in various formats including JSON, XML, or a human-readable format. The human-readable format is particularly useful for manual creation and editing of CFs. In this format, a user can specify sequences as strings-only (as fasta or tsv) and they are interpreted as Polynucleotides. In a JSON or XML representation, you would explicitly encode a Polynucleotide.

## Polynucleotide

A `Polynucleotide` is a class that represents a DNA molecule. It has several properties including `sequence`, `ext5`, `ext3`, `is_double_stranded`, `is_circular`, `mod_ext5`, and `mod_ext3`. The `sequence` is the DNA sequence of the molecule. The `ext5` and `ext3` properties represent the 5' and 3' extensions of the molecule, respectively. The `is_double_stranded` and `is_circular` properties are boolean values that indicate whether the molecule is double-stranded and whether it is circular, respectively. The `mod_ext5` and `mod_ext3` properties represent the 5' and 3' modifications of the molecule, respectively.

## Simulator Usage

Once you have created your CF, you can use the functions in `polynucleotide.py` and `pcr.py` to simulate the steps of your experiment. The simulator currently supports the Polymerase Chain Reaction (PCR) operation, with plans to support more operations in the future. The functions for these activities are all separate objects, not methods of polynucleotide.

## PCR Operation

The PCR operation is defined in the CF with the `type` property set to `pcr`. The operation includes the following properties:

- `for_oligo`: The forward oligo used in the PCR reaction.
- `rev_oligo`: The reverse oligo used in the PCR reaction.
- `template`: The template DNA used in the PCR reaction.

The `pcr` function in `pcr.py` takes these inputs and simulates the PCR reaction, returning the resulting DNA product.

## Data Structures/Models

For a detailed description of the data structures and models used in CF SimPy, please refer to the [Model Definitions](./docs/model_definitions.md) document. It provides comprehensive information about the properties and functionalities of the `Polynucleotide` class and other relevant models.
