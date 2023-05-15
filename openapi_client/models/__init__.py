# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.attribute_definition import AttributeDefinition
from openapi_client.model.data_source import DataSource
from openapi_client.model.data_source_basic_info import DataSourceBasicInfo
from openapi_client.model.export_csv_form import ExportCsvForm
from openapi_client.model.extended_star import ExtendedStar
from openapi_client.model.external_details import ExternalDetails
from openapi_client.model.identifier import Identifier
from openapi_client.model.light_curve_measurement import LightCurveMeasurement
from openapi_client.model.magnitude import Magnitude
from openapi_client.model.motion import Motion
from openapi_client.model.radial_velocity import RadialVelocity
from openapi_client.model.spectrum_measurement import SpectrumMeasurement
from openapi_client.model.star import Star
from openapi_client.model.star_basic_info import StarBasicInfo
from openapi_client.model.star_datasource_attribute import StarDatasourceAttribute
from openapi_client.model.vizier_table import VizierTable
