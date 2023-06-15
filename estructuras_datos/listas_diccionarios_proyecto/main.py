from colorama import Fore, Style
from pprint import pprint
import utils

options = {
    "1": (
        "Obtener todos los estudiantes que pertenezcan a una ciudad",
        utils.get_all_students_by_city,
    ),
    "2": (
        "Obtener todos los estudiantes que vivan en un país dado",
        utils.get_all_students_by_country,
    ),
    "3": (
        "Obtener todos los estudiantes que estén dentro del rango de edades dado",
        utils.get_all_students_by_age,
    ),
    "4": (
        "Obtener todas las ciudades de residencia de los estudiantes",
        utils.get_all_hometowns,
    ),
    "5": (
        "Identificar la edad promedio por carrera",
        utils.get_average_age_by_career,
    ),
    "6": (
        "Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad",
        utils.get_average_status_student_by_career,
    ),
    "7": (
        "Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35)",
        utils.get_group_students_with_ranges_age,
    ),
    "8": (
        "Identifica la ciudad que tienen la mayor variedad de carreras universitarias entre los estudiantes",
        utils.get_the_most_city_with_careers,
    ),
    "9": ("Salida", exit),
}


def show_menu(options):
    print(f"{Fore.BLUE}Selecciona una opcion: {Style.RESET_ALL}")
    for key in sorted(options):
        print(f"{Fore.BLUE}{key}){Style.RESET_ALL} {options[key][0]}")


def execute_option(options, option):
    result = options[option][1]()
    if result is None:
        return
    pprint(result)


def read_option(options):
    while (
        option := input(
            f"{Fore.BLUE}Seleccione alguna de las opciones: {Style.RESET_ALL}"
        )
    ) not in options:
        print(f"{Fore.RED}Opcion Incorrecta, vuelve a intentarlo{Style.RESET_ALL}")
    return option


def generate_menu(options, exit):
    option = None
    while option != exit:
        show_menu(options)
        option = read_option(options)
        execute_option(options, option)
        print()


def exit():
    print(f"{Fore.YELLOW}Saliendo...")


if __name__ == "__main__":
    generate_menu(options, "9")
