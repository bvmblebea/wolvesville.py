import requests

class WolvesVille:
	def __init__(
			self,
			platform: str = "android",
			locale: str = "ru") -> None:
		self.api = "https://api-game.wolvesville.com/api"
		self.core_api = "https://core.api-wolvesville.com"
		self.auth_api = "https://api-auth.wolvesville.com"
		self.headers = {
			"user-agent": "okhttp/3.12.12"}
		self.locale = locale
		self.platform = platform
		self.version_number = 4194708

	def login(self, email: str, password: str) -> dict:
		data = {
			"email": email,
			"password": password
		}
		response = requests.post(
			f"{self.auth_api}/players/signInWithEmailAndPassword",
			json=data,
			headers=self.headers).json()
		if "idToken" in response:
			self.id_token = response["idToken"]
			self.headers["authorization"] = f"Bearer {self.token}"
		return response

	def sign_up_with_email_and_password(
			self,
			email: str,
			password: str) -> dict:
		data = {
			"email": email,
			"password": password,
			"locale": self.locale
		}
		return requests.post(
			f"{self.auth_api}/players/signUpWithEmailAndPassword",
			json=data,
			headers=self.headers).json()

	def register(
			self,
			username: str,
			token: str,
			gender: str = "MALE") -> dict:
		data = {
			"username": username,
			"token": token,
			"gender": gender,
			"locale": self.locale,
			"versionNumber": self.version_number,
			"platform": self.platform
		}
		return requests.post(
			f"{self.core_api}/register",
			json=data,
			headers=self.headers).json()

	def claim_daily_reward(self) -> dict:
		return requests.post(
			f"{self.core_api}/dailyRewards",
			headers=self.headers).json()

	def change_password(self, password: str) -> dict:
		data = {
			"password": password,
			"idToken": self.id_token
		}
		return requests.post(
			f"{self.core_api}/players/changePassword",
			json=data,
			headers=self.headers).json()

	def redeem_voucher(self, code: str) -> dict:
		data = {"code": code}
		return requests.post(
			f"{self.core_api}/vouchers/redeem",
			json=data,
			headers=self.headers).json()

	def get_friend_invitation_rewards(self) -> dict:
		return requests.get(
			f"{self.core_api}/players/friendInvitationRewards",
			headers=self.headers).json()

	def get_purchases(self) -> dict:
		return requests.get(
			f"{self.core_api}/billing/purchases",
			headers=self.headers).json()

	def get_support_pins(self) -> dict:
		return requests.get(
			f"{self.core_api}/supportPins",
			headers=self.headers).json()

	def refresh_support_pins(self) -> dict:
		return requests.post(
			f"{self.core_api}/supportPins/refresh",
			headers=self.headers).json()

	def get_sent_gifts(self) -> dict:
		return requests.get(
			f"{self.core_api}/billing/gifts/sent",
			headers=self.headers).json()

	def get_received_gifts(self) -> dict:
		return requests.get(
			f"{self.core_api}/billing/gifts/received",
			headers=self.headers).json()

	def get_rotating_limited_offers(self) -> dict:
		return requests.get(
			f"{self.core_api}/billing/rotatingLimitedOffers",
			headers=self.headers).json()

	def get_pending_friend_requests(self) -> dict:
		return requests.get(
			f"{self.core_api}/friendRequests/pending",
			headers=self.headers).json()

	def get_friends_list(self) -> dict:
		return requests.get(
			f"{self.core_api}/friends",
			headers=self.headers).json()

	def get_season_and_battlepasses(self) -> dict:
		return requests.get(
			f"{self.core_api}/battlePass/seasonAndBattlePass",
			headers=self.headers).json()

	def get_daily_rewards_list(self) -> dict:
		return requests.get(
			f"{self.core_api}/dailyRewards",
			headers=self.headers).json()

	def get_wheel_items(self) -> dict:
		return requests.get(
			f"{self.core_api}/rewards/wheelItems/v2",
			headers=self.headers).json()

	def get_calendars(self) -> dict:
		return requests.get(
			f"{self.core_api}/calendars",
			headers=self.headers).json()

	def get_inventory(self) -> dict:
		return requests.get(
			f"{self.core_api}/inventory",
			headers=self.headers).json()

	def get_equipped_items(self) -> dict:
		return requests.get(
			f"{self.core_api}/equippedItems",
			headers=self.headers).json()

	def get_role_cards_abilities(self) -> dict:
		return requests.get(
			f"{self.core_api}/roleCards/abilities",
			headers=self.headers).json()

	def get_total_win_count(self) -> dict:
		return requests.get(
			f"{self.core_api}/playerRoleStats/totalWinCount",
			headers=self.headers).json()

	def get_annoucements(self, limit: int = 1) -> dict:
		return requests.get(
			f"{self.core_api}/announcements/v2?limit={limit}",
			headers=self.headers).json()

	def get_blocked_players(self) -> dict:
		return requests.get(
			f"{self.core_api}/blockedPlayers",
			headers=self.headers).json()

	def get_claimable_rewards(self) -> dict:
		return requests.get(
			f"{self.core_api}/challenges/claimAbleRewards",
			headers=self.headers).json()

	def get_clans_open_requests(self) -> dict:
		return requests.get(
			f"{self.core_api}/clans/openRequests",
			headers=self.headers).json()

	def get_inventory_hidden_item_ids(self) -> dict:
		return requests.get(
			f"{self.core_api}/inventory/hiddenItemIds",
			headers=self.headers).json()

	def get_owned_role_cards(self) -> dict:
		return requests.get(
			f"{self.core_api}/roleCards/owned",
			headers=self.headers).json()

	def get_gamemode_info(self, gamemode: str) -> dict:
		return requests.get(
			f"{self.core_api}/roleRotation/funGameMode/{gamemode}",
			headers=self.headers).json()

	def get_inventory_slot_price(self) -> dict:
		return requests.get(
			f"{self.core_api}/inventory/slotPrice",
			headers=self.headers).json()

	def check_app_cache(self) -> dict:
		return requests.get(
			f"{self.core_api}/appCache/check",
			headers=self.headers).json()

	def get_active_game_modes(self) -> dict:
		return requests.get(
			f"{self.api}/public/activeGameModes/v2",
			headers=self.headers).json()
