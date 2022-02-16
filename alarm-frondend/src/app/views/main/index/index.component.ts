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
    private _authSvc:AuthService,
    private _craiglistSvc: CraiglistService
  ) { }


  states_and_cities:any
  craiglist_alarms:any

  isddCraiglistActive:boolean=false

  delete(id:number){
    this._craiglistSvc.delete(id).subscribe(res =>{
      this._craiglistSvc.sync_list()
    })
  }

  ngOnInit(): void {
    this._authSvc.verify()
    this._craiglistSvc.craiglist_alarmsBS.subscribe(res => this.craiglist_alarms = res)
    console.log(this.craiglist_alarms)
    this._craiglistSvc.sync_list()

  }

}
