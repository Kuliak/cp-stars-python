"""
Simple test file to check whether CP-Stars database server can be queried.

Only subset of all functions provided by CPStars class is tested,
however, functions tend to use each other (*_by_renson especially).
"""


from cpstars import CPStars
from openapi_client.model.external_details import ExternalDetails
from openapi_client.model.identifier import Identifier
from openapi_client.model.light_curve_measurement import LightCurveMeasurement
from openapi_client.model.magnitude import Magnitude
from openapi_client.model.magnitude_attribute import MagnitudeAttribute
from openapi_client.model.radial_velocity import RadialVelocity
from openapi_client.model.spectrum_measurement import SpectrumMeasurement
from openapi_client.model.star import Star

# In case different server should be queried, host_address can be specified
# cpstars: CPStars = CPStars(host_address="http://localhost:8081")

# This is constructor for querying/requesting default server
cpstars: CPStars = CPStars()


def get_basic_info_for_stars_test():
    current_database_stars_count = 8205

    stars: list = cpstars.get_basic_info_for_stars()

    assert len(stars) == current_database_stars_count


def get_identifiers_for_star_by_renson_test():
    renson_id = '61670'
    expected_identifiers_count = 5

    identifiers: list[Identifier] = cpstars.get_identifiers_for_star_by_renson(renson_id)

    assert len(identifiers) == expected_identifiers_count


def get_light_curve_for_star_test():
    cp_stars_id: int = 76
    expected_number_of_measurements = 1092

    light_curve_measurements: list[LightCurveMeasurement] = cpstars.get_light_curve_for_star(cp_stars_id)

    assert len(light_curve_measurements) == expected_number_of_measurements


def get_light_curve_for_star_by_renson_test():
    renson_id = '61600'
    expected_number_of_measurements = 1126

    light_curve_measurements: list[LightCurveMeasurement] = cpstars.get_light_curve_for_star_by_renson(renson_id)

    assert len(light_curve_measurements) == expected_number_of_measurements


def get_magnitudes_attributes_for_star_test():
    cp_stars_id: int = 64
    expected_number_of_attributes = 1

    stellar_magnitudes_attributes: list[MagnitudeAttribute] = cpstars.get_magnitudes_attributes_for_star(cp_stars_id)

    assert len(stellar_magnitudes_attributes) == expected_number_of_attributes


def get_magnitudes_for_star_test():
    cp_stars_id: int = 2
    expected_magnitudes_count = 18

    magnitudes: list[Magnitude] = cpstars.get_magnitudes_for_star(cp_stars_id)

    assert len(magnitudes) == expected_magnitudes_count


def get_radial_velocities_for_star_test():
    cp_stars_id: int = 7
    expected_radial_velocities_measurements_count = 1

    radial_velocities: [RadialVelocity] = cpstars.get_radial_velocities_for_star(cp_stars_id)

    assert len(radial_velocities) == expected_radial_velocities_measurements_count
    assert radial_velocities[0].get('datasource').get('name') == 'Gaia DR2'


def get_simbad_external_details_test():
    """
    External data may change, thus this test may fail as well in case expected
    data will not be adjusted accordingly.
    """
    star_name: str = "Renson 61590"
    expected_effective_temperature = 7750.0
    expected_effective_temperature_unit = '[ K ]'
    expected_redshift = None

    external_details: ExternalDetails = cpstars.get_simbad_external_details(star_name)

    assert external_details.get('effective_temperature') == expected_effective_temperature
    assert external_details.get('effective_temperature_unit') == expected_effective_temperature_unit
    assert external_details.get('redshift') == expected_redshift


def get_spectrum_for_star_test():
    cp_stars_id = 1491
    expected_number_of_spectrum_measurements = 3233

    spectrum_measurements: list[SpectrumMeasurement] = cpstars.get_spectrum_for_star(cp_stars_id)

    assert len(spectrum_measurements) == expected_number_of_spectrum_measurements


def get_spectrum_for_star_by_renson_test():
    renson_id = '160'
    expected_number_of_spectrum_measurements = 3233

    spectrum_measurements: list[SpectrumMeasurement] = cpstars.get_spectrum_for_star_by_renson(renson_id)

    assert len(spectrum_measurements) == expected_number_of_spectrum_measurements


def get_star_test():
    cp_stars_id: int = 3
    expected_renson_id: str = '61600'

    star: Star = cpstars.get_star(cp_stars_id)

    assert star
    assert star.id == cp_stars_id
    assert star.get('renson') == expected_renson_id


def get_star_by_renson_test():
    renson_id: str = '61600'
    expected_cp_stars_id: int = 3

    star: Star = cpstars.get_star_by_renson(renson_id)

    assert star
    assert star.id == expected_cp_stars_id
    assert star.get('renson') == renson_id


def get_vizier_metadata_test():
    """
    External data may change, thus this test may fail as well in case expected
    data will not be adjusted accordingly.

    This test may take significant amount of time as the external service
    may experience slowness problems sometimes.
    """
    star_name: str = 'Gaia DR2 432308082052936576'
    expected_number_of_vizier_tables: int = 92

    external_details: ExternalDetails = cpstars.get_vizier_metadata(star_name)

    assert len(external_details.get('vizier_tables')) == expected_number_of_vizier_tables


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
    get_basic_info_for_stars_test()
    print("[ OK ]")

    print(str.format("   {:<40} ", "get_identifiers_for_star_by_renson"), end="")
    get_identifiers_for_star_by_renson_test()
    print("[ OK ]")

    print(str.format("   {:<40} ", "get_light_curve_for_star"), end="")
    get_light_curve_for_star_test()
    print("[ OK ]")

    print(str.format("   {:<40} ", "get_light_curve_for_star_by_renson"), end="")
    get_light_curve_for_star_by_renson_test()
    print("[ OK ]")

    print(str.format("   {:<40} ", "get_magnitudes_attributes_for_star"), end="")
    get_magnitudes_attributes_for_star_test()
    print("[ OK ]")

    print(str.format("   {:<40} ", "get_magnitudes_for_star"), end="")
    get_magnitudes_for_star_test()
    print("[ OK ]")

    print(str.format("   {:<40} ", "get_radial_velocities_for_star"), end="")
    get_radial_velocities_for_star_test()
    print("[ OK ]")

    print(str.format("   {:<40} ", "get_simbad_external_details"), end="")
    get_simbad_external_details_test()
    print("[ OK ]")

    print(str.format("   {:<40} ", "get_spectrum_for_star"), end="")
    get_spectrum_for_star_test()
    print("[ OK ]")

    print(str.format("   {:<40} ", "get_spectrum_for_star_by_renson"), end="")
    get_spectrum_for_star_by_renson_test()
    print("[ OK ]")

    print(str.format("   {:<40} ", "get_star"), end="")
    get_star_test()
    print("[ OK ]")

    print(str.format("   {:<40} ", "get_star_by_renson"), end="")
    get_star_by_renson_test()
    print("[ OK ]")

    print(str.format("   {:<40} ", "get_vizier_metadata"), end="")
    get_vizier_metadata_test()
    print("[ OK ]")
