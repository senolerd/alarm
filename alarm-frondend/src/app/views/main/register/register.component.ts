import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AuthService } from 'src/app/services/auth.service';
import { UiService } from 'src/app/services/ui.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  constructor(
    private _auth:AuthService,
    private _uiSvc:UiService
  ) { }

  registerForm= new FormGroup({
    email: new FormControl(),
    password: new FormControl()
  })

  formError:string= ""
  clearMsg(){
    this.formError = ""
  }
  registerUser(){
    this._auth.registerEmailPassword(this.registerForm.value).subscribe({
      next: _ => this._uiSvc.update_menu_item_status('Login'),
      error:  e => {this.formError = e.error.status}
    })
  }

  ngOnInit(): void {
  }

}
