from flask import Blueprint, jsonify
from flask_login import login_required,current_user

craiglistBP = Blueprint('craiglist', __name__, url_prefix='/craiglist')


from alarm import login_manager


@craiglistBP.route('/')
def craiglist_index():
    return {"api_version":"v1.0"}


@craiglistBP.route('/get_sales')
def get_sales():
    print("User at Login required route: ", current_user)
    return jsonify(sales)


@craiglistBP.route('/cities')
def get_cities():
    return jsonify(state_and_cities)


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


state_and_cities= [
    { "Alabama": [
                    {"name":"auburn", "code":"auburn"},
                    {"name":"birmingham", "code":"bham"},
                    {"name":"columbus", "code":"columbusga"},
                    {"name":"columbus", "code":"columbusga"},
                    {"name":"dothan", "code":"dothan"},
                    {"name":"florence / muscle shoals", "code":"shoals"},
                    {"name":"gadsden-anniston", "code":"gadsden"},
                    {"name":"huntsville / decatur", "code":"huntsville"},
                    {"name":"mobile", "code":"mobile"},
                    {"name":"montgomery", "code":"montgomery"},
                    {"name":"tuscaloosa", "code":"tuscaloosa"},
                ]
    },

    { "Alaska" :[
                    {"name":"anchorage / mat-su", "code":"anchorage"},
                    {"name":"fairbanks", "code":"fairbanks"},
                    {"name":"kenai peninsula", "code":"kenai"},
                    {"name":"southeast alaska", "code":"juneau"},  
                ]
    },
    # { "arizona":[
    #                 {"name":"flagstaff / sedona", "code":"flagstaff"},
    #                 {"name":"mohave county", "code":"mohave"},
    #                 {"name":"phoenix", "code":"phoenix"},
    #                 {"name":"prescott", "code":"prescott"},
    #                 {"name":"show low", "code":"showlow"},
    #                 {"name":"sierra vista", "code":"sierravista"},
    #                 {"name":"tucson", "code":"tucson"},
    #                 {"name":"yuma", "code":"yuma"}
    #             ]
    # },
    # { "Arkansas": [
    #                 {"name":"fayetteville", "code": "fayar"},
    #                 {"name":"fort smith", "code": "fortsmith"},
    #                 {"name":"jonesboro", "code": "jonesboro"},
    #                 {"name":"little rock", "code": "littlerock"},
    #                 {"name":"memphis, TN", "code": "memphis"},
    #                 {"name":"texarkana", "code": "texarkana"}
    #                 ]
    # },
    # { "California": [
    #                 {"name":"bakersfield","code":"bakersfield"},
    #                 {"name":"chico","code":"chico"},
    #                 {"name":"fresno / madera","code":"fresno"},
    #                 {"name":"gold country","code":"goldcountry"},
    #                 {"name":"hanford-corcoran","code":"hanford"},
    #                 {"name":"humboldt county","code":"humboldt"},
    #                 {"name":"imperial county","code":"imperial"},
    #                 {"name":"inland empire - riverside and san bernardino counties","code":"inlandempire"},
    #                 {"name":"los angeles","code":"losangeles"},
    #                 {"name":"mendocino county","code":"mendocino"},
    #                 {"name":"merced","code":"merced"},
    #                 {"name":"modesto","code":"modesto"},
    #                 {"name":"monterey bay","code":"monterey"},
    #                 {"name":"orange county","code":"orangecounty"},
    #                 {"name":"palm springs","code":"palmsprings"},
    #                 {"name":"redding","code":"redding"},
    #                 {"name":"reno / tahoe","code":"reno"},
    #                 {"name":"sacramento","code":"sacramento"},
    #                 {"name":"san diego","code":"sandiego"},
    #                 {"name":"san luis obispo","code":"slo"},
    #                 {"name":"santa barbara","code":"santabarbara"},
    #                 {"name":"santa maria","code":"santamaria"},
    #                 {"name":"SF bay area","code":"sfbay"},
    #                 {"name":"siskiyou county","code":"siskiyou"},
    #                 {"name":"stockton","code":"stockton"},
    #                 {"name":"susanville","code":"susanville"},
    #                 {"name":"ventura county","code":"ventura"},
    #                 {"name":"visalia-tulare","code":"visalia"},
    #                 {"name":"yuba-sutter","code":"yubasutter"}
    #     ]
    # },


]
