class IntegerProcessorWithPowered:
    
    def __init__(self, source_filename):
        self.source_filename = source_filename

    def process_integers(self):
        try:
            with open(self.source_filename, 'r') as file, \
                open('program_4_integer_processor_containing_power_functions/double.txt', 'w') as squared_file, \
                open('program_4_integer_processor_containing_power_functions/triple.txt', 'w') as cube_file:

                for line in file:
                    clean_line = line.strip()
                    if not clean_line:
                        continue

                    number = int(clean_line)

                    if number % 2 == 0:
                        squared = number ** 2
                        squared_file.write(f'{squared}\n')

                    else:
                        cube = number ** 3
                        cube_file.write(f'{cube}\n')

                print('Processing complete. Files double.txt and triple.txt have been created.') 

        except FileNotFoundError:
            print(f'Error: {self.source_filename} not found.')
        except ValueError:
            print('Error: The file contains non-integer data.')        