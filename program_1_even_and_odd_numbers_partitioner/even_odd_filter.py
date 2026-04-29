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
                if len(even) > 1:    
                    main_list = ', '.join(even[:-1])
                    end_number_list = even[-1]
                    even_text_file.write(f'{main_list}, and {end_number_list}')

                else:
                    even_text_file.write(', '.join(even) + '.')

            with open('program_1_even_and_odd_numbers_partitioner/odd.txt', 'w') as odd_text_file:        
                if len(odd) > 1:
                    main_list = ', '.join(odd[:-1])
                    end_number_list = odd[-1]
                    odd_text_file.write(f'{main_list}, and {end_number_list}')

                else:
                    odd_text_file.write(', '.join(odd) + '.')

            print('Analyzing complete successfully.')

        except FileNotFoundError:
            print('Error: File not found')
        except ValueError:
            print('Error: The file contains text that is not a number')
        except Exception as e:
            print(f'An unexpected error occured: {e}')