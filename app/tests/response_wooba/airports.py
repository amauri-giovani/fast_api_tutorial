from pydantic import BaseModel


class Airport(BaseModel):
    airport_iata_code: str | None = None
    airport_name: str | None = None
    airport_slug: str | None = None
    region_name: str | None = None
    region_slug: str | None = None
    city_iata_code: str | None = None
    city_name: str | None = None
    city_slug: str | None = None
    state_code: str | None = None
    state_name: str | None = None
    state_slug: str | None = None
    country_name: str | None = None
    country_slug: str | None = None
    country_code: str | None = None


airports = {
'GKA': Airport(
    airport_iata_code='GKA',
    airport_name='Goroka Airport',
    airport_slug='goroka-airport',
    region_name='Goroka',
    region_slug='goroka',
    city_iata_code=None,
    city_name='',
    city_slug='',
    state_code='Eastern Highlands Province',
    state_name='Eastern Highlands Province',
    state_slug='eastern-highlands-province',
    country_name='Papua-Nova Guiné',
    country_slug='papua-nova-guine',
    country_code='PG'
               ),