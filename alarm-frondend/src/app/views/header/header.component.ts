import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { UiService, ImenuItem } from 'src/app/services/ui.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor(
    private _uiSvc:UiService,
    private _authSvc:AuthService
    
  ) { }
  

  menu_list:ImenuItem[]=[]
  isMenuOpen:any
  width:any
  current_user= null

  menu_set(item_name:String){
    this._uiSvc.update_menu_item_status(item_name)
  }

  toggle_menu(){
    this._uiSvc.menu_openBS.next(!this.isMenuOpen)
  }

  logout(){
    this._authSvc.logout()
  }

  ngOnInit(): void {
    this._uiSvc.menu_openBS.subscribe(menu_status =>{
      this.isMenuOpen = menu_status
    })
    this._uiSvc.widthBS.subscribe(width => this.width = width)
    
    this._authSvc.current_user.subscribe(current_user => this.current_user = current_user)

    this._uiSvc.menuBS.subscribe((menu_list:ImenuItem[]) =>{
      this.menu_list = menu_list
    })
  }

}



