def bls_api_req(
    regkey: str,
    series_id: str | list[str],
    start_year: str | int,
    end_year: str | int,
    catalog: bool = False,
    calculations: bool = False,
    annual_average: bool = False,
    aspects: bool = False,
):
    URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
    regkey = open(regkey).read()

    # Validates for empty str or list, then list with empty str
    while (not series_id) or (series_id == [""]):
        series_id = input("please input a valid Series ID or IDs, sep with commas")
        series_id = series_id.split(sep=",")

    if isinstance(series_id, str):
        series_id = [series_id]

    data = {
        "seriesid": series_id,
        "startyear": start_year,
        "endyear": end_year,
        "catalog": catalog,
        "calculations": calculations,
        "annualaverage": annual_average,
        "aspects": aspects,
    }

    for k, v in data.items():
        if v == "":
            del data[k]


def main():
    pass


if __name__ == "__main__":
    main()

    # todo: add validator for start/end year param (max -20 years from today)
    # add converter for int start/end year params
    # maybe remove str option from start/end year params?
    # test BLS api for invalide api error, add handler?
    # source series from BLS and start graphing, move bls_api_req to new module?
