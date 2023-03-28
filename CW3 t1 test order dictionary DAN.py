this_dict = {1:[3,4], 'fred':[5], ('little','shit'): [5,9,10]}

#order this in terms of the length of its zeroes. fuckk I've just realised that the#
#recursive way to solve this code before would actually be heaps better. so maybe
#i don't need to order them completely, I just need to access the zero with the least
# candidates. So why make the list at all then? so I can compare them I guess.
#and then access the necessary key data. but jeez i wish there were an easier
#way to find the least-candidate zero. Well there may well be, but I'll just
#write it in a way that makes sense to me at the moment. Then I'll work on efficiency
# and making it more recursive if necessary, because I think that's possible

values = this_dict.values()
# values.sort()
print(values)

