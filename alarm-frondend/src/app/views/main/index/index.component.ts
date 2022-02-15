import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { CraiglistService } from 'src/app/services/craiglist.service';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.scss']
})
export class IndexComponent implements OnInit {

  constructor(
    private _authSvc:AuthService
  ) { }

  states_and_cities:any
  
  isddCraiglistActive:boolean=false

  ngOnInit(): void {
    this._authSvc.verify()
  }

}
