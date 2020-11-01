import pytest
from .common.requests_helper import SharedAPI
from .common.selenium_helper import SeleniumHelper
import os

@pytest.fixture(scope='session')
def houtai_session():
    login_url = os.environ.get('login_url')
    login_data = {
        'verifycode': '1',
        'username': os.environ.get('usr'),
        'password': os.environ.get('pwd'),
        'mobile': '1',
        'lt': 'LT-454616-rkGMsAK0hfQdHSXDDDLlvfWuA9pCNX-37.18.124',
        'isForm': 'yes',
        'execution': 'e223a350-d45b-48b6-a4c9-630a662a819a_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuUjI1R1Rrd3ZUR2RWYVdKUk1FMWhOVGx0WkdKMlV6ZzBUWGszYjNWdWVGWjROM2hDTWt4Qk5YSTFXV05sWWtaMWFFRmhkVFJ1YW5veVNVSkliakJqVXpJMmRscG1jMU16YzA1WlJXSkRTbkkwTW10SlFWSkhWMlpJUjJFMFJEUmtVUzh2ZUVOVlFtMW9NbU5ZTkZGR04zbFlaMU5oVFVsalYxZENVMnBOZUdKUVQxbFNOVmRpYlVWcU1FSlJORWxFTVhwSGIyMVRkbE41YlZGR09HdGFXRWw0UkVoRVdETktUaTltWWt0cEwyUlZSRWhQUW1oRVFUTlFPVlo2Y1ZSWk16Y3ZSa1JMUjBJMUwyYzNSbXhxZVhwdVZtbExURE5OYUhJMFJYRkpZa3dyUzNkcU0wbG5jRzVCUjFkbmNXUmxOMVV5ZGpBck56QkViMU12YlcwcmNFOUxaa2s0UkhCbGNrSnJRM1EzV21SbFRHZDBNbEZTS3poNVNIaHJhMFZzYzJaT1NVZFlWR1pqYWpONU1GQjROemRWVkhKQ0t6UkVhMVU1WW5sSVNGUnBMMWd6WVN0UmVGcFhaVFpyVlVGR1NHRnNRV1JXZFN0MVIySXlha2RrY21aaGJYZzVLMEpaUzNreVVtc3ZORXR6WVVOVmRIYzNWakE0UW14M2NHdFBNa2gxYVRoR1JVcFlNVkp4YkRORFozVnVjbmszYWxkUlUxUlVhRmsyVW5KcllqWm9lVlZIVFdaMU4xaHlSbTlHYUdOUVQybG9ORmRCZDJadmFtaDNWa1ZIV2xkRFZWWnZSMEYyY0hjclJUUjZiMUZITVUxV1YxVjNiWEJGYVZkU1QzTnFjMGhzY1VnNFZYWlZMMVpRV1ZsSFIwUlhaMFpvTHpCeGFuWlFkRlI1TDBOM1ZXVm1RMjUyUW01bVowbFdlbXhPWkdKcVUzWTFZME5qZUV0d1dqWk5UelV2TTNobFZGVk9iVkJhYVhabE5UQjRTVzFCUzFsRFUxZDBjaTlyUWpJMGR6RnFlVTlDZWpKUEszaFhTalZCTVVFNFVIQmpOa05VT1ZWalVpODNZek5yVkcxbVRYTTVZbmRpV2sxVGFHcFlhQzloWjJ4bmNuRnNhWFEzUTFKaFRXcFFhMHh1TjJKT01WWTRiMGhCU2pkUU9IWm5Wbmx4V0VOS1pGTnhVbWd2ZVZSWWRWUXdWazlQVm1GRVFsWTVkVzF2ZDBjMWEycGpkSFpvY1hOVFRYazBhMk1yTVVGNU5sVXJMMUJxTlRFclQxVTNibnBTTTJsek1rMHZLM0ZUYkZJeU0ydDVZalJFVFZSdmNWRnBkRmhYY25sMGVWTk5NMUF4ZFZWUU5GRkdWR3Q2YkhSdk5EbDJRU3MyVld0a2RtOXhSVlJ2WkROb2RGZDJja2cxTm04NFRUaGhjalZ5ZFU5eU0yWnpRelJzYTJOMlJHOUdkRXhPY0M5MFVFTmpOSE5DYVdoeVMxUmxhMFk1WTFndmVIRlhZWHBQVDB0bmRYZGhPVGxOV2tnelpGUmplVmRGYzBkeFRqTlJWa0o0VFdkRE4yRkVjVm95V21sdk9VdHVSbEZ2T1dkVmVXeENkMkZWZVVsblRUVXpjMXBFUlVwVmRtOU1NMlJ2UVVGQ01HZDRiM2hvVmprMmMwRlllbk00YWpoMVQzQkdUM2RRZG1od0szWndiR1ZrT1RaTFNIWkZNVGROUWpWbVl6UjZUVk5oYkVkNWVqQnVWVlJzYTJrMVVVaGpUeXRXVkRnM1UzTmtiREpJWm1jeFpFSjBaRlJOZGt4eFN5dGlhVWRWWm04dmNuazRjbTgyUTI5S2JUaFNVV0l4TmxWc1NESlBTVzFXVGtaR1dHdFpLMFYyT0daVU5UTkpVbWxrTm1GUVpqZGFNVUp1Ym1OeVNtbFFNMnhKV1ZwV2VFRm5PREpWWkVkSmVsZHVSMGhUY0RObWVGUTNTRE40WlVkTldVSnlUa2xxUjJVcmVuZDFhV0ZMYzB4RGVIZDJjVkJJUTBzemRsQTFSbFpFY2tjclJGSm9iVGRGVkZkVE4wRmtaa2RrVlZNMlUyMUVlRnBDU2sxRGVUaHBXRkJISzJwbFZ6WmFVRWRIYzFWSFdYcDNkRUV2WmxwWlJHaDVOM0IwYXpOS0sxZ3dUMHA1UWpWRWIzUkRVbmRxY21wWkwyNDJZV0ZwUjBSbVVEQktVMEV5VVRWUWNUWmtiVFpOVlVoNVVrazNialZWYVdwSVRscGliVkphV2pkeFdYY3pabTQxUnpOTmNsTkJSREJxUTJNclREZGlaRkF5YW5oT05VaG1SMG8yZDJGTldVSklSVXh6VlVzNVlWSkpaRFpYVDFGcFNYTjJNVWh3VDJORldtdEJZMGxIVVROaWRVWjBXbVZPYW1OT1ExZzJSelF3UzNOR09HUnJkR1ZvTUhabGJuRnZlVVpsTmpkUE1sTlphRWR6VlZKUGVVTjVTa3R2UVdaVFZqaGFTMHhHUVRGbE0yTXlZVEpUYmxGRmVrRTNXamh2Unk5VFNrVnBWa1prWjJ4SWMzWkhiVWhPTkhkaFNtY3hjVVpLVTNKR1JtMUJNVlowYVdWS1dXb3pURzV0YVdveVFVY3ZURTB3Ym5BNFNqZHdXVGR0YVVOUFRVdzJkblZUWTBWVFdWZFVhalpwT1M4MllqaHhPVmh5ZFdGTWNEaFFiMVFyWWtKaVZYUnVhbFZXZEZBMlFWTTBOamw2VVVSM1VsbHVSVkkzYTI0MVZ6aHFaR3R2WTFCaWNITTRTRE50WkZNMk1FeGFaRFZDYUcxa1RYcDNXWEpWWkhkU05YSlZTR2xEWm1zNVVEZEpTVmxTUVdGdmFYcHFVblZ6VFhnNVdIbHFNSFJVVWxRcmFXWXpXbnBwTW1ScFNrVnFlbHB4WnpRMWJqUlpWRTh2YTFWU2VERnhNVTkzZVRWYVJDOU9WR0Z4UmpJMlpWVmFiRm8zWWs1amRWTkxiVmw0V0ZWdmNIUkxlRmdyTUhwWFNUazNVM0JYUmxrME4yY3libmd3ZFVwalRub3dkM05QWlRSMlEzWktWamxWUWsxQk1XOU5la05CZEdKdVJHVmpPRmczY1VKNVNsSlRZMXBDU0VGbFpUSm5VMUpPYlZKVGJrVlpUbXhqVm5Kd1YwUktielYxTkZnd1FtaENMMFppY1ZBMk0zWkliWGxrUmlzMk9WY3JlRGg2VWxST1ozSmxhRFprU1VkT1pHNWhORVZOV1hsa2RHNWhVR3R5TW1Sa1kyeFVXbXRzTUN0UFZrMTJXVmRYWjBKRGVuSnVVMWsyY2pRelQyTlJPRWhuWmtNdk0xVXpZWGR6VEd4T1ZHTlRlVkpHWlhCU2JFWlhPSEZLZURSaVdWbDNhbVEwU2taSU1XSjVUM0JrVjJWU1ZUbDZPSEo1U1VGTlNsZDBPV1F5YUhCTU5tSktRMnhSTURWclVVVTBUazF6ZFVodGIzWjVTRlV2VURCeFZXbFplbEJOU1dsUFlYSnRVWG94VTNGSU1qZHZiV041THpJeE9FbFlLMGMzWkhCdVZHZzBkMnhWUzNKV1lTOXRUMlIzZEc5MVJtVTVRMWhSZURFMGVFTnFVRUpRZWxSMFJrbElOVTFNT1VKRWFIWkdSbXBOTkVOR1kxbHlVVVpQYVdaQmNXMVFSRXBWYzJWRlJqSnhZMDlzVUdOVVdsTmhWMjlOUzIxdmQwOXZMekpHTm5ORmVHaDJVbE0yVUV4R09FOUZaMlExVjFGUU1uZFRlbGxTYzJoWVZqY3hUbWxRVEZsWmR6WllMMDlIUms1bWRHdHFiekZFUjNsMlYwaEthamQyWjFONVdXVmFOMkZoTnk5RmExbGFTR1YzTmsxaGNtRnBPR0pZUlVscVdURk9RMGR6UlRsSVFUWnNVMk5YZVVKQ0wwSk1PV1kyV1RKd2IxWXpOMGc1T1VGa2R6QnVWblpyVVhGRFZDOTRjVmRGYUVOUk5rMW9ibWhJZDJsWFRuRlhWVVpzVFhKMVRIaGlhMFV5YzNGUFJucE5TV0VyZDJkUVFXeFNWbTl0V2tKTlZUVkVhRWN6Um05cmR6SlNlWEZLTHpaeGRsbGFLMHBRZVZWNk1sbEtVM2hxUkc5NU5VWkhValJ1Y2tSNFdVWkxUWGN4UVROd01taG9UblEzYjB4aWFEWnhXbTVVWWxkWlZFdDVSMGRMY25BeVNVOWpTUzk2WW1rMWQxTm5TM0E0TURabFRURm5ZemRtU1hSVmRtSnlNSHBYTkZOM1FWWnBaV3hYSzJNNFNVOVJiakZ6UmpOVmNYSlVZbVZvVlVwVGVYTmtjMkZPWVVGVWJVbEhkREZDWWtremNVTlRiMDkxV210Qk5IUkRiR1l4U0RaUVJuWlZObGRRYlZOTk5VcFRVVEJQVWtadlYxWkVNV28yTnpGdVlUUnFaWEkyTTFWRWNtMVpVbEV3VVZOdFFWSlFURTFNVFZCcGFXTlZTREY0VHl0RWNFVlpPSGhCVDFaRFZrTlBhRE5NYVM5RWIydGllbkY1V0VGRGFGcDBWVTFpY1U5blkwRTVUakF3WmxCdVpFdFhhRFp6VUU1SGN6QlpTakpzS3pacWRqRXhOMWxXTjJWWlJUWkROVGhYYTBWeFlXMVFaRmxTTlVONmRIRm5TRXdyUzB4MVYycDNhR2hYV1U1SGMyUjNVMWd4TlVRdk1sSkJRblo1ZUdWT1FVZHNaRzFEU205M01sWTFZbXhTVTNOaU5raGphMkpNVjA1V2FVZFpXVEIzVGswMGFrOTViRVJaVmxrMmRVaHlNemRIVlZSTVZEYzRPSFUyUlV0NWVqaHVNa3RUV25ob2RuTnRlaTlhTUZseGVVcGhSMmhvYlZadk1FTm1Ra2g1WkhoWFltOWpTV2h3ZEZOWmFuaEhWVlZ5YjB0M1dsUTVTVFl5Tm1OdFFVdHRka1pEWlVSV2NXWXpObEZZY2k4eGNYZERPV2R5WmxFeGFtZFRVRmR6ZGs5SlpDdDVTakVyWkc5NlJVaDJNMXBxVTNoeFZFZEdjVFl4YkRkclNqZEhTMndyVEc1Vk1uY3hZMUJoUTBSUGNuZE9RbUZPVFhGNU0wSnlXVlZoTlRobldrUnRTVEl6V21oalFUMDkuM3NDOFI5UGFRWkRSOTBPZ0tGX2NPZ08yanRrTzJya1Fvc3hNdTM0TjNpUUtnMExRWjlsbTV1eXVVOTgtY1RBay1fVFBRblREY2dENXdsRmwxeGlfVVE=',
        '_rememberMe': 'on',
        '_eventId': 'submit',
    }
    se = SharedAPI(login_url=login_url, login_data=login_data)
    se.login()
    return se.s


@pytest.fixture(scope='session')
def driver():
    d = SeleniumHelper.initial_driver('chrome')
    yield d
    d.close()