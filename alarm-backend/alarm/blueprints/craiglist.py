from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from sqlalchemy import null
from alarm.models import CraiglistAlarm
from alarm import db
craiglistBP = Blueprint('craiglist', __name__, url_prefix='/craiglist')

from alarm import login_manager


@craiglistBP.route('/')
def craiglist_index():
    return {"api_version":"v1.0"}


@craiglistBP.route('/create', methods=['POST'])
@login_required
def create():
    try:
        data = request.get_json()
        clAlarm = CraiglistAlarm( user_id = current_user.id, name = data['name'], url = data['url'],  data = data )
        db.session.add(clAlarm)
        db.session.commit()
        return {"status":"ok"}, 200
    except:
        return {"status":"error"}, 400


@craiglistBP.route('/list')
@login_required
def list():
    alarm_list = CraiglistAlarm.query.filter_by(user_id = current_user.id)

    temp_alarm_list = []

    for alarm in alarm_list:
        alarm.data['id'] = alarm.id
        temp_alarm_list.append(alarm.data)


    return jsonify([ alarm for alarm in temp_alarm_list ])


@craiglistBP.route('/delete/<id>', methods=['DELETE'])
@login_required
def delete(id):
    alarm = CraiglistAlarm.query.filter_by(id=id).first()
    try:
        if alarm.user_id == current_user.id:
            db.session.delete(alarm)
            db.session.commit()
            return {"delete": "ok"}, 200
    except Exception as e:
        return {"delete": "error"}, 400
        



@craiglistBP.route('/get_sales')
def get_sales():
    print("User at Login required route: ", current_user)
    return jsonify(sales_types)


@craiglistBP.route('/get_cities')
def get_cities():
    return jsonify(state_and_cities)


sales_types = [
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
                    {"name":"Auburn", "code":"auburn"},
                    {"name":"Birmingham", "code":"bham"},
                    {"name":"Columbus", "code":"columbusga"},
                    {"name":"Columbus", "code":"columbusga"},
                    {"name":"Dothan", "code":"dothan"},
                    {"name":"Florence / muscle shoals", "code":"shoals"},
                    {"name":"Gadsden-anniston", "code":"gadsden"},
                    {"name":"Huntsville / decatur", "code":"huntsville"},
                    {"name":"Mobile", "code":"mobile"},
                    {"name":"Montgomery", "code":"montgomery"},
                    {"name":"Tuscaloosa", "code":"tuscaloosa"},
                ]
    },
    { "Alaska" :[
                    {"name":"Anchorage / mat-su", "code":"anchorage"},
                    {"name":"Fairbanks", "code":"fairbanks"},
                    {"name":"Kenai peninsula", "code":"kenai"},
                    {"name":"Southeast alaska", "code":"juneau"},  
                ]
    },
    { "Arizona":[
                    {"name":"Flagstaff / sedona", "code":"flagstaff"},
                    {"name":"Mohave county", "code":"mohave"},
                    {"name":"Phoenix", "code":"phoenix"},
                    {"name":"Prescott", "code":"prescott"},
                    {"name":"Show low", "code":"showlow"},
                    {"name":"Sierra vista", "code":"sierravista"},
                    {"name":"Tucson", "code":"tucson"},
                    {"name":"Yuma", "code":"yuma"}
                ]
    },
    { "Arkansas": [
                    {"name":"Fayetteville", "code": "fayar"},
                    {"name":"Fort smith", "code": "fortsmith"},
                    {"name":"Jonesboro", "code": "jonesboro"},
                    {"name":"Little rock", "code": "littlerock"},
                    {"name":"Memphis, TN", "code": "memphis"},
                    {"name":"Texarkana", "code": "texarkana"}
                    ]
    },
    { "California": [
                    {"name":"Bakersfield","code":"bakersfield"},
                    {"name":"Chico","code":"chico"},
                    {"name":"Fresno / madera","code":"fresno"},
                    {"name":"Gold country","code":"goldcountry"},
                    {"name":"Hanford-corcoran","code":"hanford"},
                    {"name":"Humboldt county","code":"humboldt"},
                    {"name":"Imperial county","code":"imperial"},
                    {"name":"Inland empire - riverside and san bernardino counties","code":"inlandempire"},
                    {"name":"Los angeles","code":"losangeles"},
                    {"name":"Mendocino county","code":"mendocino"},
                    {"name":"Merced","code":"merced"},
                    {"name":"Modesto","code":"modesto"},
                    {"name":"Monterey bay","code":"monterey"},
                    {"name":"Orange county","code":"orangecounty"},
                    {"name":"Palm springs","code":"palmsprings"},
                    {"name":"Redding","code":"redding"},
                    {"name":"Reno / tahoe","code":"reno"},
                    {"name":"Sacramento","code":"sacramento"},
                    {"name":"San diego","code":"sandiego"},
                    {"name":"San luis obispo","code":"slo"},
                    {"name":"Santa barbara","code":"santabarbara"},
                    {"name":"Santa maria","code":"santamaria"},
                    {"name":"SF bay area","code":"sfbay"},
                    {"name":"Siskiyou county","code":"siskiyou"},
                    {"name":"Stockton","code":"stockton"},
                    {"name":"Susanville","code":"susanville"},
                    {"name":"Ventura county","code":"ventura"},
                    {"name":"Visalia-tulare","code":"visalia"},
                    {"name":"Yuba-sutter","code":"yubasutter"}
        ]
    },
    { "Colorado" : [
                    {"name":"Boulder","code":"boulder"},
                    {"name":"Bolorado springs","code":"cosprings"},
                    {"name":"Denver","code":"denver"},
                    {"name":"Eastern CO","code":"eastco"},
                    {"name":"Fort collins / north CO","code":"fortcollins"},
                    {"name":"High rockies","code":"rockies"},
                    {"name":"Pueblo","code":"pueblo"},
                    {"name":"Western slope","code":"westslope"},
            ]
    },
    { "Connecticut" : [
                {"name":"Eastern CT","code":"newlondon"},
                {"name":"Hartford","code":"hartford"},
                {"name":"New haven","code":"newhaven"},
                {"name":"Northwest CT","code":"nwct"},

        ]
    },
    { "DC" : [
                {"name":"Washington, DC","code":"washingtondc"},
                {"name":"Hartford","code":"hartford"},
                {"name":"New haven","code":"newhaven"},
                {"name":"Northwest CT","code":"nwct"},

        ]
    },
    { "Delaware" : [
                {"name":"Delaware","code":"delaware"},
        ]
    },
    { "Florida" : [
                {"name":"Daytona beach","code":"daytona"},
                {"name":"Florida keys","code":"keys"},
                {"name":"Ft myers / SW florida","code":"fortmyers"},
                {"name":"Gainesville","code":"gainesville"},
                {"name":"Heartland florida","code":"cfl"},
                {"name":"Jacksonville","code":"jacksonville"},
                {"name":"Lakeland","code":"lakeland"},
                {"name":"North central FL","code":"lakecity"},
                {"name":"Ocala FL","code":"ocala"},
                {"name":"Okaloosa / walton","code":"okaloosa"},
                {"name":"Panama city / walton","code":"panamacity"},
                {"name":"Pensacola","code":"pensacola"},
                {"name":"Sarasota-bradenton","code":"sarasota"},
                {"name":"South florida - includes separate sections for miami/dade, broward, and palm beach counties","code":"miami"},
                {"name":"Space coast","code":"spacecoast"},
                {"name":"St augustine","code":"staugustine"},
                {"name":"Tallahassee","code":"tallahassee"},
                {"name":"Tampa bay area","code":"tampa"},
                {"name":"Treasure coast","code":"treasure"},

        ]
    },
    { "Georgia" : [
                {"name":"Albany","code":"albanyga"},
                {"name":"Athens","code":"athensga"},
                {"name":"Atlanta","code":"atlanta"},
                {"name":"Augusta","code":"augusta"},
                {"name":"Brunswick","code":"brunswick"},
                {"name":"Columbus","code":"columbusga"},
                {"name":"Macon / warner robins","code":"macon"},
                {"name":"Northwest GA","code":"nwga"},
                {"name":"Savannah / hinesville","code":"savannah"},
                {"name":"Statesboro","code":"statesboro"},
                {"name":"Valdosta","code":"valdosta"},
        ]
    },
    { "Guam-Micronesia" : [
                {"name":"Guam-micronesia","code":"micronesia"},
        ]
    },
    { "Hawaii" : [
                {"name":"Hawaii","code":"honolulu"},
        ]
    },
    { "Idaho" : [
                {"name":"Boise","code":"boise"},
                {"name":"East idaho","code":"eastidaho"},
                {"name":"Lewiston / clarkston","code":"lewiston"},
                {"name":"Pullman / moscow / clarkston","code":"pullman"},
                {"name":"Spokane / coeur d'alene","code":"spokane"},
                {"name":"Twin falls","code":"twinfalls"},
        ]
    },
    { "Illinois" : [
                {"name":"Bloomington-normal","code":"bn"},
                {"name":"Champaign urbana","code":"chambana"},
                {"name":"Chicago","code":"chicago"},
                {"name":"Decatur","code":"decatur"},
                {"name":"La salle co","code":"lasalle"},
                {"name":"Mattoon-charleston","code":"mattoon"},
                {"name":"Peoria","code":"peoria"},
                {"name":"Quad cities, IA/IL","code":"quadcities"},
                {"name":"Rockford, IA/IL","code":"rockford"},
                {"name":"Southern illinois, IA/IL","code":"carbondale"},
                {"name":"Springfield, IA/IL","code":"springfieldil"},
                {"name":"St louis, MO","code":"stlouis"},
                {"name":"St western IL","code":"quincy"},
        ]
    },  
    { "Indiana" : [
                {"name":"Bloomington","code":"bloomington"},
                {"name":"Evansville","code":"evansville"},
                {"name":"Fort wayne","code":"fortwayne"},
                {"name":"Indianapolis","code":"indianapolis"},
                {"name":"Kokomo","code":"kokomo"},
                {"name":"Lafayette / west lafayette","code":"tippecanoe"},
                {"name":"Muncie / anderson","code":"muncie"},
                {"name":"Richmond","code":"richmondin"},
                {"name":"South bend / michiana","code":"southbend"},
                {"name":"Terre haute","code":"terrehaute"},
        ]
    },
    { "Iowa" : [
                {"name":"Ames","code":"ames"},
                {"name":"Cedar rapids","code":"cedarrapids"},
                {"name":"Des moines","code":"desmoines"},
                {"name":"Dubuque","code":"dubuque"},
                {"name":"Fort dodge","code":"fortdodge"},
                {"name":"Iowa city","code":"iowacity"},
                {"name":"Mason city","code":"masoncity"},
                {"name":"Omaha / council bluffs","code":"omaha"},
                {"name":"Quad cities, IA/IL","code":"quadcities"},
                {"name":"Sioux city","code":"siouxcity"},
                {"name":"Southeast IA","code":"ottumwa"},
                {"name":"Waterloo / cedar falls","code":"waterloo"},
        ]
    },
    { "Kansas" : [
                {"name":"Kansas city, MO","code":"kansascity"},
                {"name":"Lawrence, MO","code":"lawrence"},
                {"name":"Manhattan","code":"ksu"},
                {"name":"Northwest KS","code":"nwks"},
                {"name":"Salina","code":"salina"},
                {"name":"Southeast KS","code":"seks"},
                {"name":"Southwest KS","code":"swks"},
                {"name":"Topeka KS","code":"swks"},
                {"name":"Topeka","code":"topeka"},
                {"name":"Wichita","code":"wichita"},
        ]
    },
    { "Kentucky" : [
                {"name":"Bowling green","code":"bgky"},
                {"name":"Cincinnati, OH","code":"cincinnati"},
                {"name":"Eastern kentucky, OH","code":"eastky"},
                {"name":"Huntington-ashland, OH","code":"huntington"},
                {"name":"Lexington, OH","code":"lexington"},
                {"name":"Louisville","code":"louisville"},
                {"name":"Owensboro","code":"owensboro"},
                {"name":"Western KY","code":"westky"},

        ]
    },
    { "Louisiana" : [
                {"mame":"Baton rouge", "code":"batonrouge"},
                {"mame":"Central louisiana", "code":"cenla"},
                {"mame":"Houma", "code":"houma"},
                {"mame":"Lafayette", "code":"lafayette"},
                {"mame":"Lake charles", "code":"lakecharles"},
                {"mame":"Monroe", "code":"monroe"},
                {"mame":"New orleans", "code":"neworleans"},
                {"mame":"Shreveport", "code":"shreveport"},
        ]
    },
    { "Maine" : [
                {"mame":"Maine", "code":"maine"},
        ]
    },
    { "Maryland" : [
                {"name":"Annapolis", "code": "annapolis"},
                {"name":"Baltimore", "code": "baltimore"},
                {"name":"Cumberland valley", "code": "baltimore"},
                {"name":"Eastern shore", "code": "easternshore"},
                {"name":"Frederick", "code": "frederick"},
                {"name":"Southern maryland", "code": "southern maryland"},
                {"name":"Western maryland", "code": "westmd"},
        ]
    },
    { "Massachusetts" : [
                {"name":"Boston - includes merrimack valley, metro west, north shore, south shore", "code": "boston"},
                {"name":"Cape cod / islands", "code": "capecod"},
                {"name":"South coast - southern bristol and plymouth counties", "code": "southcoast"},
                {"name":"Western massachusetts", "code": "westernmass"},
                {"name":"Worcester / central MA", "code": "worcester"},
        ]
    },
    { "Michigan" : [
                {"name":"Ann arbor", "code": "annarbor"},
                {"name":"Battle creek", "code": "battlecreek"},
                {"name":"Central michigan", "code": "centralmich"},
                {"name":"Detroit metro", "code": "detroit"},
                {"name":"Flint", "code": "flint"},
                {"name":"Grand rapids", "code": "grandrapids"},
                {"name":"Holland", "code": "holland"},
                {"name":"Jackson", "code": "jxn"},
                {"name":"Kalamazoo", "code": "kalamazoo"},
                {"name":"Lansing", "code": "lansing"},
                {"name":"Monroe", "code": "monroemi"},
                {"name":"Muskegon", "code": "muskegon"},
                {"name":"Northern michigan", "code": "nmi"},
                {"name":"Port huron", "code": "porthuron"},
                {"name":"Saginaw-midland-baycity", "code": "saginaw"},
                {"name":"South bend / michiana", "code": "southbend"},
                {"name":"Southwest michigan", "code": "swmi"},
                {"name":"The thumb", "code": "thumb"},
                {"name":"Upper peninsula", "code": "up"},
        ]
    },
    { "Minnesota" : [
                {"name":"Bemidji", "code": "bemidji"},
                {"name":"Brainerd", "code": "brainerd"},
                {"name":"Duluth / superior", "code": "duluth"},
                {"name":"Fargo / moorhead", "code": "fargo"},
                {"name":"Mankato", "code": "mankato"},
                {"name":"Minneapolis / st paul", "code": "minneapolis"},
                {"name":"Rochester", "code": "rmn"},
                {"name":"Southwest MN", "code": "marshall"},
                {"name":"St cloud", "code": "stcloud"},
        ]
    },
    { "Mississippi" : [
                {"name":"Gulfport / biloxi", "code": "gulfport"},
                {"name":"Hattiesburg", "code": "hattiesburg"},
                {"name":"Jackson", "code": "jackson"},
                {"name":"Memphis, TN", "code": "memphis"},
                {"name":"Meridian", "code": "meridian"},
                {"name":"North mississippi", "code": "northmiss"},
                {"name":"Southwest MS", "code": "natchez"},
        ]
    },
    { "Missouri" : [
                {"name":"Columbia / jeff city", "code":"columbiamo"},
                {"name":"Joplin", "code":"joplin"},
                {"name":"Kansas city", "code":"kansascity"},
                {"name":"Kirksville", "code":"kirksville"},
                {"name":"Lake of the ozarks", "code":"loz"},
                {"name":"Southeast missouri", "code":"semo"},
                {"name":"Springfield", "code":"springfield"},
                {"name":"St joseph", "code":"stjoseph"},
                {"name":"St louis", "code":"stlouis"}
        ]
    },
    { "Montana" : [
                {"name":"Billings", "code":"billings"},
                {"name":"Bozeman", "code":"bozeman"},
                {"name":"Butte", "code":"butte"},
                {"name":"Eastern montana", "code":"montana"},
                {"name":"Great falls", "code":"greatfalls"},
                {"name":"Melena", "code":"helena"},
                {"name":"Kalispell", "code":"kalispell"},
                {"name":"Missoula", "code":"missoula"},
        ]
    },  
    { "North Carolina" : [
                {"name":"Asheville", "code": "asheville"},
                {"name":"Boone", "code": "boone"},
                {"name":"Charlotte", "code": "charlotte"},
                {"name":"Eastern NC", "code": "eastnc"},
                {"name":"Fayetteville", "code": "fayetteville"},
                {"name":"Greensboro", "code": "greensboro"},
                {"name":"Hickory / lenoir", "code": "hickory"},
                {"name":"Jacksonville", "code": "onslow"},
                {"name":"Outer banks", "code": "outerbanks"},
                {"name":"Raleigh / durham / CH", "code": "raleigh"},
                {"name":"Wilmington", "code": "wilmington"},
                {"name":"Winston-salem", "code": "winstonsalem"},
        ]
    },
    { "Nebraska" : [
                {"name":"Grand island", "code": "grandisland"},
                {"name":"Lincoln", "code": "lincoln"},
                {"name":"North platte", "code": "northplatte"},
                {"name":"Omaha / council bluffs", "code": "omaha"},
                {"name":"Scottsbluff / panhandle", "code": "scottsbluff"},
                {"name":"Sioux city, IA", "code": "siouxcity"},
        ]
    },
    { "Nevada" : [
                {"name":"Elko", "code": "elko"},
                {"name":"Las vegas", "code": "lasvegas"},
                {"name":"Reno / tahoe", "code": "reno"},
        ]
    },
    { "New Jersey" : [
                {"name":"Central NJ", "code":"cnj"},
                {"name":"Jersey shore", "code":"jerseyshore"},
                {"name":"North jersey", "code":"newjersey"},
                {"name":"South jersey", "code":"southjersey"},
        ]
    },  
    { "New Mexico" : [
                {"name":"Albuquerque", "code":"albuquerque"},
                {"name":"Clovis / portales", "code":"clovis"},
                {"name":"Farmington", "code":"farmington"},
                {"name":"Las cruces", "code":"lascruces"},
                {"name":"Roswell / carlsbad", "code":"roswell"},
                {"name":"Santa fe / taos", "code":"santafe"},
        ]
    },
    { "New York" : [
                {"name": "Albany", "code":"albany"},
                {"name": "Binghamton", "code":"binghamton"},
                {"name": "Buffalo", "code":"buffalo"},
                {"name": "Catskills", "code":"catskills"},
                {"name": "Chautauqua", "code":"chautauqua"},
                {"name": "Elmira-corning", "code":"elmira"},
                {"name": "Finger lakes", "code":"fingerlakes"},
                {"name": "Glens falls", "code":"glensfalls"},
                {"name": "Hudson valley", "code":"hudsonvalley"},
                {"name": "Ithaca", "code": "ithaca"},
                {"name": "Long island", "code": "longisland"},
                {"name": "New york city", "code": "newyork"},
                {"name": "Oneonta", "code":"oneonta"},
                {"name": "Plattsburgh-adirondacks", "code":"plattsburgh"},
                {"name": "Potsdam-canton-massena", "code":"potsdam"},
                {"name": "Rochester", "code":"rochester"},
                {"name": "Syracuse", "code":"syracuse"},
                {"name": "Twin tiers NY/PA", "code":"twintiers"},
                {"name": "Utica-rome-oneida", "code":"utica"},
                {"name": "Watertown", "code":"watertown"},
        ]
    },
    { "New hampshire" : [
        {"name":"New Hampshire", "code":"nh"}
        ]
    },
    { "North Dakota" : [
            {"name":"Bismarck", "code": "bismarck"},
            {"name":"Fargo / moorhead", "code": "fargo"},
            {"name":"Grand forks", "code": "grandforks"},
            {"name":"North dakota", "code": "nd"},
        ]
    },
    { "Ohio" : [
            {"name": "Akron / canton", "code": "akroncanton"},
            {"name": "Ashtabula", "code": "ashtabula"},
            {"name": "Athens", "code": "athensohio"},
            {"name": "Chillicothe", "code": "chillicothe"},
            {"name": "Cincinnati", "code": "cincinnati"},
            {"name": "Cleveland", "code": "cleveland"},
            {"name": "Columbus", "code": "columbus"},
            {"name": "Dayton / springfield", "code": "dayton"},
            {"name": "Huntington-ashland", "code": "huntington"},
            {"name": "Lima / findlay", "code": "limaohio"},
            {"name": "Mansfield", "code": "mansfield"},
            {"name": "Northern panhandle", "code": "wheeling"},
            {"name": "Parkersburg-marietta", "code": "parkersburg"},
            {"name": "Sandusky", "code": "sandusky"},
            {"name": "Toledo", "code": "toledo"},
            {"name": "Tuscarawas co", "code": "tuscarawas"},
            {"name": "Youngstown", "code": "youngstown"},
            {"name": "Zanesville / cambridge", "code": "zanesville"},
        ]
    },
    { "Oklahoma" : [
                {"name":"Fort smith, AR", "code": "fortsmith"},
                {"name":"Lawton", "code": "lawton"},
                {"name":"Northwest OK", "code": "enid"},
                {"name":"Oklahoma city", "code": "oklahomacity"},
                {"name":"Stillwater", "code": "stillwater"},
                {"name":"Texoma", "code": "texoma"},
                {"name":"Tulsa", "code": "tulsa"},
        ]
    },
    { "Oregon" : [
                {"name":"Bend", "code": "bend"},
                {"name":"Corvallis/albany", "code": "corvallis"},
                {"name":"East oregon", "code": "eastoregon"},
                {"name":"Eugene", "code": "eugene"},
                {"name":"Klamath falls", "code": "klamath"},
                {"name":"Medford-ashland", "code": "medford"},
                {"name":"Oregon coast", "code": "oregoncoast"},
                {"name":"Portland", "code": "portland"},
                {"name":"Roseburg", "code": "roseburg"},
                {"name":"Salem", "code": "salem"},
        ]
    },
    { "Pennsylvania" : [
                {"name":"Altoona-johnstown", "code": "altoona"},
                {"name":"Cumberland valley", "code": "chambersburg"},
                {"name":"Erie", "code": "erie"},
                {"name":"Harrisburg", "code": "harrisburg"},
                {"name":"Lancaster", "code": "lancaster"},
                {"name":"Lehigh valley", "code": "allentown"},
                {"name":"Meadville", "code": "meadville"},
                {"name":"Philadelphia", "code": "philadelphia"},
                {"name":"Pittsburgh", "code": "pittsburgh"},
                {"name":"Poconos", "code": "poconos"},
                {"name":"Reading", "code": "reading"},
                {"name":"Scranton / wilkes-barre", "code": "scranton"},
                {"name":"State college", "code": "pennstate"},
                {"name":"Twin tiers NY/PA", "code": "twintiers"},
                {"name":"Williamsport", "code": "williamsport"},
                {"name":"York", "code": "york"}
        ]
    },
    { "Puerto Rico" : [
                {"name":"Puerto rico", "code": "puertorico"},
        ]
    },
    { "Rhode Island" : [
                {"name":"Rhode island", "code": "providence"},
        ]
    },
    { "South Carolina" : [
                {"name": "Charleston", "code": "charleston"},
                {"name": "Columbia", "code": "columbia"},
                {"name": "Florence", "code": "florencesc"},
                {"name": "Greenville / upstate", "code": "greenville"},
                {"name": "Hilton head", "code": "hiltonhead"},
                {"name": "Myrtle beach", "code": "myrtlebeach"},
        ]
    },
    { "South Carolina" : [
            {"name": "Northeast SD", "code": "nesd"},
            {"name": "Pierre / central SD", "code": "csd"},
            {"name": "Rapid city / west SD", "code": "rapidcity"},
            {"name": "Sioux falls / SE SD", "code": "siouxfalls"},
            {"name": "South dakota", "code": "sd"},
        ]
    },
    { "Tennessee" : [
                {"name": "Chattanooga", "code": "chattanooga"},
                {"name": "Clarksville", "code": "clarksville"},
                {"name": "Cookeville", "code": "cookeville"},
                {"name": "Jackson", "code": "jacksontn"},
                {"name": "Knoxville", "code": "knoxville"},
                {"name": "Memphis", "code": "memphis"},
                {"name": "Nashville", "code": "nashville"},
                {"name": "Tri-cities", "code": "tricities"},
        ]
    },
    { "Texas" : [
                {"name": "Abilene", "code": "abilene"},
                {"name": "Amarillo", "code": "amarillo"},
                {"name": "Austin", "code": "austin"},
                {"name": "Beaumont / port arthur", "code": "beaumont"},
                {"name": "Brownsville", "code": "brownsville"},
                {"name": "College station", "code": "collegestation"},
                {"name": "Corpus christi", "code": "corpuschristi"},
                {"name": "Dallas / fort worth", "code": "dallas"},
                {"name": "Deep east texas", "code": "nacogdoches"},
                {"name": "Del rio / eagle pass", "code": "delrio"},
                {"name": "El paso", "code": "elpaso"},
                {"name": "Galveston", "code": "galveston"},
                {"name": "Houston", "code": "houston"},
                {"name": "Killeen / temple / ft hood", "code": "killeen"},
                {"name": "Laredo", "code": "laredo"},
                {"name": "Lubbock", "code": "lubbock"},
                {"name": "Mcallen / edinburg", "code": "mcallen"},
                {"name": "Odessa / midland", "code": "odessa"},
                {"name": "San angelo", "code": "odessa"},
                {"name": "San antonio", "code": "sanangelo"},
                {"name": "San marcos", "code": "sanmarcos"},
                {"name": "Southwest TX", "code": "bigbend"},
                {"name": "Texarkana", "code": "texoma"},
                {"name": "Texoma", "code": "easttexas"},
                {"name": "Tyler / east TX", "code": "easttexas"},
                {"name": "Victoria", "code": "victoriatx"},
                {"name": "Waco", "code": "waco"},
                {"name": "Wichita falls", "code": "wichitafalls"},
        ]
    },
    { "Utah" : [
                {"name": "Logan", "code": "logan"},
                {"name": "Ogden-clearfield", "code": "ogden"},
                {"name": "Provo / orem", "code": "provo"},
                {"name": "Salt lake city", "code": "saltlakecity"},
                {"name": "St george", "code": "stgeorge"},
        ]
    },
    { "Vermont" : [
        {"name": "Vermont", "code":"vermont"}
        ]
    },
    { "Vermont" : [
                {"name": "Charlottesville", "code": "charlottesville"},
                {"name": "Danville", "code": "danville"},
                {"name": "Eastern shore", "code": "easternshore"},
                {"name": "Fredericksburg", "code": "fredericksburg"},
                {"name": "Harrisonburg", "code": "harrisonburg"},
                {"name": "Lynchburg", "code": "lynchburg"},
                {"name": "New river valley - blacksburg, christiansburg, radford, etc", "code": "blacksburg"},
                {"name": "Norfolk / hampton roads", "code": "norfolk"},
                {"name": "Richmond", "code": "richmond"},
                {"name": "Roanoke", "code": "roanoke"},
                {"name": "Southwest VA", "code": "swva"},
                {"name": "Winchester", "code": "winchester"},
        ]
    },
    { "Washington" : [
                {"name": "Bellingham", "code": "bellingham"},
                {"name": "Kennewick-pasco-richland", "code": "kpr"},
                {"name": "Lewiston / clarkston", "code": "lewiston"},
                {"name": "Moses lake", "code": "moseslake"},
                {"name": "Olympic peninsula", "code": "olympic"},
                {"name": "Pullman / moscow", "code": "pullman"},
                {"name": "Seattle-tacoma", "code": "seattle"},
                {"name": "Skagit / island / SJI", "code": "skagit"},
                {"name": "Spokane / coeur d'alene", "code": "spokane"},
                {"name": "Wenatchee", "code": "wenatchee"},
                {"name": "Yakima", "code": "yakima"},
                {"name": "Clark co / SW WA (subregion of PDX site)", "code": ""},
        ]
    },
    { "West Virginia" : [
                {"name": "Charleston", "code": "charlestonwv"},
                {"name": "Eastern panhandle", "code": "martinsburg"},
                {"name": "Huntington-ashland", "code": "huntington"},
                {"name": "Morgantown", "code": "morgantown"},
                {"name": "Northern panhandle", "code": "wheeling"},
                {"name": "Parkersburg-marietta", "code": "parkersburg"},
                {"name": "Southern WV", "code": "swv"},
                {"name": "West virginia (old)", "code": "wv"},
        ]
    },
    { "Wisconsin" : [
                {"name": "Appleton-oshkosh-FDL", "code": "appleton"},
                {"name": "Duluth / superior", "code": "duluth"},
                {"name": "Eau claire", "code": "eauclaire"},
                {"name": "Green bay", "code": "greenbay"},
                {"name": "Janesville", "code": "janesville"},
                {"name": "Kenosha-racine", "code": "racine"},
                {"name": "La crosse", "code": "lacrosse"},
                {"name": "Madison", "code": "madison"},
                {"name": "Milwaukee", "code": "milwaukee"},
                {"name": "Northern WI", "code": "northernwi"},
                {"name": "Sheboygan", "code": "sheboygan"},
                {"name": "Wausau", "code": "wausau"},
        ]
    },   
    { 
        "Wyoming" : [ {"name": "Wyoming", "code": "wyoming"} ] 
    },  
]


sales_types = [
    {"name":"antiques", "code": ["ata", "atq", "atd"]},
    {"name":"appliances", "code": ["ppa", "app", "ppd"]},
    {"name":"arts & crafts", "code": ["ara", "art", "ard"]},
    {"name":"atvs, utvs, snowmobiles", "code": ["sna", "snw", "snd"]},
    {"name":"auto parts", "code": ["pta", "pts", "ptd"]},
    {"name":"auto wheels & tires", "code": ["wta", "wto", "wtd"]},
    {"name":"aviation", "code": ["ava", "avo", "avd"]},
    {"name":"baby & kid stuff", "code": ["baa", "bab", "bad"]},
    {"name":"barter", "code": ["bar", "bar", "bar"]},
    {"name":"bicycle parts", "code": ["bip", "bop", "bdp"]},
    {"name":"bicycles", "code": ["bia", "bik", "bid"]},
    {"name":"boat parts & accessories", "code": ["bpa", "bpo", "bpd"]},
    {"name":"boats", "code": ["boo", "boa", "bod"]},
    {"name":"books & magazines", "code": ["bka", "bks", "bkd"]},
    {"name":"business", "code": ["bfa", "bfs", "bfd"]},
    {"name":"cars & trucks", "code": ["cta", "cto", "ctd"]},
    {"name":"cds / dvds / vhs", "code": ["ema", "emd", "emq"]},
    {"name":"cell phones", "code": ["moa", "mob", "mod"]},
    {"name":"clothing & accessories", "code": ["cla", "clo", "cld"]},
    {"name":"collectibles", "code": ["cba", "clt", "cbd"]},
    {"name":"computer parts", "code": ["cbd", "sop", "sdp"]},
    {"name":"computers", "code": ["sya", "sys", "syd"]},
    {"name":"electronics", "code": ["ela", "ele", "eld"]},
    {"name":"farm & garden", "code": ["gra", "grd", "grq"]},
    {"name":"free stuff", "code": ["zip", "zip", "zip"]},
    {"name":"furniture", "code": ["fua", "fuo", "fud"]},
    {"name":"general for sale", "code": ["foa", "for", "fod"]},
    {"name":"health and beauty", "code": ["haa", "hab", "had"]},
    {"name":"heavy equipment", "code": ["hva", "hvo", "hvd"]},
    {"name":"household items", "code": ["hsa", "hsh", "hsd"]},
    {"name":"jewelry", "code": ["jwa", "jwl", "jwd"]},
    {"name":"materials", "code": ["maa", "mat", "mad"]},
    {"name":"motorcycle parts & accessories", "code": ["mpa", "mpo", "mpd"]},
    {"name":"motorcycles/scooters", "code": ["mca", "mcy", "mcd"]},
    {"name":"musical instruments", "code": ["msa", "msg", "msd"]},
    {"name":"photo/video", "code": ["pha", "pho", "phd"]},
    {"name":"recreational vehicles", "code": ["rva", "rvs", "rvd"]},
    {"name":"sporting goods", "code": ["sga", "spo", "sgd"]},
    {"name":"tools", "code": ["tla", "tls", "tld"]},
    {"name":"toys & games", "code": ["taa", "tag", "tad"]},
    {"name":"trailers", "code": ["tra", "tro", "trb"]},
    {"name":"video gaming", "code": ["vga", "vgm", "vgd"]},
    {"name":"wanted", "code": ["waa", "wan", "wad"]}
]

