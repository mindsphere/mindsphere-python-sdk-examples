from timeseries.models import RetrieveTimeseriesRequest


def get_timeseries_data(entity_id, property_name, _from, to):
    request_data = RetrieveTimeseriesRequest(entity=entity_id, propertysetname=property_name, _from=_from, to=to)
    return request_data