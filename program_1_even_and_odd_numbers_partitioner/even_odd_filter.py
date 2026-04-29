class OddAndEvenSettings:
    def __init__(self, source_filename):
        self.chosen_file = source_filename
    
    def sort_numbers(self):
        try:
            even = []
            odd = []
            with open(self.chosen_file, 'r') as file:
                for line in file:
                    clean_line = line.strip()
                    if not clean_line:
                        continue

                    number = int(clean_line)

                    if number % 2 == 0:
                        even.append(str(number))
                    else:
                        odd.append(str(number))

            with open('program_1_even_and_odd_numbers_partitioner/even.txt', 'w') as even_text_file:
                result = ', '.join(odd) + '.'
                even_text_file.write(result)
            with open('program_1_even_and_odd_numbers_partitioner/odd.txt', 'w') as odd_text_file:        
                result = ', '.join(even) + '.'
                odd_text_file.write(result) + '.'
                
            print('Analyzing complete successfully.')

        except FileNotFoundError:
            print('Error: File not found')
        except ValueError:
            print('Error: The file contains text that is not a number')
        except Exception as e:
            print(f'An unexpected error occured: {e}')