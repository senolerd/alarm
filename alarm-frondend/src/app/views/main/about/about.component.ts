import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.scss']
})
export class AboutComponent implements OnInit {

  constructor(
    private _authSvc:AuthService
  ) { }

  current_user:any

  ngOnInit(): void {
    this._authSvc.current_user.subscribe(current_user=>{
      this.current_user = current_user
    })
  }

}
