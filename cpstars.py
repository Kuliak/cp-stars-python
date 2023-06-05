"""
|    Python library for querying CP-Stars Database Application.
|
|    Chemically peculiar (CP) stars are stored in the database based on the catalog of Ap, HgMn and Am stars
|    (Bibcode: 2009A&A...498..961R).
|
|    Several types of data can be obtained:
|        -> General (CP-Stars ID, Renson ID, binary system component flag, ICRS coordinates, galactic coordinates
            alpha/delta coordinates, considered category affiliation probability)
|        -> Magnitudes (band, value, error, quality)
|        -> Motion-related values (ICRS proper motion + errors, parallax + error)
|        -> Radial velocities (value, error)
|        -> Identifiers (stored in the CP-Stars database)
|        -> Attributes (e.g. Spectral type)
|        -> Vizier metadata, external details
|
|    AUTHOR: Ľuboslav Halama
|
|    This library is a part of Master's thesis developed for Department of Theoretical Physics and Astrophysics,
     Physics Section, Faculty of Science, Masaryk University, Brno.
|
|    REQUIREMENTS:
|        - Python >= 3.x
|        - requests
|        - python_dateutil >= 2.5.3
|        - setuptools >= 21.0.0
|        - urllib3 >= 1.25.3
|
|    USAGE:
|        1.) Instance of the CPStars class has to be created
|        2.) Functions of the created instance can be used to obtain data from remote server
|        3-a.) After valid response is obtained, corresponding object or list of objects is
               returned. In order to access object's properties, .get(...) method has to be
               used with property name (string).
|              Property names can be found in openapi_client/model folder or by simply printing
               the obtained object using print(...) function.
|        3-b.) In case some problem occurred, error (exception) is raised so user may decide
               how he wants to react to it.
|
|       Example 1:
|           Provided example uses default CP-Stars Database Address to obtain magnitudes of star
            with Renson identifier equal to '710':
|
|           -------------------------------------------------------------------------------------------------
|              cpstars_instance = CPStars()
|              magnitudes = cpstars_instance.get_magnitudes_for_star_by_renson('710')
|           -------------------------------------------------------------------------------------------------
|
|       Example 2:
|           Provided example uses default CP-Stars Database Address to obtain star object
            with CP-Stars database identifier equal to 1.
|           In order to obtain specific attribute (except ID), its name has to be used
            in .get(...) method. In this case, we print Renson identifier by using 'renson':
|
|           -------------------------------------------------------------------------------------------------
|              cpstars_instance = CPStars()
|              star: Star = cpstars_instance.get_star(1)
|              print(star.get('renson'))
|           -------------------------------------------------------------------------------------------------
|
|       Some other examples can also be found in test.py file.
"""

from openapi_client import ApiClient, Configuration

from openapi_client.api.export_controller_api import ExportControllerApi
from openapi_client.api.external_services_controller_api import ExternalServicesControllerApi
from openapi_client.api.stars_controller_api import StarsControllerApi

from openapi_client.model.external_details import ExternalDetails
from openapi_client.model.identifier import Identifier
from openapi_client.model.light_curve_measurement import LightCurveMeasurement
from openapi_client.model.magnitude import Magnitude
from openapi_client.model.magnitude_attribute import MagnitudeAttribute
from openapi_client.model.motion import Motion
from openapi_client.model.radial_velocity import RadialVelocity
from openapi_client.model.spectrum_measurement import SpectrumMeasurement
from openapi_client.model.star import Star
from openapi_client.model.star_basic_info import StarBasicInfo
from openapi_client.model.star_datasource_attribute import StarDatasourceAttribute


class CPStars:
    """
    Class used for querying CP-Stars Database (backend).

    If no specific configuration is provided, default configuration is used.
    """

    def __init__(self, host_address=None):
        """
        CPStars class constructor.
        Default configuration may be overridden in case different backend should be queried.

        :param host_address: CP-Stars database backend (server) address
        """
        self.api_client = ApiClient(
            Configuration(host_address)
        )
        self.stars_controller = StarsControllerApi(self.api_client)
        self.export_controller = ExportControllerApi(self.api_client)
        self.external_services_controller = ExternalServicesControllerApi(self.api_client)

    def get_basic_info_for_stars(self) -> list[StarBasicInfo]:
        """
        Obtain list of all stars from the database containing basic information:
            - Renson ID (id_2009_A_AND_A_498_961_R)
            - probability flag for affiliation with considered category (consideredCategoryAffiliationProbabilityFlag)
            - binary component information (binarySystemComponent)
            - coordinates
                - ICRS Right Ascension (icrsRightAscension) and Declination (icrsDeclination)
                - galactic longitude (galacticLongitude) and latitude (galacticLatitude)

        :return: list of stars in the database with basic information
        """
        return self.stars_controller.get_basic_info_stars_list()

    def get_identifiers_for_star(self, cp_stars_id: int) -> list[Identifier]:
        """
        Obtain identifiers that are stored in the database for the given star
        specified by CP-Stars database identifier.

        :param cp_stars_id: CP-Stars database identifier
        :return: list of identifiers of the given star
        """
        return self.stars_controller.get_star_identifiers(cp_stars_id)

    def get_identifiers_for_star_by_renson(self, renson_id: str) -> list[Identifier]:
        """
        Obtain identifiers that are stored in the database for the given star
        specified by Renson identifier.

        :param renson_id: Renson identifier
        :return: list of identifiers of the given star
        """
        star: Star = self.stars_controller.get_star_by_renson_id(renson_id)
        return self.stars_controller.get_star_identifiers(star.id)

    def get_simbad_external_details(self, star_name: str) -> ExternalDetails:
        """
        Obtain specific subset of information from SIMBAD database.
        Stellar name has to be specified including data source identification, e.g. 'Renson 61590'.

        :param star_name: star name that will be used for querying external services
        :return: external details object with SIMBAD details (subset) filled only
        """
        return self.external_services_controller.get_simbad_external_details(star_name)

    def get_star_attributes(self, cp_stars_id: int) -> list[StarDatasourceAttribute]:
        """
        Obtain list of attributes belonging to the specified star.
        CP-Stars database identifier is used to find corresponding attributes.

        Each attribute has also corresponding datasource specified it was
        obtained from.

        :param cp_stars_id: CP-Stars database identifier
        :return: list of attributes of given star
        """
        return self.stars_controller.get_star_datasource_attributes(cp_stars_id)

    def get_star_attributes_by_renson(self, renson_id: str) -> list[StarDatasourceAttribute]:
        """
        Obtain list of attributes belonging to the specified star.
        Renson identifier is used to find corresponding attributes.

        Each attribute has also corresponding datasource specified it was
        obtained from.

        :param renson_id: Renson identifier
        :return: list of attributes of given star
        """
        star: Star = self.stars_controller.get_star_by_renson_id(renson_id)
        return self.stars_controller.get_star_datasource_attributes(star.id)

    def get_star(self, cp_stars_id: int) -> Star:
        """
        Get star information using CP-Stars database identifier.
        Besides basic information, other information is included:
            - ICRS coordinates errors
            - Alpha and Delta coordinates

        :param cp_stars_id: CP-Stars identifier
        :return: star information
        """
        return self.stars_controller.get_star(cp_stars_id)

    def get_star_by_renson(self, renson_id: str) -> Star:
        """
        Get star information using Renson identifier.
        Besides basic information, other information is included:
            - ICRS coordinates errors
            - Alpha and Delta coordinates

        :param renson_id: Renson identifier
        :return: star information
        """
        return self.stars_controller.get_star_by_renson_id(renson_id)

    def get_magnitudes_attributes_for_star(self, cp_stars_id: int) -> list[MagnitudeAttribute]:
        """
        Obtain list of stellar magnitudes attributes of the given star
        specified by CP-Stars database identifier

        :param cp_stars_id: CP-Stars database identifier
        :return: list of stellar magnitudes attributes
        """
        return self.stars_controller.get_star_magnitude_attributes(cp_stars_id)

    def get_magnitudes_attributes_for_star_by_renson(self, renson_id: str) -> list[MagnitudeAttribute]:
        """
        Obtain list of stellar magnitudes attributes of the given star
        specified by Renson identifier

        :param renson_id: Renson identifier
        :return: list of stellar magnitudes attributes
        """
        star: Star = self.stars_controller.get_star_by_renson_id(renson_id)
        return self.stars_controller.get_star_magnitude_attributes(star.id)

    def get_magnitudes_for_star(self, cp_stars_id: int) -> [Magnitude]:
        """
        Obtain list of magnitudes corresponding to the given star
        specified by CP-Stars database identifier.

        :param cp_stars_id: Cp-Stars identifier
        :return: list of star magnitudes
        """
        return self.stars_controller.get_star_magnitudes(cp_stars_id)

    def get_magnitudes_for_star_by_renson(self, renson_id: str) -> [Magnitude]:
        """
        Obtain list of magnitudes corresponding to the given star
        specified by Renson identifier.

        :param renson_id: Renson identifier
        :return: list of star magnitudes
        """
        star: Star = self.stars_controller.get_star_by_renson_id(renson_id)
        return self.stars_controller.get_star_magnitudes(star.id)

    def get_motion_related_info_for_star(self, cp_stars_id: int) -> list[Motion]:
        """
        Obtain motion-related information for the given star
        specified by CP-Stars database identifier:
             - parallaxes with corresponding errors
             - proper motion Right Ascension and Declination, with corresponding error values

        :param cp_stars_id: CP-Stars identifier
        :return: list of motion-related values for given star
        """
        return self.stars_controller.get_star_motions(cp_stars_id)

    def get_motion_related_info_for_star_by_renson(self, renson_id: str) -> list[Motion]:
        """
        Obtain motion-related information for the given star
        specified by Renson identifier:
             - parallaxes with corresponding errors
             - proper motion Right Ascension and Declination, with corresponding error values

        :param renson_id: Renson identifier
        :return: list of motion-related values for given star
        """
        star: Star = self.stars_controller.get_star_by_renson_id(renson_id)
        return self.stars_controller.get_star_motions(star.id)

    def get_radial_velocities_for_star(self, cp_stars_id: int) -> list[RadialVelocity]:
        """
        Obtain radial velocities with corresponding errors for the given star
        specified by CP-Stars database identifier.

        :param cp_stars_id: CP-Stars identifier
        :return: list of radial velocities of the given star
        """
        return self.stars_controller.get_star_radial_velocities(cp_stars_id)

    def get_radial_velocities_for_star_by_renson(self, renson_id: str) -> [RadialVelocity]:
        """
        Obtain radial velocities with corresponding errors for the given star
        specified by Renson identifier.

        :param renson_id: Renson identifier
        :return: list of radial velocities of the given star
        """
        star: Star = self.stars_controller.get_star_by_renson_id(renson_id)
        return self.stars_controller.get_star_radial_velocities(star.id)

    def get_light_curve_for_star(self, cp_stars_id: int) -> list[LightCurveMeasurement]:
        """
        Obtain stellar light curve measurements for the given star
        specified by CP-Stars database identifier.

        :param cp_stars_id: CP-Stars database identifier
        :return: stellar light curve measurements
        """
        return self.stars_controller.get_star_light_curve_measurements(cp_stars_id)

    def get_light_curve_for_star_by_renson(self, renson_id: str) -> list[LightCurveMeasurement]:
        """
        Obtain stellar light curve measurements for the given star
        specified by Renson identifier.

        :param renson_id: Renson identifier
        :return: stellar light curve measurements
        """
        return self.stars_controller.get_star_light_curve_measurements_by_renson(renson_id)

    def get_spectrum_for_star(self, cp_stars_id: int) -> list[SpectrumMeasurement]:
        """
        Obtain stellar spectrum measurements for the given star
        specified by CP-Stars database identifier.

        :param cp_stars_id: CP-Stars database identifier
        :return: stellar spectrum measurements
        """
        return self.stars_controller.get_star_spectra_measurements(cp_stars_id)

    def get_spectrum_for_star_by_renson(self, renson_id: str) -> list[SpectrumMeasurement]:
        """
        Obtain stellar spectrum measurements for the given star
        specified by Renson identifier.

        :param renson_id: Renson identifier
        :return: stellar spectrum measurements
        """
        return self.stars_controller.get_star_spectra_measurements_by_renson(renson_id)

    def get_vizier_metadata(self, star_name: str) -> ExternalDetails:
        """
        Obtain Vizier database metadata containing tables the given star is present in.
        Stellar name has to be specified including data source identification, e.g. 'Renson 61593'.

        :param star_name: star name that will be used for querying external services
        :return: external details object with Vizier metadata (tables) filled only
        """
        return self.external_services_controller.get_vizier_metadata(star_name)

