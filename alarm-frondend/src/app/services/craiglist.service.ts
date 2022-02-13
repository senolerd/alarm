import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';

export interface ISalesType { name: String, types: String[] }


@Injectable({
  providedIn: 'root'
})
export class CraiglistService {

  constructor(
    private _http:HttpClient
  ) { }

  sales_types = new BehaviorSubject<ISalesType[]>([])

  get_sales_types(){
    return this._http.get<ISalesType[]>('http://192.168.1.68:4444/craiglist/get_sales')
  }
}

