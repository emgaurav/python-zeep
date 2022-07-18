from zeep import Client, xsd

API_KEY_TEST = 'YOUR_OWN_API_KEY'
WSDL_TEST = 'https://apitest.trafficvance.com/?v3=system.wsdl'

client = Client(WSDL)
header = xsd.Element(
    '{WSDL_TEST}AuthenticateRequest',
    xsd.ComplexType([
        xsd.Element(
            '{WSDL_TEST}apiKey', xsd.String()
        )
    ])
)
header_value = header(apiKey=skndks)

res = client.service.getServerTime(_soapheaders=[header_value])
