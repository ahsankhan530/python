def make_album(artist_name,album_title,track=0):
    if track:
        return {'artist name':artist_name,'album title':album_title,'track':track}
    else:
        return {'artist name':artist_name,'album title':album_title}
print(make_album('jhon','tiger'))
print(make_album(artist_name='ahsan',album_title='jj'))
print(make_album('a','b','rock'))

#================================



#==================================================================================================
def print_models(unprinted_design,completed_models):
    while unprinted_design:
        current_design=unprinted_design.pop()
        print("printing models :"+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\n the following models have been printed :")
    print(completed_models)
unprinted_designs=['iphone case','robot pendant','dodecahredon']
completed_models=[]
print_models(unprinted_designs,completed_models)
completed_models=[]