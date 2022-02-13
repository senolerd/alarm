from flask import Blueprint, jsonify

craiglistBP = Blueprint('craiglist', __name__, url_prefix='/craiglist')


@craiglistBP.route('/')
def craiglist_index():
    return {"api_version":"v1.0"}


##########
@craiglistBP.route('/get_sales')
def get_sales():
    return jsonify(sales)


sales = [
    {"name":"antiques", "types":["ata", "atq", "atd"]},
    {"name":"appliances", "types":["ppa", "app", "ppd"]},
    {"name":"arts & crafts", "types":["ara", "art", "ard"]},
    {"name":"atvs, utvs, snowmobiles", "types":["sna", "snw", "snd"]},
    {"name":"auto parts", "types":["pta", "pts", "ptd"]},
    {"name":"aviation", "types":["ava", "avo", "avd"]},
    {"name":"baby & kid stuff", "types":["baa", "bab", "bad"]},
    {"name":"barter", "types":["bar", "bar", "bar"]},
    {"name":"health and beauty", "types":["haa", "hab", "had"]},
    {"name":"bicycle parts", "types":["bip", "bop", "bdp"]},
    {"name":"bicycle parts", "types":["bip", "bop", "bdp"]},
    {"name":"bicycles", "types":["bia", "bik", "bid"]},
    {"name":"boat parts & accessories", "types":["bpa", "bpo", "bpd"]},
    {"name":"boats", "types":["boo", "boa", "bod"]},
    {"name":"books & magazines", "types":["bka", "bks", "bkd"]},
    {"name":"business / commercial", "types":["bfa", "bfs", "bfd"]},
    {"name":"cars & trucks", "types":["cta", "cto", "ctd"]},
    {"name":"cds / dvds / vhs", "types":["ema", "emd", "emq"]},
    {"name":"cell phones", "types":["moa", "mob", "mod"]},
    {"name":"collectibles", "types":["cba", "clt", "cbd"]},
    {"name":"computer parts", "types":["syp", "sop", "sdp"]},
    {"name":"computers", "types":["sya", "sys", "syd"]},
    {"name":"electronics", "types":["ela", "ele", "eld"]},
    {"name":"farm & garden", "types":["gra", "grd", "grq"]},
    {"name":"free stuff", "types":["zip", "zip", "zip"]},
    {"name":"furniture", "types":["fua", "fuo", "fud"]},
    {"name":"general for sale", "types":["foa", "for", "fod"]},
    {"name":"heavy equipment", "types":["hva", "hvo", "hvd"]},
    {"name":"household items", "types":["hsa", "hsh", "hsd"]},
    {"name":"jewelry", "types":["jwa", "jwl", "jwd"]},
    {"name":"materials", "types":["maa", "mat", "mad"]},
    {"name":"motorcycle parts & accessories", "types":["mpa", "mpo", "mpd"]},
    {"name":"motorcycles / scooters", "types":["mca", "mcy", "mcd"]},
    {"name":"musical instruments", "types":["msa", "msg", "msd"]},
    {"name":"photo/video", "types":["pha", "pho", "phd"]},
    {"name":"recreational vehicles", "types":["rva", "rvs", "rvd"]},
    {"name":"sporting goods", "types":["sga", "spo", "sgd"]},
    {"name":"tools", "types":["tla", "tls", "tld"]},
    {"name":"toys & games", "types":["taa", "tag", "tad"]},
    {"name":"trailers", "types":["tra", "tro", "trb"]},
    {"name":"video gaming", "types":["vga", "vgm", "vgd"]},
    {"name":"wanted", "types":["waa", "wan", "wad"]},
    {"name":"auto wheels & tires", "types":["wta", "wto", "wtd"]},
]