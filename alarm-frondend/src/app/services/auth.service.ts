import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { UiService } from './ui.service';
import { BehaviorSubject } from 'rxjs';

export interface ICredential {
  email: string
  password: string
}

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor(
    private _http: HttpClient,
    private _uiSvc:UiService
    ) {
      this.apiUrl= environment.apiUrl
    }

  apiUrl:string = ""

  current_user = new BehaviorSubject(null)


  registerEmailPassword( formdata:ICredential ) {
    return this._http.post(this.apiUrl+"/api/register", formdata)
  }

  loginEmailAndPassword(formData:ICredential){
    return this._http.post(this.apiUrl+"/api/login", formData)
  }

  logout(){
    localStorage.removeItem('token')
    
    this.verify()
  }

  verify(){
    // It works at app.component.ts
    this._http.get(this.apiUrl+"/api/verify").subscribe({
      next: (user:any) => this.current_user.next(user['user']),
      error: _ => {
        this.current_user.next(null)
        this._uiSvc.update_menu_item_status('Login')
      }
    })
  }
}
