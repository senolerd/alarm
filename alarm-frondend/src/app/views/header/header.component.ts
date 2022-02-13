import { Component, OnInit } from '@angular/core';
import { UiService, ImenuItem } from 'src/app/services/ui.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor(
    private _uiSvc:UiService
  ) { }
  

  menu_list:ImenuItem[]=[]

  menu_set(item_name:String){
    this._uiSvc.update_menu_item_status(item_name)
  }



  ngOnInit(): void {
    this._uiSvc.active_menuBS.subscribe((menu_list:ImenuItem[]) =>{
      this.menu_list = menu_list
    })
  }

}
