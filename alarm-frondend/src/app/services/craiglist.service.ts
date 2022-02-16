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
    return this._http.post(this.apiUrl+"/craiglist/create", data)
  }


  sync_list(){
    return this._http.get(this.apiUrl+"/craiglist/list").subscribe(res =>{
      this.craiglist_alarmsBS.next(res)
      console.log(res)
    })
  }

  delete(id:number){
    return this._http.delete(this.apiUrl+"/craiglist/delete/"+id)
  }


  get_sales_types(){
    return this._http.get<ISalesType[]>('http://192.168.1.68:4444/craiglist/get_sales')
  }

  get_states_and_cities(){
    return this._http.get<ICities[]>('http://192.168.1.68:4444/craiglist/get_cities')
  }
}



