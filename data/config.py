# api id, hash
API_ID = xxxx
API_HASH = 'xxxxxxxxxxxx'

REF_LINK = "https://t.me/xkucoinbot/kucoinminiapp?startapp=cm91dGU9JTJGdGFwLWdhbWUlM0ZpbnZpdGVyVXNlcklkJTNENTkwMzI4MjA4MSUyNnJjb2RlJTNE"

DELAYS = {
    'ACCOUNT': [5, 15],  # độ trễ giữa các kết nối với tài khoản (càng nhiều tài khoản, độ trễ càng lâu)
}

PROXY = {
    "USE_PROXY_FROM_FILE": False,  # True - if use proxy from file, False - if use proxy from accounts.json
    "PROXY_PATH": "data/proxy.txt",  # path to file proxy
    "TYPE": {
        "TG": "socks5",  # proxy type for tg client. "socks4", "socks5" and "http" are supported
        "REQUESTS": "socks5"  # proxy type for requests. "http" for https and http proxys, "socks5" for socks5 proxy.
        }
}
# thư mục phiên (không thay đổi)
WORKDIR = "sessions/"

# thời gian chờ tính bằng giây để kiểm tra tài khoản hợp lệ
TIMEOUT = 30

