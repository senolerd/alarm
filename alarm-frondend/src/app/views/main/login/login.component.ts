import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AuthService } from 'src/app/services/auth.service';
import { UiService } from 'src/app/services/ui.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(
    private _authSvc: AuthService,
    private _uiSvc: UiService
  ) { }

  formError:string= ""
  
  loginFG= new FormGroup({
    email: new FormControl(),
    password: new FormControl()
  })



  clearMsg(){
    this.formError = ""
  }

  login(){
    this._authSvc.loginEmailAndPassword(this.loginFG.value).subscribe({

      next: (res:any) => {
        localStorage.setItem("token", res.token)
        this._uiSvc.update_menu_item_status('Home')
       
      },
      error: e => {
        this.formError = e.error.error
      }
    })
  }

  ngOnInit(): void {
  }

}
