import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface ISalesType { name: String, types: String[] }

export interface ICities {
  "": { name: String; code:String }[]
}

@Injectable({
  providedIn: 'root'
})
export class CraiglistService {

  constructor(
    private _http:HttpClient
  ) { }

  get_sales_types(){
    return this._http.get<ISalesType[]>('http://192.168.1.68:4444/craiglist/get_sales')
  }

  get_states_and_cities(){
    return this._http.get<ICities[]>('http://192.168.1.68:4444/craiglist/get_cities')
  }
}



