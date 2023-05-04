# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from cpstars import CPStars
from openapi_client.model.star import Star
import requests


def test_request():
    response = requests.request(
        method='GET',
        url="http://localhost:8081/stars"
    )

    print("Obtained response:")
    print("------------------")
    print("Status:", response.status_code)
    print("Content:")
    print(response.content)

    print("\n\n\n")
    print("Text:")
    print(response.text)

    print("\n\n\n")
    print("JSON:")
    print(response.json())


def get_stars_basic_info_test():
    cpstars: CPStars = CPStars()
    stars: list = cpstars.get_basic_info_for_stars()

    print('List:')
    print(len(stars))


def get_star_test():
    cp_stars_id: int = 1

    cpstars: CPStars = CPStars()
    star: Star = cpstars.get_star(cp_stars_id)

    print('Response:')
    print(star)

    assert star
    assert star.id == cp_stars_id


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test_request()
    get_stars_basic_info_test()
    # get_star_test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
