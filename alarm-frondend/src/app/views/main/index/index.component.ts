import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { CraiglistService, ICities, ISalesType } from 'src/app/services/craiglist.service';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.scss']
})
export class IndexComponent implements OnInit {

  constructor(
    private _craiglistSvc: CraiglistService,
    private _authSvc:AuthService
  ) { }

  states_and_cities:any

  ngOnInit(): void {
    this._craiglistSvc.get_states_and_cities()
    this._craiglistSvc.citiesBS.subscribe(states_and_cities => this.states_and_cities = states_and_cities)
    this._authSvc.verify()

  }

}
