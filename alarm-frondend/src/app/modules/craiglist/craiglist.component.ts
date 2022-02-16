import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { CraiglistService, ICities } from 'src/app/services/craiglist.service';

@Component({
  selector: 'app-craiglist',
  templateUrl: './craiglist.component.html',
  styleUrls: ['./craiglist.component.scss']
})
export class CraiglistComponent implements OnInit {
@Output() close = new EventEmitter()
  constructor(
    private _craiglistSvc:CraiglistService
  ) { }

  // Api data
  states_and_cities:ICities[]=[]
  
  // State name list
  states:string[] = []
  
  // Selected state name
  selectedState = ""
  
  // Cities of selected state list
  citiesOfState:any

  // Sale types
  sale_types:any 

  searchParams = new URLSearchParams()
  craiglistURL=""
  builded_name=""

  // https://anchorage.craigslist.org/search/ata?query=mahmut+mahmutow&srchType=T

  craiglistFG = new FormGroup({
    query: new FormControl(null), 
    state: new FormControl(null),
    city: new FormControl(null),
    sale_type: new FormControl(null),
    sale_type_name: new FormControl(null),
    ownage: new FormControl(null),
    srchType: new FormControl(null),
    hasPic: new FormControl(null),
    postedToday: new FormControl(null),
    bundleDuplicates: new FormControl(null),
    searchNearby: new FormControl(null),
    postal: new FormControl(null),
    auto_make_model: new FormControl(null),
    min_price: new FormControl(null),
    max_price: new FormControl(null),
    search_distance: new FormControl(null),
    url: new FormControl(null),
    name: new FormControl(null),

  })

  stateChangeHandler(selectedState:any){
    // US states change handler
    this.selectedState = selectedState

    this.states_and_cities.forEach(stateAndCities =>{
      if (Object.keys(stateAndCities)[0] === this.selectedState){
        this.citiesOfState = Object.values(stateAndCities)[0]
      }
    })
    this.craiglistFG.get("city")?.reset()
  }

  create(){
    this.craiglistFG.get('url')?.setValue(this.craiglistURL)

    !this.craiglistFG.get('name')?.value ?  this.craiglistFG.get('name')?.setValue(this.builded_name) : null

    this._craiglistSvc.create(this.craiglistFG.value).subscribe({
      next: _ => {
        this._craiglistSvc.sync_list()
        this.close.emit()
      },
      error: e => console.log(e)
    })
  }

  updateURL(){
    // Update any changes for the link
    let url_base = `https://${this.craiglistFG.get('city')?.value}.craigslist.org/search/`
    let url_suffix =""

    const ownage = this.craiglistFG.get('ownage')?.value

    if (this.craiglistFG.get('ownage')?.value) {
      ownage === "all" ? url_suffix = this.craiglistFG.get('sale_type')?.value['code'][0] : null
      ownage === "owner" ? url_suffix = this.craiglistFG.get('sale_type')?.value['code'][1] : null
      ownage === "dealer" ? url_suffix = this.craiglistFG.get('sale_type')?.value['code'][2] : null
      this.craiglistURL = url_base + url_suffix+"?"+this.searchParams.toString()
    } else {
      this.craiglistURL = ""
    }
    // Auto generated name building (ugly!)
    this.builded_name = `At ${String(this.craiglistFG.get('city')?.value)}/${this.craiglistFG.get('state')?.value}, `
    this.builded_name = this.builded_name + `${this.craiglistFG.get('sale_type_name')?.value} from ${this.craiglistFG.get('ownage')?.value} sellers`

  }

  ngOnInit(): void {
    // Form listener 
    this.craiglistFG.valueChanges.subscribe(_ => this.updateURL())

    this._craiglistSvc.get_states_and_cities().subscribe(states_and_cities =>{
      // Getting state and cities
      this.states_and_cities = states_and_cities
      // Gathering only state names  
      for (let state of this.states_and_cities){
        this.states.push(Object.keys(state)[0])
      }
    })

    this._craiglistSvc.get_sales_types().subscribe(sales_types =>{
      // Getting sale types
      this.sale_types = sales_types
    })

    // Search parameters building

    this.craiglistFG.get('query')?.valueChanges.subscribe( res =>  {
      res ? this.searchParams.set("query", String(res) ): this.searchParams.delete("query")
    })

    this.craiglistFG.get('srchType')?.valueChanges.subscribe( res =>  {
      res ? this.searchParams.set("srchType","1"): this.searchParams.delete("srchType")
    })

    this.craiglistFG.get('hasPic')?.valueChanges.subscribe( res =>  {
      res ? this.searchParams.set("hasPic","1"): this.searchParams.delete("hasPic")
    })

    this.craiglistFG.get('postedToday')?.valueChanges.subscribe( res =>  {
      res ? this.searchParams.set("postedToday","1"): this.searchParams.delete("postedToday")
    })

    this.craiglistFG.get('bundleDuplicates')?.valueChanges.subscribe( res =>  {
      res ? this.searchParams.set("bundleDuplicates","1"): this.searchParams.delete("bundleDuplicates")
    })

    this.craiglistFG.get('searchNearby')?.valueChanges.subscribe( res =>  {
      res ? this.searchParams.set("searchNearby","1"): this.searchParams.delete("searchNearby")
    })

    this.craiglistFG.get('postal')?.valueChanges.subscribe( res =>  {
      res ? this.searchParams.set("postal",this.craiglistFG.get('postal')?.value): this.searchParams.delete("postal")
    })

    this.craiglistFG.get('auto_make_model')?.valueChanges.subscribe( res =>  {
      res ? this.searchParams.set("auto_make_model",this.craiglistFG.get('auto_make_model')?.value): this.searchParams.delete("auto_make_model")
    })

    this.craiglistFG.get('min_price')?.valueChanges.subscribe( res =>  {
      res ? this.searchParams.set("min_price",this.craiglistFG.get('min_price')?.value): this.searchParams.delete("min_price")
    })

    this.craiglistFG.get('max_price')?.valueChanges.subscribe( res =>  {
      res ? this.searchParams.set("max_price",this.craiglistFG.get('max_price')?.value): this.searchParams.delete("max_price")
    })

    this.craiglistFG.get('search_distance')?.valueChanges.subscribe( res =>  {
      res ? this.searchParams.set("search_distance",this.craiglistFG.get('search_distance')?.value): this.searchParams.delete("search_distance")
    })
  }

}
