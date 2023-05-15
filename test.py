"""
Simple test file to check whether CP-Stars database server can be queried.
"""


from cpstars import CPStars
from openapi_client.model.star import Star


cpstars: CPStars = CPStars(host_address="http://localhost:8081")


def get_stars_basic_info_test():
    current_database_stars_count = 8205

    stars: list = cpstars.get_basic_info_for_stars()

    assert len(stars) == current_database_stars_count


def get_star_test():
    cp_stars_id: int = 1
    expected_renson_id = '61593'

    star: Star = cpstars.get_star(cp_stars_id)

    assert star
    assert star.id == cp_stars_id
    assert star.get('renson') == expected_renson_id


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print()
    print("Chemically peculiar (CP) stars database library tests")
    print("=====================================================")
    print("\n")

    print("+---------------------------------------------------+")
    print("|  FUNCTION                                         |")
    print("+---------------------------------------------------+")

    print(str.format("   {:<40} ", "get_basic_info_for_stars"), end="")
    get_stars_basic_info_test()
    print("[ OK ]")

    print(str.format("   {:<40} ", "get_star"), end="")
    get_star_test()
    print("[ OK ]")
