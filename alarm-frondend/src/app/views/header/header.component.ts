import { Component, OnInit } from '@angular/core';
import { UiService, ImenuItem } from 'src/app/services/ui.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor(
    private _uiSvc:UiService,
    
  ) { }
  

  menu_list:ImenuItem[]=[]
  isMenuOpen:any
  width:any


  menu_set(item_name:String){
    this._uiSvc.update_menu_item_status(item_name)
  }

  toggle_menu(){
    this._uiSvc.menu_openBS.next(!this.isMenuOpen)
  }

  ngOnInit(): void {
    this._uiSvc.menu_openBS.subscribe(menu_status =>{
      this.isMenuOpen = menu_status
    })
    this._uiSvc.widthBS.subscribe(width => this.width = width)


    this._uiSvc.menuBS.subscribe((menu_list:ImenuItem[]) =>{
      this.menu_list = menu_list
    })
  }

}



