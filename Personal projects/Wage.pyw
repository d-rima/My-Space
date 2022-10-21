import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
import schedule
import time
import pyodbc

ID = 0

today = date.today()

cnxn = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}',server = 'localhost\SQLEXPRESS' , database = 'Econ')

cursor = cnxn.cursor()

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Safari/537.36'}

def get_data():

        employment_change_from_original_low = []
        employment_change_from_original_large = []
        employment_change_from_original_no = []

        URL = ''

        # Low hike state URLs
        Arizona_URL = 'https://www.google.com/search?q=what+is+the+current+unemployment+rate+in+arizona&sxsrf=ALiCzsYu5kxCIbIZprYL0r5mccRIEK7giw%3A1655272029341&ei=XXKpYv_DFJ_LkPIPjrq3iAg&ved=0ahUKEwi_5sLq4K74AhWfJUQIHQ7dDYEQ4dUDCA4&uact=5&oq=what+is+the+current+unemployment+rate+in+arizona&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAeEBYyBQgAEIYDOgcIABBHELADOgQIIxAnOgQILhAnOgUIABCRAjoKCAAQsQMQgwEQQzoRCC4QgAQQsQMQgwEQxwEQowI6CAguELEDEIMBOggIABCxAxCDAToOCC4QgAQQsQMQxwEQowI6BAgAEEM6CggAEIAEEIcCEBQ6CAgAEMkDEJECOggIABCABBDJAzoICAAQgAQQsQM6BwgjEOoCECc6EAgAEIAEEIcCELEDEIMBEBQ6CwgAEIAEELEDEIMBOhMIABCABBCHAhCxAxCDARDJAxAUOg0IABCABBCHAhDJAxAUSgYIPBICMjRKBAhBGABKBAhGGABQqDdYldoCYKfbAmgZcAF4BYABkQOIAYxQkgELMC4zMy4xNC4zLjGYAQCgAQGwAQrIAQjAAQE&sclient=gws-wiz'

        Colorado_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+colorado&sxsrf=ALiCzsbUO3DSskFAVirNiL4ezCvpIAuk7g%3A1655312407177&ei=FxCqYqe-CufAkPIPv-OWmAM&ved=0ahUKEwjnpZag96_4AhVnIEQIHb-xBTMQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+colorado&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAeEBYyCAgAEB4QDxAWMgYIABAeEBY6BwgAEEcQsAM6BAgjECc6BQgAEIYDSgUIPBIBMUoECEEYAEoECEYYAFDWCljWI2D5JmgBcAF4AYABggOIAbAZkgEHMC45LjUuMZgBAKABAcgBCMABAQ&sclient=gws-wiz'

        Maine_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+Maine&sxsrf=ALiCzsYIADmVywojOtIJhYVbqT6HP1QJgA%3A1655313120868&ei=4BKqYtPPNLyckPIP0pqdiA0&ved=0ahUKEwjTv770-a_4AhU8DkQIHVJNB9EQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+Maine&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjoHCAAQRxCwAzoFCAAQgARKBQg8EgEzSgQIQRgASgQIRhgAUOcMWP8PYO8RaANwAXgAgAGgA4gB-QeSAQcyLTEuMS4xmAEAoAEByAEIwAEB&sclient=gws-wiz'

        Massachusetts_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+massachusetts&sxsrf=ALiCzsZStEDhAHYa595DkOo4J7sU3uXzlg%3A1655313535977&ei=fxSqYoOaO7SekPIPwtCg6A8&oq=current+unemployment+rate+in+Mass&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQHhAWOgcIABBHELADOgQIIxAnOgUIABCABEoFCDwSATFKBAhBGABKBAhGGABQqwJY_ghgvxFoAXABeACAAcICiAHlCZIBBTItNC4xmAEAoAEByAEIwAEB&sclient=gws-wiz'

        Michigan_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+michigan&sxsrf=ALiCzsayYvyvbI-x2eKCJ84_BBSqQlRe9Q%3A1655313761347&ei=YRWqYvjmFO2hkPIPjrmc-A8&ved=0ahUKEwi4m_Kl_K_4AhXtEEQIHY4cB_8Q4dUDCA4&uact=5&oq=current+unemployment+rate+in+michigan&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBY6BwgAEEcQsAM6BAgjECdKBQg8EgExSgQIQRgASgQIRhgAUIKlBVi0rAVg7a0FaAFwAXgBgAGDBIgB9xOSAQkyLTEuNS4wLjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        Maryland_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+marland&sxsrf=ALiCzsYS97xebks4mxbdWRamvPZZ2fqYoA%3A1656974856961&ei=CG7DYumuOoSfkPIPyYSu-AQ&ved=0ahUKEwjp0oCuqOD4AhWED0QIHUmCC08Q4dUDCA8&uact=5&oq=current+unemployment+rate+in+marland&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEA06BAgAEEc6BAgjECc6CAgAEB4QDxAWOgYIABAeEBY6BQgAEIYDOgUIABCABDoFCCEQoAFKBAhBGABKBAhGGABQigRY3yxguTRoAXACeAGAAaMFiAGWK5IBCTItNC4wLjEuN5gBAKABAcgBCMABAQ&sclient=gws-wiz'

        Missouri_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+missouri&sxsrf=ALiCzsboVAa0koCf38mUfpOp_GGbgHVFMQ%3A1656993813996&ei=FbjDYo-4PKmekPIPtJC9mAI&ved=0ahUKEwjPlrb97uD4AhUpD0QIHTRIDyMQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+missouri&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMggIABAeEA8QFjoHCAAQRxCwAzoECCMQJzoGCAAQHhAWOgUIABCGA0oECEEYAEoECEYYAFD7A1iqFmC7HWgBcAF4A4AB7AaIAYYekgENMC4yLjUuMi4wLjEuMZgBAKABAcgBCMABAQ&sclient=gws-wiz'

        New_York_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+new+york&sxsrf=ALiCzsZyOU17-X2xdhUB5IMJFjWD4aTmnQ%3A1656993869117&ei=TbjDYtDYBvfNkPIPzry_sA8&oq=current+unemployment+rate+in+New&gs_lcp=Cgdnd3Mtd2l6EAEYAjIFCAAQgAQyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWOgcIABBHELADOgQIIxAnSgQIQRgASgQIRhgAUKQHWLEYYIgqaAFwAXgAgAHjAogBzxSSAQcwLjUuNC4ymAEAoAEByAEIwAEB&sclient=gws-wiz'

        Rhode_Island_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+rhode+island&sxsrf=ALiCzsabNIwa-pp42qP6EdmKpA_GuSKGpQ%3A1656993890850&ei=YrjDYtfFM8bXkPIPzLGciAE&ved=0ahUKEwjX_oii7-D4AhXGK0QIHcwYBxEQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+rhode+island&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjoHCAAQRxCwAzoFCAAQgAQ6BQgAEIYDSgQIQRgASgQIRhgAUIgEWM0jYOokaAFwAXgAgAGmAogBshKSAQUwLjUuNpgBAKABAcgBCMABAQ&sclient=gws-wiz'

        Vermont_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+vermont&sxsrf=ALiCzsbEhmoZ1b29hee9FTZwk5tQP3e4pA%3A1656993911968&ei=d7jDYv7cOomckPIPm_SH-AM&ved=0ahUKEwi-9JGs7-D4AhUJDkQIHRv6AT8Q4dUDCA4&uact=5&oq=current+unemployment+rate+in+vermont&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjoHCAAQRxCwAzoECCMQJzoFCAAQgAQ6BQghEKABOggIIRAeEBYQHToKCCEQHhAPEBYQHUoECEEYAEoECEYYAFDYAljRDWDuD2gBcAF4AIABoAKIAfUMkgEFMC4xLjaYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        Washington_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+Washington&sxsrf=ALiCzsZv3n7RPPK5j0df_ylekxkt0wpXtA%3A1656993932739&ei=jLjDYu3gLPHHkPIP9rm4wAs&ved=0ahUKEwjt1oW27-D4AhXxI0QIHfYcDrgQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+Washington&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIFCAAQhgMyBQgAEIYDOgcIABBHELADOgUIABCABEoECEEYAEoECEYYAFDiBFitEmCdFWgBcAF4AYABxAOIAcQWkgEJMC4yLjQuMi4ymAEAoAEByAEIwAEB&sclient=gws-wiz'

        # Large hike state URLs
        California_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+california&sxsrf=ALiCzsaJWfN0-9Ml5MvQXAy3ACi0iSK_xw%3A1655313918653&ei=_hWqYoTHJ9WgkPIP2IO24A8&oq=current+unemployment+rate+in+calif&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBY6BAgAEEc6BAgjECdKBQg6EgExSgQIQRgASgQIRhgAUGxY7BtgxyhoAHACeAOAAb8GiAGiH5IBDTAuMy4zLjMuMi4wLjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        Deleware_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+delaware&sxsrf=ALiCzsbsRjOiONWqly-lg3mSMH4reFBFhw%3A1655315037383&ei=XRqqYtaNF67KkPIPypat6AM&oq=current+unemployment+rate+in+Delew&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQHhAWOgcIABBHELADOgcIABCwAxBDOgYIABAeEA1KBQg8EgEzSgQIQRgASgQIRhgAUPAIWJgWYIMfaANwAXgAgAG7AYgB_QeSAQMwLjaYAQCgAQHIAQrAAQE&sclient=gws-wiz'

        Illinois_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+illinois&sxsrf=ALiCzsbqJPsv0RCXLKK45r9DN-bdGJSYDw%3A1655315079074&ei=hxqqYpGSBILBkPIPnoSxmAg&oq=current+unemployment+rate+in+Illin&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQyBggAEB4QFjIFCAAQhgM6BwgAEEcQsANKBQg8EgExSgQIQRgASgQIRhgAUKgEWOwKYOgVaAFwAXgAgAGgAogBkgiSAQUwLjMuMpgBAKABAcgBCMABAQ&sclient=gws-wiz'

        New_Mexico_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+new+mexico&sxsrf=ALiCzsZX9Yi7_o6PxXZCAvqJJ0xpWOUM9A%3A1655315105201&ei=oRqqYqDwC_vVkPIP7KGUoAo&ved=0ahUKEwjgxNimgbD4AhX7KkQIHewQBaQQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+new+mexico&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIGCAAQHhAWOgcIABBHELADOgQIIxAnOgUIABCABDoFCCEQoAE6BQghEKsCOggIIRAeEBYQHToFCAAQhgNKBQg8EgEySgQIQRgASgQIRhgAUPUGWMIhYPojaAJwAXgAgAHcAogB5RmSAQgwLjE0LjMuMZgBAKABAcgBCMABAQ&sclient=gws-wiz'

        Virginia_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+virginia&sxsrf=ALiCzsasg5RzVgqx-Ve7-zT6DoWmG2H0Mw%3A1655315142158&ei=xhqqYo-MCYWekPIP4t-a4AM&ved=0ahUKEwiPh6i4gbD4AhUFD0QIHeKvBjwQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+virginia&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBQgAEIYDOgcIABBHELADOgUIABCABEoFCDwSATFKBAhBGABKBAhGGABQ_gJYqQtgvQxoAXABeAGAAaUDiAH3CZIBBzAuNS40LTGYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        New_Jersey_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+New+Jersey&sxsrf=ALiCzsaAEsAKXKZNHbSMqAJ6VisiK3-eyg%3A1656993952495&ei=oLjDYoDxHZ2ekPIPi4GRyAU&ved=0ahUKEwiAwbu_7-D4AhUdD0QIHYtABFkQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+New+Jersey&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjoHCAAQRxCwAzoECCMQJzoFCAAQhgM6BQgAEIAESgQIQRgASgQIRhgAUIsCWN4dYLQfaAFwAXgBgAGvAogBuxaSAQcwLjcuNi4xmAEAoAEByAEIwAEB&sclient=gws-wiz'

        # No hike state URLs

        Alabama_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+Alabama&sxsrf=ALiCzsZ4eBh0owZhjyhY4p_9SkwnJP6xMw%3A1656993977482&ei=ubjDYreLHdHXkPIPwL62sA4&ved=0ahUKEwj3y7DL7-D4AhXRK0QIHUCfDeYQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+Alabama&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjoHCAAQRxCwAzoECCMQJzoFCAAQgAQ6CAgAEB4QDxAWSgQIQRgASgQIRhgAUOcDWJARYIYTaAFwAXgBgAHTBYgB_xOSAQsyLTEuMi4yLjAuMZgBAKABAcgBCMABAQ&sclient=gws-wiz'

        Alaska_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+Alaska&sxsrf=ALiCzsbRYlKtaf-q7tCGYHJ1-A428IRv0g%3A1656993999000&ei=zrjDYpvWPJvUkPIPwsq1gAI&ved=0ahUKEwib9dHV7-D4AhUbKkQIHUJlDSAQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+Alaska&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIFCAAQhgM6BwgAEEcQsANKBAhBGABKBAhGGABQ9QFYxQRgrwZoAXABeACAAcABiAGMBJIBAzAuM5gBAKABAcgBCMABAQ&sclient=gws-wiz'

        Arkansas_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+Arkansas&sxsrf=ALiCzsYbr7x44D0UvfTothjKug7308cFyg%3A1656994012701&ei=3LjDYvC2KpbJkPIP0ZaIiAQ&ved=0ahUKEwjwlJbc7-D4AhWWJEQIHVELAkEQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+Arkansas&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEOgcIABBHELADOgQIIxAnOgYIABAeEBY6CAgAEB4QDxAWOgUIABCGA0oECEEYAEoECEYYAFCnBljdF2DFGWgBcAF4AIAB5wOIAfoXkgEJMC4yLjYuMS4ymAEAoAEByAEIwAEB&sclient=gws-wiz'

        Connecticut_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+connecticut&sxsrf=ALiCzsbnYzC5L75xtXPVKYatNVoJgvf_ug%3A1656994028858&ei=7LjDYsSMNIWekPIPlvWj2Ac&oq=current+unemployment+rate+in+conn&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQHhAWMggIABAeEA8QFjIGCAAQHhAWMgUIABCGAzoHCAAQRxCwAzoFCAAQgARKBAhBGABKBAhGGABQrgZY5QlgvxloAnABeAGAAakDiAHgCJIBCTAuMS4yLjAuMZgBAKABAcgBCMABAQ&sclient=gws-wiz'

        Florida_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+florida&sxsrf=ALiCzsYVKrwS2-0Bt88QDqzjCBWM9SaXwQ%3A1656994044117&ei=_LjDYu3oBpOckPIPwfCimAI&ved=0ahUKEwjt1pPr7-D4AhUTDkQIHUG4CCMQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+florida&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMggIABAeEBYQCjIGCAAQHhAWMgUIABCGAzIFCAAQhgM6CggAEEcQsAMQyQM6BwgAEEcQsANKBAhBGABKBAhGGABQ0AhY6hBg6RFoAnABeACAAYACiAG7CZIBBTAuMy4zmAEAoAEByAEIwAEB&sclient=gws-wiz'
        
        Georgia_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+georgia&sxsrf=ALiCzsZnBsqKntvGGo-qvA1AzX9qHYeRSQ%3A1656994058787&ei=CrnDYtzWL4DLkPIP392C2Ak&ved=0ahUKEwjcg5Py7-D4AhWAJUQIHd-uAJsQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+georgia&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEOgoIABBHELADEMkDOgcIABBHELADOgYIABAeEBY6CAgAEB4QDxAWOgUIABCGA0oECEEYAEoECEYYAFCGDVj8E2CwF2gCcAF4AIABxAKIAcQMkgEHMC4zLjMuMZgBAKABAcgBCMABAQ&sclient=gws-wiz'

        Hawaii_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+hawaii&sxsrf=ALiCzsap79OqVntCpxwMW1T0qKimBGMYrg%3A1656994074821&ei=GrnDYovVMazTkPIPr6ONkA0&ved=0ahUKEwiLyuX57-D4AhWsKUQIHa9RA9IQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+hawaii&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEOgcIABBHELADOgYIABAeEBY6BQgAEIYDSgQIQRgASgQIRhgAUJkGWLwMYOoPaAJwAXgAgAGIAogBuQqSAQUwLjEuNZgBAKABAcgBCMABAQ&sclient=gws-wiz'

        Idaho_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+idaho&sxsrf=ALiCzsaeISKEslQvBIrqYxjbgh1RQTEg7Q%3A1656994092709&ei=LLnDYqj6KomfkPIP2fyu4Ao&ved=0ahUKEwiowKmC8OD4AhWJD0QIHVm-C6wQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+idaho&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIGCAAQHhAWMggIABAeEA8QFjIFCAAQhgM6BwgAEEcQsANKBAhBGABKBAhGGABQzgVY3wlgrAtoAnABeACAAc8BiAHABZIBBTAuMy4xmAEAoAEByAEIwAEB&sclient=gws-wiz'

        Indiana_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+indiana&sxsrf=ALiCzsYmm4PiBPOY27szPP1GMHqDkEAFVw%3A1656994105760&ei=ObnDYo2GLpW-kPIPiYyy2A8&ved=0ahUKEwjNhsaI8OD4AhUVH0QIHQmGDPsQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+indiana&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAeEBYyCAgAEB4QDxAWMgUIABCGAzIFCAAQhgM6BwgAEEcQsAM6BAgjECdKBAhBGABKBAhGGABQuwVY5QpgpxBoAnABeACAAcICiAGxDJIBBzAuMy4zLjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        Iowa_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+iowa&sxsrf=ALiCzsa6CSlGaJn8389pn59_LWEdVyz5JQ%3A1656994119456&ei=R7nDYtPAG5adkPIP-c6XmAQ&ved=0ahUKEwiTgIqP8OD4AhWWDkQIHXnnBUMQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+iowa&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCGAzoHCAAQRxCwAzoECCMQJ0oECEEYAEoECEYYAFC9BljECmC5C2gCcAF4AIABlQKIAb0FkgEFMC4xLjKYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        Kansas_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+kansas&sxsrf=ALiCzsbhGn2gv7TGAWKf8m7oGYixGLaIIA%3A1656994140479&ei=XLnDYq6zGKafkPIPxfmxiAc&ved=0ahUKEwiu0YiZ8OD4AhWmD0QIHcV8DHEQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+kansas&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIGCAAQHhAWMgUIABCGAzoHCAAQRxCwAzoFCAAQgAQ6BQghEKABSgQIQRgASgQIRhgAUJcFWMsOYNUTaANwAXgAgAH8AYgBmAuSAQUwLjQuM5gBAKABAcgBCMABAQ&sclient=gws-wiz'

        Kentucky_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+kentucky&sxsrf=ALiCzsZI_iu-Bczm_8LoHJUqxZwqTuO5iw%3A1656994154196&ei=arnDYuvNC4WckPIP6cuB6AQ&ved=0ahUKEwjrqtKf8OD4AhUFDkQIHellAE0Q4dUDCA4&uact=5&oq=current+unemployment+rate+in+kentucky&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBQgAEIYDMgUIABCGAzoHCAAQRxCwAzoKCAAQRxCwAxDJAzoICAAQkgMQsAM6BAgjECc6BQgAEIAESgQIQRgASgQIRhgAUPcGWP0OYLcRaAJwAXgAgAHbAYgB-QySAQUwLjEuN5gBAKABAcgBCsABAQ&sclient=gws-wiz'

        Louisiana_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+louisiana&sxsrf=ALiCzsYglBcsapZLVAZOiWpaFtBqCym3LQ%3A1656994464238&ei=oLrDYt2cDszIkPIPg6mgmAM&oq=current+unemployment+rate+in+Lo&gs_lcp=Cgdnd3Mtd2l6EAEYATIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIFCAAQhgM6BwgAEEcQsANKBAhBGABKBAhGGABQtQNY8AVgwxZoAXABeACAAawDiAH6BJIBBzItMS4wLjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        Minnesota_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+minnesota&sxsrf=ALiCzsaix2_vQ0c1w6wdM_ojFMlcCFQdZA%3A1656994169603&ei=ebnDYtKsJKeckPIPufm68AE&ved=0ahUKEwiSzf6m8OD4AhUnDkQIHbm8Dh4Q4dUDCA4&uact=5&oq=current+unemployment+rate+in+minnesota&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEOgcIABBHELADOgoIABBHELADEMkDOgQIIxAnOgYIABAeEBY6BQgAEIYDSgQIQRgASgQIRhgAUJ4FWOISYIYVaAJwAXgAgAG-AogBzQySAQcwLjIuNC4xmAEAoAEByAEIwAEB&sclient=gws-wiz'

        Mississippi_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+mississippi&sxsrf=ALiCzsZWrH8ZSdViWnn7eUcSxnBy9hJDCw%3A1656994183440&ei=h7nDYqjBGsC_kPIP8POnsAg&ved=0ahUKEwjooMut8OD4AhXAH0QIHfD5CYYQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+mississippi&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjoHCAAQRxCwAzoKCAAQRxCwAxDJAzoECCMQJzoFCAAQgAQ6BQgAEIYDSgQIQRgASgQIRhgAUPgEWPsUYI8XaAJwAXgAgAHRBIgBmxuSAQswLjEuNi4xLjIuMZgBAKABAcgBCMABAQ&sclient=gws-wiz'

        Montana_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+montana&sxsrf=ALiCzsZpbB2aGbnhXI36wyqcwOdUEgr0wA%3A1656994198160&ei=lrnDYs6wCYPXkPIPlaaQiAQ&ved=0ahUKEwjO08208OD4AhWDK0QIHRUTBEEQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+montana&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIGCAAQHhAWOgcIABBHELADOgQIIxAnOgUIABCABDoICAAQHhAPEBZKBAhBGABKBAhGGABQ1AdYkw5gyBloAnABeAGAAekEiAGTEZIBCzAuMS4zLjEuMS4xmAEAoAEByAEIwAEB&sclient=gws-wiz'

        Nebraska_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+nebraska&sxsrf=ALiCzsaVrhWZh93iVSvb3MCnC_XXMeqn1w%3A1656994215067&ei=p7nDYpbYA7qZkPIPkMOSEA&oq=current+unemployment+rate+in+nebraska&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQHhAWOgcIABBHELADOgoIABBHELADEMkDOgQIIxAnOgUIABCABDoFCAAQhgNKBAhBGABKBAhGGABQxwZYsQ5goBdoAnABeACAAa8CiAHvDpIBBzAuMS42LjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        Nevada_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+nevada&sxsrf=ALiCzsYai7W3uYnXUakcIubd08A6Pekl0A%3A1656994232006&ei=t7nDYqn9PJHXkPIPsfu5kAc&ved=0ahUKEwjptN_E8OD4AhWRK0QIHbF9DnIQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+nevada&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIGCAAQHhAWOgcIABBHELADOgUIABCGAzoECCMQJzoFCAAQgARKBAhBGABKBAhGGABQtgNY5BRgvBdoAXABeACAAYMDiAGgFZIBBzAuMy44LjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        New_Hampshire_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+new+hampshire&sxsrf=ALiCzsaPHpWvWfJEt7JahGJxNBeLbNnxEw%3A1656994249746&ei=ybnDYuydLYHNkPIPpfOZoA4&ved=0ahUKEwispprN8OD4AhWBJkQIHaV5BuQQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+new+hampshire&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjoHCAAQRxCwAzoECCMQJzoFCAAQgAQ6BQgAEIYDSgQIQRgASgQIRhgAUJ0DWNgYYOEZaAFwAXgCgAH-BYgBnCSSAQ0wLjMuNS4yLjEuMi4xmAEAoAEByAEIwAEB&sclient=gws-wiz'

        North_Carolina_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+north+carolina&sxsrf=ALiCzsY1OqXsYmPllfNXzuI8VFy_Qrhd9w%3A1656994264769&ei=2LnDYr_ZLrfWkPIPxLC_EA&ved=0ahUKEwi_pa_U8OD4AhU3K0QIHUTYDwIQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+north+carolina&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBQgAEIYDOgcIABBHELADOgoIABBHELADEMkDOgUIABCABEoECEEYAEoECEYYAFCRBVi1E2CiF2gBcAF4AYABsgSIAZEjkgELMC4xLjMuMi41LjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        North_Dakota_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+north+dakota&sxsrf=ALiCzsbOXGCiG9jTye54L6Ex0l4WVRtXrA%3A1656994278628&ei=5rnDYoL4Jc2dkPIP1ra9-As&ved=0ahUKEwiCg_3a8OD4AhXNDkQIHVZbD78Q4dUDCA4&uact=5&oq=current+unemployment+rate+in+north+dakota&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEOgcIABBHELADOgUIABCGA0oECEEYAEoECEYYAFDpAljzCGDaCmgBcAF4AIAB5gGIAeEHkgEFMC4yLjOYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        Ohio_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+ohio&sxsrf=ALiCzsZhvGJbKzttLpuZeaWIV5BsFGBFEQ%3A1656994292386&ei=9LnDYomjF-afkPIP0NSUiAM&ved=0ahUKEwiJ7cTh8OD4AhXmD0QIHVAqBTEQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+ohio&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBQgAEIYDOgcIABBHELADSgQIQRgASgQIRhgAUNgDWNEHYJgKaAFwAXgAgAGWBYgBjguSAQkyLTEuMC4xLjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        Oklahoma_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+oklahoma&sxsrf=ALiCzsbpGVFqQcfDABbZ4VHSF4osbPyXhQ%3A1656994305002&ei=ALrDYpLlPIXFkPIPrYeAgAM&ved=0ahUKEwiS5cbn8OD4AhWFIkQIHa0DADAQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+oklahoma&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIFCAAQhgM6BwgAEEcQsAM6BAgjECc6BQgAEIAESgQIQRgASgQIRhgAULMHWMgWYN4iaAFwAXgBgAH4BIgBhRqSAQswLjEuMy4yLjAuM5gBAKABAcgBCMABAQ&sclient=gws-wiz'

        Oregon_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+oregon&sxsrf=ALiCzsbm-m5SDaDjvLtATFQNEPR4912FcQ%3A1656994322283&ei=ErrDYsXzEMnGkPIPouen4AE&ved=0ahUKEwjFxOXv8OD4AhVJI0QIHaLzCRwQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+oregon&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAeEBYyBggAEB4QFjoKCAAQRxCwAxDJAzoHCAAQRxCwAzoECCMQJzoFCAAQhgNKBAhBGABKBAhGGABQsAZYnRhgoxpoAXABeAKAAesEiAHUHZIBCzAuMi41LjIuMS4ymAEAoAEByAEIwAEB&sclient=gws-wiz'

        Pennsylvania_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+pennsylvania&sxsrf=ALiCzsbrCNbRZ1UDF6ThZq1_4JxHkPr2Tg%3A1656994337393&ei=IbrDYrnFF8PVkPIP6ciZ-Ac&ved=0ahUKEwj52f_28OD4AhXDKkQIHWlkBn8Q4dUDCA4&uact=5&oq=current+unemployment+rate+in+pennsylvania&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAeEBY6BwgAEEcQsAM6CggAEEcQsAMQyQM6CAgAEB4QDxAWOgUIABCGA0oECEEYAEoECEYYAFDoBljvHmD7ImgCcAF4AIAByAKIAagTkgEHMC42LjUuMZgBAKABAcgBCMABAQ&sclient=gws-wiz'

        South_Carolina_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+south+carolina&sxsrf=ALiCzsbTmWZNMpkSKdM1gFkosE5pC66zow%3A1656994353652&ei=MbrDYui9J_qfkPIPmPC0gAY&ved=0ahUKEwiomuD-8OD4AhX6D0QIHRg4DWAQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+south+carolina&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIGCAAQHhAWMgYIABAeEBY6BAgAEEc6BQgAEIAEOgUIABCGA0oECEEYAEoECEYYAFCaCFjPH2CaJGgAcAR4A4ABmAaIAaYjkgELMi00LjQuMy4wLjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        South_Dakota_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+south+dakota&sxsrf=ALiCzsbIZXQevBs4bkhIitMiMc-2NOCFcA%3A1656994369763&ei=QbrDYpidLt6ekPIP3KmAmA0&ved=0ahUKEwjYwbeG8eD4AhVeD0QIHdwUANMQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+south+dakota&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIGCAAQHhAWOgcIABBHELADOgUIABCGA0oECEEYAEoECEYYAFCyCFj_DWCvEGgCcAF4AYABjAOIAcQKkgEHMC40LjEuMZgBAKABAcgBCMABAQ&sclient=gws-wiz'

        Tennessee_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+tennessee&sxsrf=ALiCzsaNbg4tKYv1iWqF3IOAQ3MidSR2cw%3A1656994382203&ei=TrrDYtmLDN3AkPIP9M-P0Ak&ved=0ahUKEwjZ6q6M8eD4AhVdIEQIHfTnA5oQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+tennessee&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIFCAAQhgM6BwgAEEcQsAM6BAgjECc6BAgAEEM6BQgAEIAESgQIQRgASgQIRhgAUKkEWLobYMIdaAJwAXgCgAGUBIgBgB-SAQswLjMuNi4yLjEuMpgBAKABAcgBCMABAQ&sclient=gws-wiz'

        Texas_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+texas&sxsrf=ALiCzsZvPX-NbAE1VyoDefNK4Aqebf2Xog%3A1656994396408&ei=XLrDYuvJGJnWkPIPoLe82Ak&ved=0ahUKEwjr55GT8eD4AhUZK0QIHaAbD5sQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+texas&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjoHCAAQRxCwAzoECCMQJzoFCAAQhgNKBAhBGABKBAhGGABQrwZY0xVgmRloAXABeACAAakFiAGfGJIBCzAuMi4yLjMuMC4ymAEAoAEByAEIwAEB&sclient=gws-wiz'

        Utah_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+utah&sxsrf=ALiCzsY4VQcdJKm6fXXRGgHc4_TZ-aXoow%3A1656994410834&ei=arrDYsy1MqLKkPIPluyM-AE&ved=0ahUKEwjMkoKa8eD4AhUiJUQIHRY2Ax8Q4dUDCA4&uact=5&oq=current+unemployment+rate+in+utah&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyCAgAEB4QDxAWMgYIABAeEBYyBQgAEIYDOgcIABBHELADOgUIABCABEoECEEYAEoECEYYAFC0BliSCmCKDGgCcAF4AIAB2AGIAYkGkgEFMC4yLjKYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        West_Virginia_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+west+virginia&sxsrf=ALiCzsZR3gF_avpLuEu4tw4euU3Aq8XaVw%3A1656994423102&ei=d7rDYoDxBa2YkPIP2caHuAI&ved=0ahUKEwjAiO-f8eD4AhUtDEQIHVnjAScQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+west+virginia&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIFCAAQhgMyBQgAEIYDOgcIABBHELADSgQIQRgASgQIRhgAUL0GWIMaYKQbaAJwAXgDgAGWBIgBmxySAQswLjEuMi4yLjQuMZgBAKABAcgBCMABAQ&sclient=gws-wiz'

        Wisconsin_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+wisconsin&sxsrf=ALiCzsaPeH_pp_-svsDs9fOJU9E0VfnAww%3A1656994437470&ei=hbrDYtmyHPTBkPIPx5iUyAs&oq=current+unemployment+rate+in+wiscon&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQ6BwgAEEcQsAM6BggAEB4QFjoICAAQHhAWEAo6BQgAEIYDSgQIQRgASgQIRhgAULwDWNUHYKoPaAFwAXgAgAGOAogB6QiSAQUwLjEuNJgBAKABAcgBCMABAQ&sclient=gws-wiz'

        Wyoming_URL = 'https://www.google.com/search?q=current+unemployment+rate+in+wyoming&sxsrf=ALiCzsYmyEr-qg_mTTYgQih11Z7dFaaitA%3A1656994452926&ei=lLrDYoaSOMHFkPIPuqysoAI&ved=0ahUKEwiGrIuu8eD4AhXBIkQIHToWCyQQ4dUDCA4&uact=5&oq=current+unemployment+rate+in+wyoming&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIICAAQHhAPEBYyBQgAEIYDOgcIABBHELADOgoIABBHELADEMkDOgQIIxAnOgUIABCABEoECEEYAEoECEYYAFDiCliNEWCMEmgDcAF4AIABmgKIAb0HkgEFMC4xLjOYAQCgAQHIAQjAAQE&sclient=gws-wiz'

        def Get_Unemployment(headers, URL):
            page = requests.get(URL, headers = headers)

            soup = BeautifulSoup(page.content, "html.parser")
            
            Unemployment = soup.find("p", class_="F0QAwe").get_text().strip()

            if len(Unemployment) > 2:
                Unemployment = float(Unemployment[0:3])
            else:
                Unemployment = float(Unemployment[0])
            State = soup.find("div", class_="EGmpye").get_text().strip().capitalize()
            cursor.execute(f"select StateID from State where State = '{State}'")
            
            for row in cursor:
                ID = row[0]

            today = date.today()

            cursor.execute(f"Insert into Unemployment_Rate(StateID, Unemployment_Rate, Date) Values ({ID}, {Unemployment}, '{today}')")

        # Adding the current unemployment rate for each of the low_bump states to their respective array
        URL = Arizona_URL
        Get_Unemployment(headers, URL)

        URL = Colorado_URL
        Get_Unemployment(headers, URL)

        URL = Maine_URL
        Get_Unemployment(headers, URL)

        URL = Massachusetts_URL
        Get_Unemployment(headers, URL)

        URL = Michigan_URL
        Get_Unemployment(headers, URL,)





        URL = California_URL
        Get_Unemployment(headers, URL)

        URL = Deleware_URL
        Get_Unemployment(headers, URL)

        URL = Illinois_URL
        Get_Unemployment(headers, URL)

        URL = New_Mexico_URL
        Get_Unemployment(headers, URL)

        URL = Virginia_URL
        Get_Unemployment(headers, URL)

        URL = Alabama_URL
        Get_Unemployment(headers, URL)

        URL = Alaska_URL
        Get_Unemployment(headers, URL)

        URL = Arkansas_URL
        Get_Unemployment(headers, URL)

        URL = Connecticut_URL
        Get_Unemployment(headers, URL)

        URL = Florida_URL
        Get_Unemployment(headers, URL)

        URL = Georgia_URL
        Get_Unemployment(headers, URL)

        URL = Hawaii_URL
        Get_Unemployment(headers, URL)

        URL = Idaho_URL
        Get_Unemployment(headers, URL)

        URL = Indiana_URL
        Get_Unemployment(headers, URL)

        URL = Iowa_URL
        Get_Unemployment(headers, URL)

        URL = Kansas_URL
        Get_Unemployment(headers, URL)

        URL = Kentucky_URL
        Get_Unemployment(headers, URL)

        URL = Louisiana_URL
        Get_Unemployment(headers, URL)

        URL = Minnesota_URL
        Get_Unemployment(headers, URL)

        URL = Mississippi_URL
        Get_Unemployment(headers, URL)

        URL = Montana_URL
        Get_Unemployment(headers, URL)

        URL = Nebraska_URL
        Get_Unemployment(headers, URL)

        URL = Nevada_URL
        Get_Unemployment(headers, URL)

        URL = New_Hampshire_URL
        Get_Unemployment(headers, URL)

        URL = North_Carolina_URL
        Get_Unemployment(headers, URL)

        URL = North_Dakota_URL
        Get_Unemployment(headers, URL)

        URL = Ohio_URL
        Get_Unemployment(headers, URL)

        URL = Oklahoma_URL
        Get_Unemployment(headers, URL)

        URL = Oregon_URL
        Get_Unemployment(headers, URL)

        URL = Pennsylvania_URL
        Get_Unemployment(headers, URL)

        URL = South_Carolina_URL
        Get_Unemployment(headers, URL)

        URL = South_Dakota_URL
        Get_Unemployment(headers, URL)

        URL = Tennessee_URL
        Get_Unemployment(headers, URL)

        URL = Texas_URL
        Get_Unemployment(headers, URL)

        URL = Utah_URL
        Get_Unemployment(headers, URL)

        URL = West_Virginia_URL
        Get_Unemployment(headers, URL)

        URL = Wisconsin_URL
        Get_Unemployment(headers, URL)

        URL = Wyoming_URL
        Get_Unemployment(headers, URL)

        URL = Maryland_URL
        Get_Unemployment(headers, URL)

        URL = Missouri_URL
        Get_Unemployment(headers, URL)

        URL = New_York_URL
        Get_Unemployment(headers, URL)

        URL = Rhode_Island_URL
        Get_Unemployment(headers, URL)

        URL = Vermont_URL
        Get_Unemployment(headers, URL)

        URL = Washington_URL
        Get_Unemployment(headers, URL)

        URL = New_Jersey_URL
        Get_Unemployment(headers, URL)



        average_low = []
        current_average_unemployment_low = 0
        cursor.execute("select Unemployment_Rate from Unemployment_By_Class where Hike_Class = 'Low_hike'")
        for row in cursor:
            average_low.append(row[0])
        for i in range(11):
            current_average_unemployment_low =  current_average_unemployment_low + average_low[i]
        current_average_unemployment_low = current_average_unemployment_low/11
        print(f'The current average unemployment for low hike states is: {current_average_unemployment_low}')


        average_large = []
        cursor.execute("select Unemployment_Rate from Unemployment_By_Class where Hike_Class = 'Large_hike'")
        for row in cursor:
            average_large.append(row[0])
        current_average_unemployment_high = 0
        for i in range(6):
            current_average_unemployment_high =  current_average_unemployment_high + average_large[i]
        current_average_unemployment_high = current_average_unemployment_high/6
        print(f'The current average unemployment for large hike states is: {current_average_unemployment_high}')

        average_no = []
        cursor.execute("select Unemployment_Rate from Unemployment_By_Class where Hike_Class = 'No_hike'")
        for row in cursor:
            average_no.append(row[0])
        current_average_unemployment_no = 0
        for i in range(33):
            current_average_unemployment_no =  current_average_unemployment_no + average_no[i]
        current_average_unemployment_no = current_average_unemployment_no/33
        print(f'The current average unemployment for no hike states is: {current_average_unemployment_no}')

        total_shift_unemployment_low = 0
        Original_rate = []
        cursor.execute("select Unemployment_Rate from Unemployment_By_Class where (Hike_Class = 'Low_hike' AND Date = '2022-01-01')")
        for row in cursor:
            Original_rate.append(row[0])
        Current_rate = []
        cursor.execute(f"select Unemployment_Rate from Unemployment_By_Class where (Hike_Class = 'Low_hike' AND Date = '{today}')")
        for row in cursor:
            Current_rate.append(row[0])

        for i in range(11):
            total_shift_unemployment_low = Original_rate[i] - Current_rate[i]
            employment_change_from_original_low.append(total_shift_unemployment_low)
        print(f'The shift in unemployment from January 2022 in low bump states, until now is: {employment_change_from_original_low}')

        total_shift_unemployment_large = 0
        Original_rate = []
        cursor.execute("select Unemployment_Rate from Unemployment_By_Class where (Hike_Class = 'Large_hike' AND Date = '2022-01-01')")
        for row in cursor:
            Original_rate.append(row[0])
        Current_rate = []
        cursor.execute(f"select Unemployment_Rate from Unemployment_By_Class where (Hike_Class = 'Large_hike' AND Date = '{today}')")
        for row in cursor:
            Current_rate.append(row[0])

        for i in range(6):
            total_shift_unemployment_large = Original_rate - Current_rate 
            employment_change_from_original_large.append(total_shift_unemployment_large)
        print(f'The shift in unemployment from January 2022 in large bump states, until now is: {employment_change_from_original_large}')

        total_shift_unemployment_no = 0
        Original_rate = []
        cursor.execute("select Unemployment_Rate from Unemployment_By_Class where (Hike_Class = 'No_hike' AND Date = '2022-01-01')")
        for row in cursor:
            Original_rate.append(row[0])
        Current_rate = []
        cursor.execute(f"select Unemployment_Rate from Unemployment_By_Class where (Hike_Class = 'No_hike' AND Date = '{today}')")
        for row in cursor:
            Current_rate.append(row[0])

        for i in range(33):
            total_shift_unemployment_no = Original_rate - Current_rate 
            employment_change_from_original_no.append(total_shift_unemployment_no)
        print(f'The shift in unemployment from January 2022 in No hike states, until now is: {employment_change_from_original_no}')

        average_total_shift_unemployment_low = 0
        for i in range(11):
            average_total_shift_unemployment_low = average_total_shift_unemployment_low + employment_change_from_original_low[i]
        average_total_shift_unemployment_low = average_total_shift_unemployment_low / 11
        print(f'The average total shift in unemployment among low bump states is {average_total_shift_unemployment_low}')

        average_total_shift_unemployment_large = 0
        for i in range(6):
            average_total_shift_unemployment_large = average_total_shift_unemployment_large + employment_change_from_original_large[i]
        average_total_shift_unemployment_large = average_total_shift_unemployment_large / 6
        print(f'The average total shift in unemployment among large bump states is {average_total_shift_unemployment_large}')

        average_total_shift_unemployment_no = 0
        for i in range(33):
            average_total_shift_unemployment_no = average_total_shift_unemployment_no + employment_change_from_original_no[i]
        average_total_shift_unemployment_no = average_total_shift_unemployment_no / 33
        print(f'The average total shift in unemployment among no bump states is {average_total_shift_unemployment_no}')

        cnxn.commit()
get_data()
