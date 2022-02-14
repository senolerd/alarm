import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

export interface ICredential {
  email: string
  password: string
}

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor(
    private _http: HttpClient
    ) {
      this.apiUrl= environment.apiUrl
    }

  apiUrl:string = ""

  registerEmailPassword( formdata:ICredential ) {
    return this._http.post(this.apiUrl+"/register", formdata)
  }

  loginEmailAndPassword(formData:ICredential){
    return this._http.post(this.apiUrl+"/login", formData)
  }
}
