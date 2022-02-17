import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { BehaviorSubject } from 'rxjs';

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
  ) { 
    this.apiUrl = environment.apiUrl
  }

  apiUrl:string = ""

  craiglist_alarmsBS = new BehaviorSubject<any>(null)


  create(data:any){
    return this._http.post(this.apiUrl+"/api/craiglist/create", data)
  }


  sync_list(){
    return this._http.get(this.apiUrl+"/api/craiglist/list").subscribe({
      next: res => this.craiglist_alarmsBS.next(res),
      error: e => {console.log("Authorization error")}
    })
  }

  delete(id:number){
    return this._http.delete(this.apiUrl + "/api/craiglist/delete/"+id)
  }


  get_sales_types(){
    return this._http.get<ISalesType[]>(this.apiUrl + '/api/craiglist/get_sales')
  }

  get_states_and_cities(){
    return this._http.get<ICities[]>(this.apiUrl + '/api/craiglist/get_cities')
  }
}



