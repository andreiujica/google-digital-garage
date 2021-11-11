import datetime

sex_dict = {
    '1': "M",
    '2': "F",
    '3': "M",
    '4': "F",
    '5': "M",
    '6': "F",
    '7': None,
    '8': None,
    '9': None
}

place_dict = {
    '01': 'Alba',
    '02': 'Arad',
    '03': 'Arges',
    '04': 'Bacau',
    '05': 'Bihor',
    '06': 'Bistrita-Nasaud',
    '07': 'Botosani',
    '08': 'Brasov',
    '09': 'Braila',
    '10': 'Buzau',
    '11': 'Caras-Severin',
    '12': 'Cluj',
    '13': 'Constanta',
    '14': 'Covasna',
    '15': 'Dambovita',
    '16': 'Dolj',
    '17': 'Galati',
    '18': 'Gorj',
    '19': 'Harghita',
    '20': 'Hunedoara',
    '21': 'Ialomita',
    '22': 'Iasi',
    '23': 'Ilfov',
    '24': 'Maramures',
    '25': 'Mehedinti',
    '26': 'Mures',
    '27': 'Neamt',
    '28': 'Olt',
    '29': 'Prahova',
    '30': 'Satu Mare',
    '31': 'Salaj',
    '32': 'Sibiu',
    '33': 'Suceava',
    '34': 'Teleorman',
    '35': 'Timis',
    '36': 'Tulcea',
    '37': 'Vaslui',
    '38': 'Vlacea',
    '39': 'Vrancea',
    '40': 'Bucuresti',
    '41': 'Bucuresti S.1',
    '42': 'Bucuresti S.2',
    '43': 'Bucuresti S.3',
    '44': 'Bucuresti S.4',
    '45': 'Bucuresti S.5',
    '46': 'Bucuresti S.6',
    '51': 'Calarasi',
    '52': 'Giurgiu',
}


def get_CNP():
    length_flag = False
    cnp = input("Please enter a CNP: ")
    if len(cnp) == 13:
        length_flag = True
    return cnp, length_flag


def get_sex(cnp):
    return cnp[0], cnp[0] in sex_dict


def get_birthdate(cnp):
    day_flag = True
    year = cnp[1:3]
    month = cnp[3:5]
    day = cnp[5:7]
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        day_flag = False
    return cnp[1:7], day_flag


def get_place_of_birth(cnp):
    place_flag = False
    if cnp[7:9] in place_dict:
        place_flag = True
    return cnp[7:9], place_flag


def validate_control(cnp):
    control_flag = False
    control_number = [int(x) for x in "279146358279"]
    cnp_list = [int(y) for y in cnp]
    result = 0
    for i in range(len(control_number)):
        result += cnp_list[i] * control_number[i]
    control = result % 11
    if control == 10:
        control = 1
    if cnp_list[-1] == control:
        control_flag = True
    return control, control_flag

def print_user_profile(cnp, sex, birthdate, place):
    print(f"CNP: {cnp}")
    print(f"Sex: {sex_dict[sex]}")
    print(f"Birthdate: {birthdate[4:6]}-{birthdate[2:4]}-{birthdate[0:2]}")
    print(f"Place of birth: {place_dict[place]}")

def main():
    cnp, cnp_flag = get_CNP()
    if cnp_flag == False:
        print("Bad length!")
        exit()
    elif get_sex(cnp)[1] == False:
        print("Not a valid digit for sex!")
        exit()
    elif get_birthdate(cnp)[1] == False:
        print("Not a valid birthdate!")
        exit()
    elif get_place_of_birth(cnp)[1] == False:
        print("Not a valid value for place of birth!")
        exit()
    elif validate_control(cnp)[1] == False:
        print("Not a valid control value!")
        exit()
    else:
        print("Valid CNP!")
    print_user_profile(cnp ,get_sex(cnp)[0], get_birthdate(cnp)[0], get_place_of_birth(cnp)[0])


if __name__ == "__main__":
    main()
