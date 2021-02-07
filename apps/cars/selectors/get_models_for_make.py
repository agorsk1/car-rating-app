import requests


def get_models_for_make(car_make: str) -> dict:
    """Method that downloads data from external source about car make and models"""
    response = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{car_make}?format=json')
    return response.json()
