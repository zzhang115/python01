import pickle
with open("pickTestFile.pkl", "r") as handle:
    account_info = pickle.load(handle)
print "read:", account_info
handle.close()

account_info["100"] = ['zzc', "deposit"]
with open("pickTestFile.pkl", "w") as handle:
    pickle.dump(account_info, handle)
handle.close()

with open("pickTestFile.pkl", "rb") as handle:
    new = pickle.load(handle)
handle.close()
print "new", new