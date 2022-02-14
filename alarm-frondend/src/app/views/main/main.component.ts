import { Component, OnInit } from '@angular/core';
import { ImenuItem, UiService } from 'src/app/services/ui.service';


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
  menu_list:ImenuItem[]=[]

  menu_toggle(){
    this._uiSvc.toggleMenu()
  }

  menu_set(item_name:String){
    this._uiSvc.update_menu_item_status(item_name)
    this.menu_toggle()
  }

  closedStart(){
    this._uiSvc.menu_openBS.next(false)
  }



  ngOnInit(): void {

    this._uiSvc.menuBS.subscribe((menu_list:ImenuItem[]) =>{
      this.menu_list = menu_list
    })

    this._uiSvc.active_menu_itemBS.subscribe(item =>{
      this.active_menu_item = item
    })

    this._uiSvc.menu_openBS.subscribe(menu_status =>{
      this.isMenuOpen = menu_status
    })
  }

}
