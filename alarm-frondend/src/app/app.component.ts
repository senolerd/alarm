import { Component } from '@angular/core';
import { AuthService } from './services/auth.service';
import { CraiglistService, ISalesType } from './services/craiglist.service';
import { UiService } from './services/ui.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  
  constructor(
    private _uiSvc:UiService,
    private _authSvc:AuthService,
    private _craiglistSvc: CraiglistService
  ){ }




  ngOnInit(){

    window.onresize = ()=>{
      this._uiSvc.widthBS.next(window.innerWidth)
    }
    this._craiglistSvc.sync_list()
    this._authSvc.verify()
    
  }
}
