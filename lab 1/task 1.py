
def main(origin_string: str, virus: str):
    formatted_virus = virus.lower()
    found_index = origin_string.lower().find(formatted_virus)
    if virus == '' or origin_string == '':
        return "ERROR! String and virus must contain at least 1 character"
    while found_index != -1:
        origin_string = origin_string[:found_index] \
                        + origin_string[found_index + len(formatted_virus):]
        found_index = origin_string.lower().find(formatted_virus)
    return origin_string



if __name__ == '__main__':
    origin_string, virus = input(), input()
    result = main(origin_string, virus)
    print(result)
