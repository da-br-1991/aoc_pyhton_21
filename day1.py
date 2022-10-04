def file_reader():
    data = []
    with open("input/01.txt", "r") as input_data:
        for i in input_data:
            data.append(i)
    return data

def measurement_analyzer():
