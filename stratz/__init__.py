import requests

from .urls import *
from .errors import ERROR_NOT_FOUND


class Api():
    def __init__(self, token, lang) -> None:
        self.executor = requests.Session()
        self.headers = {
                'Authorization': f'Bearer {token}'
        }
        self.lang = lang

    def all_heroes(self) -> dict:
        return self.executor.request(
            method="GET",
            url=HERO_URL,
            headers = self.headers,
            params={"languageId": self.lang}
        ).json()

    def get_hero_by_name(self, name: str) -> dict:
        heroes = self.all_heroes()

        for hero in heroes:
            if name in heroes[hero]["name"]:
                return heroes[hero]
        else:
            raise ERROR_NOT_FOUND

    def get_hero_by_id(self, id: int) -> dict:
        heroes = self.all_heroes()

        try:
            return heroes[str(id)]
        except:
            raise ERROR_NOT_FOUND

    def all_items(self) -> dict:
        return self.executor.request(
            method="GET",
            url=ITEM_URL,
            headers=self.headers,
            params={"languageId": self.lang}
        ).json()

    def get_item_by_id(self, id: int) -> dict:
        try:
            return self.executor.request(
                method="GET",
                url=ITEM_URL+f"/{id}",
                headers=self.headers,
                params={"languageId": self.lang}
            ).json()
        except:
            raise ERROR_NOT_FOUND

    def get_match(self, id: int) -> dict:
        try:
            return self.executor.request(
                method="GET",
                url=MATCH_URL+f"/{id}",
                headers=self.headers,
                params={"languageId": self.lang}
            ).json()
        except:
            raise ERROR_NOT_FOUND

    def get_live_match(self, id: int) -> dict:
        return self.executor.request(
            method="GET",
            url=MATCH_URL+f"/{id}/live",
            headers=self.headers,
            params={"languageId": self.lang}
        ).json()

    def get_player(self, id: int) -> dict:
        try:
            return self.executor.request(
                method="GET",
                url=PLAYER_URL+f"/{id}",
                headers=self.headers,
                params={"languageId": self.lang}
            ).json()
        except:
            raise ERROR_NOT_FOUND

    def get_player_matches(self, id: int) -> dict:
        try:
            return self.executor.request(
                method="GET",
                url=PLAYER_URL+f"/{id}/matches",
                headers=self.headers,
                params={"languageId": self.lang}
            ).json()
        except:
            raise ERROR_NOT_FOUND

    def get_item_by_name(self, name: str) -> dict:
        items = self.all_items()

        for item in items:
            if name in items[item]["name"]:
                return items[item]
        else:
            raise ERROR_NOT_FOUND

    def all_langs(self):
        return self.executor.request(
            method="GET",
            url=LANG_URL,
            headers=self.headers,
            params={"languageId": self.lang}
        ).json()

    def game_version(self) -> dict:
        return self.executor.request(
            method="GET",
            url=GAME_VERSION_URL,
            headers=self.headers,
            params={"languageId": self.lang}
        ).json()

    def current_game_version(self) -> list:
        versions = self.game_version()

        return versions[0]
