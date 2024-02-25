TXT = """
LONG_VISITOR=bd5c4f7f-52b4-42db-aa08-0762fd16147d; device.info.cookie={"bv":"118.0.0.0","bn":"Chrome","osv":"x86_64","osn":"Linux","tbl":"false","vnd":"false","mdl":"false"}; ga24x7_jsessionid="SSID3271c084-b13d-4fe1-9d6c-eea781abc7f2:null"; ga24x7_pixeltracker=from_page%3Dindex.html%26referrer_url%3D; __utma=3588915.416701776.1701682271.1701682271.1701682271.1; __utmc=3588915; __utmz=3588915.1701682271.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); NA_IDVISIT=761bbb5a-fecc-469d-b136-446cc7e2bc6e; NA_VISITOR=761bbb5a-fecc-469d-b136-446cc7e2bc6e; AWSALB=Ws6ly2kyQTHqvqw0QxUdU7LeAyfSKeVIZe7q09MngvJU2aU+52BEBYc+KTZ1uOwzyEXNmnczJp9QWnBdT12XX9Mwcd4Nx7uJgeUzdnETfc62yOlkUUKnHNcG8GiQ; AWSALBCORS=Ws6ly2kyQTHqvqw0QxUdU7LeAyfSKeVIZe7q09MngvJU2aU+52BEBYc+KTZ1uOwzyEXNmnczJp9QWnBdT12XX9Mwcd4Nx7uJgeUzdnETfc62yOlkUUKnHNcG8GiQ
""" 
for _ in TXT.split(";"):
    print(f'"{_.split("=")[0].strip(" ").strip("\n")}":"{_.split("=")[1]}",')
