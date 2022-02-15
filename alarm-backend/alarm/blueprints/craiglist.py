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
    { "Arizona":[
                    {"name":"flagstaff / sedona", "code":"flagstaff"},
                    {"name":"mohave county", "code":"mohave"},
                    {"name":"phoenix", "code":"phoenix"},
                    {"name":"prescott", "code":"prescott"},
                    {"name":"show low", "code":"showlow"},
                    {"name":"sierra vista", "code":"sierravista"},
                    {"name":"tucson", "code":"tucson"},
                    {"name":"yuma", "code":"yuma"}
                ]
    },
    { "Arkansas": [
                    {"name":"fayetteville", "code": "fayar"},
                    {"name":"fort smith", "code": "fortsmith"},
                    {"name":"jonesboro", "code": "jonesboro"},
                    {"name":"little rock", "code": "littlerock"},
                    {"name":"memphis, TN", "code": "memphis"},
                    {"name":"texarkana", "code": "texarkana"}
                    ]
    },
    { "California": [
                    {"name":"bakersfield","code":"bakersfield"},
                    {"name":"chico","code":"chico"},
                    {"name":"fresno / madera","code":"fresno"},
                    {"name":"gold country","code":"goldcountry"},
                    {"name":"hanford-corcoran","code":"hanford"},
                    {"name":"humboldt county","code":"humboldt"},
                    {"name":"imperial county","code":"imperial"},
                    {"name":"inland empire - riverside and san bernardino counties","code":"inlandempire"},
                    {"name":"los angeles","code":"losangeles"},
                    {"name":"mendocino county","code":"mendocino"},
                    {"name":"merced","code":"merced"},
                    {"name":"modesto","code":"modesto"},
                    {"name":"monterey bay","code":"monterey"},
                    {"name":"orange county","code":"orangecounty"},
                    {"name":"palm springs","code":"palmsprings"},
                    {"name":"redding","code":"redding"},
                    {"name":"reno / tahoe","code":"reno"},
                    {"name":"sacramento","code":"sacramento"},
                    {"name":"san diego","code":"sandiego"},
                    {"name":"san luis obispo","code":"slo"},
                    {"name":"santa barbara","code":"santabarbara"},
                    {"name":"santa maria","code":"santamaria"},
                    {"name":"SF bay area","code":"sfbay"},
                    {"name":"siskiyou county","code":"siskiyou"},
                    {"name":"stockton","code":"stockton"},
                    {"name":"susanville","code":"susanville"},
                    {"name":"ventura county","code":"ventura"},
                    {"name":"visalia-tulare","code":"visalia"},
                    {"name":"yuba-sutter","code":"yubasutter"}
        ]
    },
    { "Colorado" : [
                    {"name":"boulder","code":"boulder"},
                    {"name":"colorado springs","code":"cosprings"},
                    {"name":"denver","code":"denver"},
                    {"name":"eastern CO","code":"eastco"},
                    {"name":"fort collins / north CO","code":"fortcollins"},
                    {"name":"high rockies","code":"rockies"},
                    {"name":"pueblo","code":"pueblo"},
                    {"name":"western slope","code":"westslope"},
            ]
    },
    { "Connecticut" : [
                {"name":"eastern CT","code":"newlondon"},
                {"name":"hartford","code":"hartford"},
                {"name":"new haven","code":"newhaven"},
                {"name":"northwest CT","code":"nwct"},

        ]
    },
    { "DC" : [
                {"name":"washington, DC","code":"washingtondc"},
                {"name":"hartford","code":"hartford"},
                {"name":"new haven","code":"newhaven"},
                {"name":"northwest CT","code":"nwct"},

        ]
    },
    { "Delaware" : [
                {"name":"Delaware","code":"delaware"},
        ]
    },
    { "Florida" : [
                {"name":"daytona beach","code":"daytona"},
                {"name":"florida keys","code":"keys"},
                {"name":"ft myers / SW florida","code":"fortmyers"},
                {"name":"gainesville","code":"gainesville"},
                {"name":"heartland florida","code":"cfl"},
                {"name":"jacksonville","code":"jacksonville"},
                {"name":"lakeland","code":"lakeland"},
                {"name":"north central FL","code":"lakecity"},
                {"name":"ocala FL","code":"ocala"},
                {"name":"okaloosa / walton","code":"okaloosa"},
                {"name":"panama city / walton","code":"panamacity"},
                {"name":"pensacola","code":"pensacola"},
                {"name":"sarasota-bradenton","code":"sarasota"},
                {"name":"south florida - includes separate sections for miami/dade, broward, and palm beach counties","code":"miami"},
                {"name":"space coast","code":"spacecoast"},
                {"name":"st augustine","code":"staugustine"},
                {"name":"tallahassee","code":"tallahassee"},
                {"name":"tampa bay area","code":"tampa"},
                {"name":"treasure coast","code":"treasure"},

        ]
    },
    { "Georgia" : [
                {"name":"albany","code":"albanyga"},
                {"name":"athens","code":"athensga"},
                {"name":"atlanta","code":"atlanta"},
                {"name":"augusta","code":"augusta"},
                {"name":"brunswick","code":"brunswick"},
                {"name":"columbus","code":"columbusga"},
                {"name":"macon / warner robins","code":"macon"},
                {"name":"northwest GA","code":"nwga"},
                {"name":"savannah / hinesville","code":"savannah"},
                {"name":"statesboro","code":"statesboro"},
                {"name":"valdosta","code":"valdosta"},
        ]
    },
    { "Guam-Micronesia" : [
                {"name":"guam-micronesia","code":"micronesia"},
        ]
    },
    { "Hawaii" : [
                {"name":"hawaii","code":"honolulu"},
        ]
    },
    { "Idaho" : [
                {"name":"boise","code":"boise"},
                {"name":"east idaho","code":"eastidaho"},
                {"name":"lewiston / clarkston","code":"lewiston"},
                {"name":"pullman / moscow / clarkston","code":"pullman"},
                {"name":"spokane / coeur d'alene","code":"spokane"},
                {"name":"twin falls","code":"twinfalls"},
        ]
    },
    { "Illinois" : [
                {"name":"bloomington-normal","code":"bn"},
                {"name":"champaign urbana","code":"chambana"},
                {"name":"chicago","code":"chicago"},
                {"name":"decatur","code":"decatur"},
                {"name":"la salle co","code":"lasalle"},
                {"name":"mattoon-charleston","code":"mattoon"},
                {"name":"peoria","code":"peoria"},
                {"name":"quad cities, IA/IL","code":"quadcities"},
                {"name":"rockford, IA/IL","code":"rockford"},
                {"name":"southern illinois, IA/IL","code":"carbondale"},
                {"name":"springfield, IA/IL","code":"springfieldil"},
                {"name":"st louis, MO","code":"stlouis"},
                {"name":"st western IL","code":"quincy"},
        ]
    },  
    { "Indiana" : [
                {"name":"bloomington","code":"bloomington"},
                {"name":"evansville","code":"evansville"},
                {"name":"fort wayne","code":"fortwayne"},
                {"name":"indianapolis","code":"indianapolis"},
                {"name":"kokomo","code":"kokomo"},
                {"name":"lafayette / west lafayette","code":"tippecanoe"},
                {"name":"muncie / anderson","code":"muncie"},
                {"name":"richmond","code":"richmondin"},
                {"name":"south bend / michiana","code":"southbend"},
                {"name":"terre haute","code":"terrehaute"},
        ]
    },
    { "Iowa" : [
                {"name":"ames","code":"ames"},
                {"name":"cedar rapids","code":"cedarrapids"},
                {"name":"des moines","code":"desmoines"},
                {"name":"dubuque","code":"dubuque"},
                {"name":"fort dodge","code":"fortdodge"},
                {"name":"iowa city","code":"iowacity"},
                {"name":"mason city","code":"masoncity"},
                {"name":"omaha / council bluffs","code":"omaha"},
                {"name":"quad cities, IA/IL","code":"quadcities"},
                {"name":"sioux city","code":"siouxcity"},
                {"name":"southeast IA","code":"ottumwa"},
                {"name":"waterloo / cedar falls","code":"waterloo"},
        ]
    },
    { "Kansas" : [
                {"name":"kansas city, MO","code":"kansascity"},
                {"name":"lawrence, MO","code":"lawrence"},
                {"name":"manhattan","code":"ksu"},
                {"name":"northwest KS","code":"nwks"},
                {"name":"salina","code":"salina"},
                {"name":"southeast KS","code":"seks"},
                {"name":"southwest KS","code":"swks"},
                {"name":"topeka KS","code":"swks"},
                {"name":"topeka","code":"topeka"},
                {"name":"wichita","code":"wichita"},
        ]
    },
    { "Kentucky" : [
                {"name":"bowling green","code":"bgky"},
                {"name":"cincinnati, OH","code":"cincinnati"},
                {"name":"eastern kentucky, OH","code":"eastky"},
                {"name":"huntington-ashland, OH","code":"huntington"},
                {"name":"lexington, OH","code":"lexington"},
                {"name":"louisville","code":"louisville"},
                {"name":"owensboro","code":"owensboro"},
                {"name":"western KY","code":"westky"},

        ]
    },
    { "Louisiana" : [
                {"mame":"baton rouge", "code":"batonrouge"},
                {"mame":"central louisiana", "code":"cenla"},
                {"mame":"houma", "code":"houma"},
                {"mame":"lafayette", "code":"lafayette"},
                {"mame":"lake charles", "code":"lakecharles"},
                {"mame":"monroe", "code":"monroe"},
                {"mame":"new orleans", "code":"neworleans"},
                {"mame":"shreveport", "code":"shreveport"},
        ]
    },
    { "Maine" : [
                {"mame":"maine", "code":"maine"},
        ]
    },
    { "Maryland" : [
                {"name":"annapolis", "code": "annapolis"},
                {"name":"baltimore", "code": "baltimore"},
                {"name":"cumberland valley", "code": "baltimore"},
                {"name":"eastern shore", "code": "easternshore"},
                {"name":"frederick", "code": "frederick"},
                {"name":"southern maryland", "code": "southern maryland"},
                {"name":"western maryland", "code": "westmd"},
        ]
    },
    { "Massachusetts" : [
                {"name":"boston - includes merrimack valley, metro west, north shore, south shore", "code": "boston"},
                {"name":"cape cod / islands", "code": "capecod"},
                {"name":"south coast - southern bristol and plymouth counties", "code": "southcoast"},
                {"name":"western massachusetts", "code": "westernmass"},
                {"name":"worcester / central MA", "code": "worcester"},
        ]
    },
    { "Michigan" : [
                {"name":"ann arbor", "code": "annarbor"},
                {"name":"battle creek", "code": "battlecreek"},
                {"name":"central michigan", "code": "centralmich"},
                {"name":"detroit metro", "code": "detroit"},
                {"name":"flint", "code": "flint"},
                {"name":"grand rapids", "code": "grandrapids"},
                {"name":"holland", "code": "holland"},
                {"name":"jackson", "code": "jxn"},
                {"name":"kalamazoo", "code": "kalamazoo"},
                {"name":"lansing", "code": "lansing"},
                {"name":"monroe", "code": "monroemi"},
                {"name":"muskegon", "code": "muskegon"},
                {"name":"northern michigan", "code": "nmi"},
                {"name":"port huron", "code": "porthuron"},
                {"name":"saginaw-midland-baycity", "code": "saginaw"},
                {"name":"south bend / michiana", "code": "southbend"},
                {"name":"southwest michigan", "code": "swmi"},
                {"name":"the thumb", "code": "thumb"},
                {"name":"upper peninsula", "code": "up"},
        ]
    },
    { "Minnesota" : [
                {"name":"bemidji", "code": "bemidji"},
                {"name":"brainerd", "code": "brainerd"},
                {"name":"duluth / superior", "code": "duluth"},
                {"name":"fargo / moorhead", "code": "fargo"},
                {"name":"mankato", "code": "mankato"},
                {"name":"minneapolis / st paul", "code": "minneapolis"},
                {"name":"rochester", "code": "rmn"},
                {"name":"southwest MN", "code": "marshall"},
                {"name":"st cloud", "code": "stcloud"},
        ]
    },
    { "Mississippi" : [
                {"name":"gulfport / biloxi", "code": "gulfport"},
                {"name":"hattiesburg", "code": "hattiesburg"},
                {"name":"jackson", "code": "jackson"},
                {"name":"memphis, TN", "code": "memphis"},
                {"name":"meridian", "code": "meridian"},
                {"name":"north mississippi", "code": "northmiss"},
                {"name":"southwest MS", "code": "natchez"},
        ]
    },
    { "Missouri" : [
                {"name":"columbia / jeff city", "code":"columbiamo"},
                {"name":"joplin", "code":"joplin"},
                {"name":"kansas city", "code":"kansascity"},
                {"name":"kirksville", "code":"kirksville"},
                {"name":"lake of the ozarks", "code":"loz"},
                {"name":"southeast missouri", "code":"semo"},
                {"name":"springfield", "code":"springfield"},
                {"name":"st joseph", "code":"stjoseph"},
                {"name":"st louis", "code":"stlouis"}
        ]
    },
    { "Montana" : [
                {"name":"billings", "code":"billings"},
                {"name":"bozeman", "code":"bozeman"},
                {"name":"butte", "code":"butte"},
                {"name":"eastern montana", "code":"montana"},
                {"name":"great falls", "code":"greatfalls"},
                {"name":"helena", "code":"helena"},
                {"name":"kalispell", "code":"kalispell"},
                {"name":"missoula", "code":"missoula"},
        ]
    },  
    { "North Carolina" : [
                {"name":"asheville", "code": "asheville"},
                {"name":"boone", "code": "boone"},
                {"name":"charlotte", "code": "charlotte"},
                {"name":"eastern NC", "code": "eastnc"},
                {"name":"fayetteville", "code": "fayetteville"},
                {"name":"greensboro", "code": "greensboro"},
                {"name":"hickory / lenoir", "code": "hickory"},
                {"name":"jacksonville", "code": "onslow"},
                {"name":"outer banks", "code": "outerbanks"},
                {"name":"raleigh / durham / CH", "code": "raleigh"},
                {"name":"wilmington", "code": "wilmington"},
                {"name":"winston-salem", "code": "winstonsalem"},
        ]
    },
    { "Nebraska" : [
                {"name":"grand island", "code": "grandisland"},
                {"name":"lincoln", "code": "lincoln"},
                {"name":"north platte", "code": "northplatte"},
                {"name":"omaha / council bluffs", "code": "omaha"},
                {"name":"scottsbluff / panhandle", "code": "scottsbluff"},
                {"name":"sioux city, IA", "code": "siouxcity"},
        ]
    },
    { "Nevada" : [
                {"name":"elko", "code": "elko"},
                {"name":"las vegas", "code": "lasvegas"},
                {"name":"reno / tahoe", "code": "reno"},
        ]
    },
    { "New Jersey" : [
                {"name":"central NJ", "code":"cnj"},
                {"name":"jersey shore", "code":"jerseyshore"},
                {"name":"north jersey", "code":"newjersey"},
                {"name":"south jersey", "code":"southjersey"},
        ]
    },  
    { "New Mexico" : [
                {"name":"albuquerque", "code":"albuquerque"},
                {"name":"clovis / portales", "code":"clovis"},
                {"name":"farmington", "code":"farmington"},
                {"name":"las cruces", "code":"lascruces"},
                {"name":"roswell / carlsbad", "code":"roswell"},
                {"name":"santa fe / taos", "code":"santafe"},
        ]
    },
    { "New York" : [
                {"name": "albany", "code":"albany"},
                {"name": "binghamton", "code":"binghamton"},
                {"name": "buffalo", "code":"buffalo"},
                {"name": "catskills", "code":"catskills"},
                {"name": "chautauqua", "code":"chautauqua"},
                {"name": "elmira-corning", "code":"elmira"},
                {"name": "finger lakes", "code":"fingerlakes"},
                {"name": "glens falls", "code":"glensfalls"},
                {"name": "hudson valley", "code":"hudsonvalley"},
                {"name": "ithaca", "code": "ithaca"},
                {"name": "long island", "code": "longisland"},
                {"name": "new york city", "code": "newyork"},
                {"name": "oneonta", "code":"oneonta"},
                {"name": "plattsburgh-adirondacks", "code":"plattsburgh"},
                {"name": "potsdam-canton-massena", "code":"potsdam"},
                {"name": "rochester", "code":"rochester"},
                {"name": "syracuse", "code":"syracuse"},
                {"name": "twin tiers NY/PA", "code":"twintiers"},
                {"name": "utica-rome-oneida", "code":"utica"},
                {"name": "watertown", "code":"watertown"},
        ]
    },
    { "New hampshire" : [
        {"name":"New Hampshire", "code":"nh"}
        ]
    },
    { "North Dakota" : [
            {"name":"bismarck", "code": "bismarck"},
            {"name":"fargo / moorhead", "code": "fargo"},
            {"name":"grand forks", "code": "grandforks"},
            {"name":"north dakota", "code": "nd"},
        ]
    },
    { "Ohio" : [
            {"name": "akron / canton", "code": "akroncanton"},
            {"name": "ashtabula", "code": "ashtabula"},
            {"name": "athens", "code": "athensohio"},
            {"name": "chillicothe", "code": "chillicothe"},
            {"name": "cincinnati", "code": "cincinnati"},
            {"name": "cleveland", "code": "cleveland"},
            {"name": "columbus", "code": "columbus"},
            {"name": "dayton / springfield", "code": "dayton"},
            {"name": "huntington-ashland", "code": "huntington"},
            {"name": "lima / findlay", "code": "limaohio"},
            {"name": "mansfield", "code": "mansfield"},
            {"name": "northern panhandle", "code": "wheeling"},
            {"name": "parkersburg-marietta", "code": "parkersburg"},
            {"name": "sandusky", "code": "sandusky"},
            {"name": "toledo", "code": "toledo"},
            {"name": "tuscarawas co", "code": "tuscarawas"},
            {"name": "youngstown", "code": "youngstown"},
            {"name": "zanesville / cambridge", "code": "zanesville"},
        ]
    },
    { "Oklahoma" : [
                {"name":"fort smith, AR", "code": "fortsmith"},
                {"name":"lawton", "code": "lawton"},
                {"name":"northwest OK", "code": "enid"},
                {"name":"oklahoma city", "code": "oklahomacity"},
                {"name":"stillwater", "code": "stillwater"},
                {"name":"texoma", "code": "texoma"},
                {"name":"tulsa", "code": "tulsa"},
        ]
    },
    { "Oregon" : [
                {"name":"bend", "code": "bend"},
                {"name":"corvallis/albany", "code": "corvallis"},
                {"name":"east oregon", "code": "eastoregon"},
                {"name":"eugene", "code": "eugene"},
                {"name":"klamath falls", "code": "klamath"},
                {"name":"medford-ashland", "code": "medford"},
                {"name":"oregon coast", "code": "oregoncoast"},
                {"name":"portland", "code": "portland"},
                {"name":"roseburg", "code": "roseburg"},
                {"name":"salem", "code": "salem"},
        ]
    },
    { "Pennsylvania" : [
                {"name":"altoona-johnstown", "code": "altoona"},
                {"name":"cumberland valley", "code": "chambersburg"},
                {"name":"erie", "code": "erie"},
                {"name":"harrisburg", "code": "harrisburg"},
                {"name":"lancaster", "code": "lancaster"},
                {"name":"lehigh valley", "code": "allentown"},
                {"name":"meadville", "code": "meadville"},
                {"name":"philadelphia", "code": "philadelphia"},
                {"name":"pittsburgh", "code": "pittsburgh"},
                {"name":"poconos", "code": "poconos"},
                {"name":"reading", "code": "reading"},
                {"name":"scranton / wilkes-barre", "code": "scranton"},
                {"name":"state college", "code": "pennstate"},
                {"name":"twin tiers NY/PA", "code": "twintiers"},
                {"name":"williamsport", "code": "williamsport"},
                {"name":"york", "code": "york"}
        ]
    },
    { "Puerto Rico" : [
                {"name":"puerto rico", "code": "puertorico"},
        ]
    },
    { "Rhode Island" : [
                {"name":"rhode island", "code": "providence"},
        ]
    },
    { "South Carolina" : [
                {"name": "charleston", "code": "charleston"},
                {"name": "columbia", "code": "columbia"},
                {"name": "florence", "code": "florencesc"},
                {"name": "greenville / upstate", "code": "greenville"},
                {"name": "hilton head", "code": "hiltonhead"},
                {"name": "myrtle beach", "code": "myrtlebeach"},
        ]
    },
    { "South Carolina" : [
            {"name": "northeast SD", "code": "nesd"},
            {"name": "pierre / central SD", "code": "csd"},
            {"name": "rapid city / west SD", "code": "rapidcity"},
            {"name": "sioux falls / SE SD", "code": "siouxfalls"},
            {"name": "south dakota", "code": "sd"},
        ]
    },
    { "Tennessee" : [
                {"name": "chattanooga", "code": "chattanooga"},
                {"name": "clarksville", "code": "clarksville"},
                {"name": "cookeville", "code": "cookeville"},
                {"name": "jackson", "code": "jacksontn"},
                {"name": "knoxville", "code": "knoxville"},
                {"name": "memphis", "code": "memphis"},
                {"name": "nashville", "code": "nashville"},
                {"name": "tri-cities", "code": "tricities"},
        ]
    },
    { "Texas" : [
                {"name": "abilene", "code": "abilene"},
                {"name": "amarillo", "code": "amarillo"},
                {"name": "austin", "code": "austin"},
                {"name": "beaumont / port arthur", "code": "beaumont"},
                {"name": "brownsville", "code": "brownsville"},
                {"name": "college station", "code": "collegestation"},
                {"name": "corpus christi", "code": "corpuschristi"},
                {"name": "dallas / fort worth", "code": "dallas"},
                {"name": "deep east texas", "code": "nacogdoches"},
                {"name": "del rio / eagle pass", "code": "delrio"},
                {"name": "el paso", "code": "elpaso"},
                {"name": "galveston", "code": "galveston"},
                {"name": "houston", "code": "houston"},
                {"name": "killeen / temple / ft hood", "code": "killeen"},
                {"name": "laredo", "code": "laredo"},
                {"name": "lubbock", "code": "lubbock"},
                {"name": "mcallen / edinburg", "code": "mcallen"},
                {"name": "odessa / midland", "code": "odessa"},
                {"name": "san angelo", "code": "odessa"},
                {"name": "san antonio", "code": "sanangelo"},
                {"name": "san marcos", "code": "sanmarcos"},
                {"name": "southwest TX", "code": "bigbend"},
                {"name": "texarkana", "code": "texoma"},
                {"name": "texoma", "code": "easttexas"},
                {"name": "tyler / east TX", "code": "easttexas"},
                {"name": "victoria", "code": "victoriatx"},
                {"name": "waco", "code": "waco"},
                {"name": "wichita falls", "code": "wichitafalls"},
        ]
    },
    { "Utah" : [
                {"name": "logan", "code": "logan"},
                {"name": "ogden-clearfield", "code": "ogden"},
                {"name": "provo / orem", "code": "provo"},
                {"name": "salt lake city", "code": "saltlakecity"},
                {"name": "st george", "code": "stgeorge"},
        ]
    },
    { "Vermont" : [
        {"name": "Vermont", "code":"vermont"}
        ]
    },
    { "Vermont" : [
                {"name": "charlottesville", "code": "charlottesville"},
                {"name": "danville", "code": "danville"},
                {"name": "eastern shore", "code": "easternshore"},
                {"name": "fredericksburg", "code": "fredericksburg"},
                {"name": "harrisonburg", "code": "harrisonburg"},
                {"name": "lynchburg", "code": "lynchburg"},
                {"name": "new river valley - blacksburg, christiansburg, radford, etc", "code": "blacksburg"},
                {"name": "norfolk / hampton roads", "code": "norfolk"},
                {"name": "richmond", "code": "richmond"},
                {"name": "roanoke", "code": "roanoke"},
                {"name": "southwest VA", "code": "swva"},
                {"name": "winchester", "code": "winchester"},
        ]
    },
    { "Washington" : [
                {"name": "bellingham", "code": "bellingham"},
                {"name": "kennewick-pasco-richland", "code": "kpr"},
                {"name": "lewiston / clarkston", "code": "lewiston"},
                {"name": "moses lake", "code": "moseslake"},
                {"name": "olympic peninsula", "code": "olympic"},
                {"name": "pullman / moscow", "code": "pullman"},
                {"name": "seattle-tacoma", "code": "seattle"},
                {"name": "skagit / island / SJI", "code": "skagit"},
                {"name": "spokane / coeur d'alene", "code": "spokane"},
                {"name": "wenatchee", "code": "wenatchee"},
                {"name": "yakima", "code": "yakima"},
                {"name": "clark co / SW WA (subregion of PDX site)", "code": ""},
        ]
    },
    { "West Virginia" : [
                {"name": "charleston", "code": "charlestonwv"},
                {"name": "eastern panhandle", "code": "martinsburg"},
                {"name": "huntington-ashland", "code": "huntington"},
                {"name": "morgantown", "code": "morgantown"},
                {"name": "northern panhandle", "code": "wheeling"},
                {"name": "parkersburg-marietta", "code": "parkersburg"},
                {"name": "southern WV", "code": "swv"},
                {"name": "west virginia (old)", "code": "wv"},
        ]
    },
    { "Wisconsin" : [
                {"name": "appleton-oshkosh-FDL", "code": "appleton"},
                {"name": "duluth / superior", "code": "duluth"},
                {"name": "eau claire", "code": "eauclaire"},
                {"name": "green bay", "code": "greenbay"},
                {"name": "janesville", "code": "janesville"},
                {"name": "kenosha-racine", "code": "racine"},
                {"name": "la crosse", "code": "lacrosse"},
                {"name": "madison", "code": "madison"},
                {"name": "milwaukee", "code": "milwaukee"},
                {"name": "northern WI", "code": "northernwi"},
                {"name": "sheboygan", "code": "sheboygan"},
                {"name": "wausau", "code": "wausau"},
        ]
    },   
    { "Wyoming" : [
        {"name": "wyoming", "code": "wyoming"}
        ]
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

