import requests

headers = {
    'origin': 'https://www.youtube.com',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'x-youtube-page-label': 'youtube.ytfe.desktop_20180206_0_RC1',
    'x-chrome-uma-enabled': '1',
    'x-youtube-page-cl': '184733661',
    'x-spf-referer': 'https://www.youtube.com/watch?v=J5DLWBPDRVk',
    'x-spf-previous': 'https://www.youtube.com/watch?v=J5DLWBPDRVk',
    'cookie': 'YSC=fvIBtSQ9HQQ; __utmc=27069237; wide=1; live_highlight_clip_creation=true; VISITOR_INFO1_LIVE=T5tI-dPCPbg; CONSENT=YES+DE.en+V7; LOGIN_INFO=AFmmF2swRAIgBZflKX4mENzIdmXFmU1olXQ1PmS2hCCNmE0CGy24ZIUCIBsOOBwmIF0vD0nTDTm43uz3EQITb44FJJ10TXFGRc_9:QUQ3MjNmd1BqZXRQcG5KQ3pyeWlIOFh5OTItbU1zNVVrYlVPSFdrOE9iZUpkOXVVVy1idTVxRmxfdVpKaUxKaHhDZ3haSnp1M21Kb3g5WktLSWVjTVhfbXdVQzUxcDg2OEpydFQwOUU0bHBEQUl4OVg5aUdCeFEyaVpveEZ4ZWVtQzQzcmN1MlNlUGpPUjFIbHNsMGhMdVJqVUROeFRSSTJKQnV4Zkd1UUVsdERJLXBoNmRoem9yeVQzTDR4djJfWlBJRDFaOEs0SnhkNW04MVVmY2ZhLUlfWnQ5MG9ObktUc3FJc1A4c0R4LTRSRnNOdkNYclhNZw==; _ga=GA1.2.673133424.1516303512; SID=uAV5pF6R95HtcktyxlMkePjAylz4Yosz6vIonfj5PZELPpNAcRB5j4g3VlzAGwkZIqos2g.; HSID=Aw_OdISDXRiPXaC1X; SSID=AeV9QvkgL7USklMAl; APISID=hwrFJ489ZtYtSEHe/A45sRKF7f0pMEWgbe; SAPISID=eNgM0Zh3kDwjQRFZ/Aa_cjFjUcvEu_hTDL; llbcs=22; PREF=cvdm=grid&ems=default&f1=50000004&f2=1000&f3=8&f4=5000000&f5=36230&fv=16.0.0&al=en&f6=80000',
    'x-client-data': 'CIS2yQEIprbJAQjEtskBCPqcygEIqZ3KAQioo8oB',
    'pragma': 'no-cache',
    'x-youtube-client-version': '2.20180201',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'x-youtube-variants-checksum': 'a46bceb38b3bb2a8f33c4d2a7dddb55e',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'x-youtube-client-name': '1',
    'authority': 'www.youtube.com',
    'referer': 'https://www.youtube.com/watch?v=J5DLWBPDRVk',
    'x-youtube-identity-token': 'QUFFLUhqa0x5TzU1V1l5QWl1ZzNPSFhJWllJaVVaLXpZZ3w=',
    'dnt': '1',
}

params = (
    ('action_get_comments', '1'),
    ('pbj', '1'),
    ('ctoken', 'EiYSC0o1RExXQlBEUlZrwAEAyAEA4AEDogINKP___________wFAABgGMoIFCuwEQURTSl9pMkExQk9OeU1MeUwwUUdDTGtGZEp0LVBERjZmUmdCQnVMWlY0SV9nOGdkaTR5dXZhRG56M2NMRkVxQ1AtbGRXY2FkR1hpNjZ4NUVVcTE0ZzZxRHpFQ0xxN2xzaEFUblhBMWJieFhXM053dE1ZdXdJY1k4eVVsenQwQnNBcU11cWx2QWM0ZGhSN1JFMW9OTVRodDhQVjhZMmR1b192ZUR1eXRKZkRyYUhrT3FuY0xiZ0ZJN3d4bmsxUi1fMTFfMW9XM0k2RlBxTHpvaHQ4M3JjellvYnVSRzlRM3J3WmpLN0diemZicEozUkdEU3JGRkx1X2lSWlZzcWVfb05jZk9iTm10LUJEX3NlY1NBN3lubGtsQm4yYU8xV1JzTV9OQjZNVU1SSmVSVEVSSHpoZXFsWEhOYWdHV3VoR3N2SlRkeXRDM3BMcVkwamxqTTJWdHBQVFl6djk3QnZYYzA4ejZ2eVFtTHZFSWJ3bDNFS0NnbWliOVBacndHX1c3M0xlZVZYRXBONDVzamFsZXNBWFg5bzNzOU5Sam5ESXJrakVWajJjc3NWTDhVNjRjcU4tMnNXaXRXbDNNbFFVaGhDMTJJdHF3RS1DMXBuQXpNeG5UN2RqMXRibktFTDZfbkI1bEo4SUJ1amdWeUhDN3JpYXlHR1lnOGVCa05TMWpLNUtpckxlMWZoZEdWYmt0N0ZuMzJkUUxldm9lLWVzZy1xdkxKQ1BoNllaRzdvM3JKTHhKUTFIWTlZWV81VVZXTS1fdXBHSFE1bXZ0SW9wMnd3RTRYUjN4bEdtXzVBbFpZT0IyMXNJdUc0UDEiDyILSjVETFdCUERSVmswACgo'),
    ('continuation', 'EiYSC0o1RExXQlBEUlZrwAEAyAEA4AEDogINKP___________wFAABgGMoIFCuwEQURTSl9pMkExQk9OeU1MeUwwUUdDTGtGZEp0LVBERjZmUmdCQnVMWlY0SV9nOGdkaTR5dXZhRG56M2NMRkVxQ1AtbGRXY2FkR1hpNjZ4NUVVcTE0ZzZxRHpFQ0xxN2xzaEFUblhBMWJieFhXM053dE1ZdXdJY1k4eVVsenQwQnNBcU11cWx2QWM0ZGhSN1JFMW9OTVRodDhQVjhZMmR1b192ZUR1eXRKZkRyYUhrT3FuY0xiZ0ZJN3d4bmsxUi1fMTFfMW9XM0k2RlBxTHpvaHQ4M3JjellvYnVSRzlRM3J3WmpLN0diemZicEozUkdEU3JGRkx1X2lSWlZzcWVfb05jZk9iTm10LUJEX3NlY1NBN3lubGtsQm4yYU8xV1JzTV9OQjZNVU1SSmVSVEVSSHpoZXFsWEhOYWdHV3VoR3N2SlRkeXRDM3BMcVkwamxqTTJWdHBQVFl6djk3QnZYYzA4ejZ2eVFtTHZFSWJ3bDNFS0NnbWliOVBacndHX1c3M0xlZVZYRXBONDVzamFsZXNBWFg5bzNzOU5Sam5ESXJrakVWajJjc3NWTDhVNjRjcU4tMnNXaXRXbDNNbFFVaGhDMTJJdHF3RS1DMXBuQXpNeG5UN2RqMXRibktFTDZfbkI1bEo4SUJ1amdWeUhDN3JpYXlHR1lnOGVCa05TMWpLNUtpckxlMWZoZEdWYmt0N0ZuMzJkUUxldm9lLWVzZy1xdkxKQ1BoNllaRzdvM3JKTHhKUTFIWTlZWV81VVZXTS1fdXBHSFE1bXZ0SW9wMnd3RTRYUjN4bEdtXzVBbFpZT0IyMXNJdUc0UDEiDyILSjVETFdCUERSVmswACgo'),
    ('itct', 'CAEQuy8iEwi66uXd5JTZAhWQnsEKHbkvAl8='),
)

data = [
  ('session_token', 'QUFFLUhqbDl6bmxaQV9nNTNNTXo1Mm9LaHlTYnVLWnRwZ3xBQ3Jtc0ttRzhYTWZtaF9HQW1naFdzUTFFakUwdDFNbFgwakJMVi10ekp5WHpqeV9oNDdFNDRWMUNFMGJza0lNMWhLbmgtdEhPZkxCVzN2SGplNW5QendVLUw1MjEyb0x6XzZYZllGUzNHbGxCWG0tbWFuRDBpSTJNMk84dDM4MWtHanpsbUh5VVVSZDZvWWFTelRoakhLVFhJWmtuTlFjeDluQ201X01HVWExR05YQVZyUWtOaFU='),
]

response = requests.post('https://www.youtube.com/comment_service_ajax', headers=headers, params=params, data=data).json()
# print(response.text)
comments = response['response']['continuationContents']['itemSectionContinuation']['contents']
for comment in comments:
    text = comment['commentThreadRenderer']['comment']['commentRenderer']['contentText']['runs'][0]['text']
    print text
# print comments

