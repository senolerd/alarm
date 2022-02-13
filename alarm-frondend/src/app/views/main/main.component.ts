import { Component, OnInit } from '@angular/core';
import { UiService } from 'src/app/services/ui.service';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  constructor(
    private _uiSvc:UiService
  ) { }
  
  active_menu_item:String=""
  isMenuOpen:boolean = false

  menu_toggle(){
    this._uiSvc.menu_openBS.next(!this._uiSvc.menu_openBS.value)
  }

  closedStart(){
    this._uiSvc.menu_openBS.next(false)
  }

  ngOnInit(): void {
    this._uiSvc.active_menu_itemBS.subscribe(item =>{
      this.active_menu_item = item
    })

    this._uiSvc.menu_openBS.subscribe(menu_status =>{
      this.isMenuOpen = menu_status
    })
  }

}
