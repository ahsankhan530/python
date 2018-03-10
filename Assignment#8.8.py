def make_album(artist, title,track=0):
    active=True
    while active:

        if artist=='quite':
            active=False
            if title=='quite':
                SystemExit
        if track:
            return {'artist name': artist, 'album title': title, 'track': track}
        else:
            return {'artist name': artist, 'album title': title}


print(make_album(artist=input('put the artist name'),title=input('put the title name')))