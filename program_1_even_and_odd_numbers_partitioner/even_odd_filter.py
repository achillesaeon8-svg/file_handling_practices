class OddAndEvenSettings:
    def __init__(self, source_filename):
        self.chosen_file = source_filename
    
    def sort_numbers(self):
        try:
            with open(self.chosen_file, 'r') as file:
                for line in file:
                    number = int(line.strip())

                    if number % 2 == 0:
                        open('even.txt', 'w')
                    else:
                        open('odd.txt', 'r')
                    
            print('Analyzing complete successfully.')
        except FileNotFoundError:
            print('Error: File not found')
        except ValueError:
            print('Error: The file contains text that is not a number')
        except Exception as e:
            print(f'An unexpected error occured: {e}')