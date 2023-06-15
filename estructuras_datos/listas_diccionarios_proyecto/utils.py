import csv
from pprint import pprint
from unicodedata import normalize
from colorama import Fore, Style


def csv_to_dict():
    with open("data.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return list(csv_reader)


DICT_CSV = csv_to_dict()


def clean_string(sentence):
    normal_str = normalize("NFKD", sentence)
    clean_str = normal_str.encode("ASCII", "ignore").decode("ASCII")
    return clean_str.casefold()


def get_all_students_by_city():
    city_input = input(
        f"{Fore.BLUE}Ingrese la ciudad para su consulta: {Style.RESET_ALL}"
    )

    return [
        dict for dict in DICT_CSV if city_input.lower() == clean_string(dict["ciudad"])
    ]


def get_all_students_by_country():
    country_input = input(
        f"{Fore.BLUE}Ingrese el pais para su consulta: {Style.RESET_ALL}"
    )

    return [
        dict for dict in DICT_CSV if country_input.lower() == clean_string(dict["pais"])
    ]


def get_all_students_by_age():
    range_age_input = input(
        f"{Fore.BLUE}Ingrese el rango de edad para su consuta (edad-edad): {Style.RESET_ALL}"
    ).split("-")

    return [
        dict
        for dict in DICT_CSV
        if range_age_input[0] <= dict["edad"] <= range_age_input[1]
    ]


def get_all_hometowns():
    cities_of_students = []
    for dict in DICT_CSV:
        if dict["ciudad"] not in cities_of_students:
            cities_of_students.append(dict["ciudad"])

    return cities_of_students


def get_careers():
    careers_of_student = []
    for dict in DICT_CSV:
        if dict["carrera"] not in careers_of_student:
            careers_of_student.append(dict["carrera"])
    return careers_of_student


def get_average_age_by_career():
    careers = get_careers()
    averages_age = {}
    for career in careers:
        count_std, sum_age = (0, 0)
        for dict in DICT_CSV:
            if career == dict["carrera"]:
                sum_age += int(dict["edad"])
                count_std += 1
        averages_age[career] = int(sum_age / count_std)

    return averages_age


def get_average_status_student_by_career():
    averages_by_career = get_average_age_by_career()
    age_input = int(
        input(f"{Fore.BLUE}Ingrese la edad del estudiante: {Style.RESET_ALL}")
    )
    career_input = input(
        f"{Fore.BLUE}Ingrese la carrera del estudiante: {Style.RESET_ALL}"
    )

    print(
        f"{Fore.GREEN}Esta encima del promedio{Style.RESET_ALL}"
        if age_input > averages_by_career[career_input]
        else f"{Fore.RED}Esta debajo del promedio{Style.RESET_ALL}"
    )
    return


def get_group_students_with_ranges_age():
    options_range = {
        "1": [dict for dict in DICT_CSV if 18 <= int(dict["edad"]) <= 25],
        "2": [dict for dict in DICT_CSV if 26 <= int(dict["edad"]) <= 35],
        "3": [dict for dict in DICT_CSV if int(dict["edad"]) > 35],
    }
    return options_range[
        input(
            f"{Fore.BLUE}Ingrese alguna de las opciones: \n 1) 18-25\n 2) 26-35\n 3) Mayores a 35\n {Style.RESET_ALL}"
        )
    ]


def get_the_most_city_with_careers():
    city_result = (None, 0)
    cities = get_all_hometowns()
    for city in cities:
        careers_by_city = []
        for dict in DICT_CSV:
            if dict["ciudad"] == city:
                if dict["carrera"] not in careers_by_city:
                    careers_by_city.append(dict["carrera"])
        if len(careers_by_city) >= city_result[1]:
            city_result = (city, len(careers_by_city))

    return city_result
