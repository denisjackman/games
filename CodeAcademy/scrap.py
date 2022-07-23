from requests import session

DATA = {
            "url": "http://madgamers.co.uk/newforum/index.php",
            "action": "do_login",
            "submit": "Login",
            "quick_login": "1",
            "quick_username": "denis_jackman",
            "quick_password": "moro1965",
        }

with session() as page:
    page.post("http://madgamers.co.uk/newforum/member.php", data=DATA)
    response = page.get("http://madgamers.co.uk/newforum/newthread.php?fid=96")

    '''
        print(response.headers)
        print(response.text)
    '''
