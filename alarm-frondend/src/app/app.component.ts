import { Component } from '@angular/core';
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
  ){ }




  ngOnInit(){

    window.onresize = ()=>{
      this._uiSvc.widthBS.next(window.innerWidth)
    }

  }
}
