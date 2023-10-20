from pycep.services.opencep import OpenCepService
from tests.helpers.fake_http_client import FakeHttpClient

expected_get_output = {
    "cep": "72120-020",
    "logradouro": "Quadra QND 2",
    "complemento": "",
    "bairro": "Taguatinga Norte (Taguatinga)",
    "localidade": "Brasília",
    "uf": "DF",
    "ibge": "5300108",
}


async def test_querycep_returns_expected_value() -> None:
    http_client = FakeHttpClient(get_output=expected_get_output)
    sut = OpenCepService(http_client=http_client)
    output = await sut.query_cep("72120020")
    assert http_client.get_is_called
    assert output == expected_get_output
