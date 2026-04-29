class StudentsGWATracker:
    def __init__(self, source_filename):
        self.filename = source_filename
    
    def find_hightest_gwa(self):
        highest_name = ''
        highest_gwa = 5.0

        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    parts_of_line = line.strip().strip(',')
                    if len(parts) == 2:
                        students_name = parts_of_line[0].strip()
                        students_gwa = float(parts_of_line[1].strip())

                        if gwa < highest_gwa:
                            highest_gwa = students_gwa
                            highest_name = students_name

                    if highest_name:
                        print(f'The top student is {highest_name} with a GWA of {highest_gwa}.')
                    else:
                        print('No valid data found.')
        except FileNotFoundError:
            print('Error: students.txt is not found.')